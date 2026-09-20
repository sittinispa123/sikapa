import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from predict import predict_complete
from gradcam import generate_gradcam
from data.disease_info import DISEASE_INFO, normalize_disease_name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
GRADCAM_FOLDER = os.path.join(BASE_DIR, "static", "gradcam")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GRADCAM_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
@app.route("/api/predict", methods=["POST"])
def predict():
    field = "file" if "file" in request.files else "image" if "image" in request.files else None
    if not field:
        return jsonify({"success": False, "error": "File gambar tidak ditemukan."}), 400
    file = request.files[field]
    if not file.filename:
        return jsonify({"success": False, "error": "Silakan pilih gambar."}), 400
    if not allowed_file(file.filename):
        return jsonify({"success": False, "error": "Format harus JPG, JPEG, PNG, atau WEBP."}), 400
    filename = datetime.now().strftime("%Y%m%d_%H%M%S_") + secure_filename(file.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(image_path)
    try:
        result = predict_complete(image_path)
        disease = normalize_disease_name(result["disease"])
        confidence = float(result["confidence"]) * 100
        top3 = [{"label": normalize_disease_name(x["label"]), "confidence": round(float(x["confidence"])*100, 2)} for x in result["top3"]]
        info = DISEASE_INFO.get(disease, {"description":"Informasi belum tersedia.","solution":"Lakukan pemeriksaan lebih lanjut.","handling":[],"prevention":[]})
        gradcam_name = "gradcam_" + os.path.splitext(filename)[0] + ".jpg"
        gradcam_path = os.path.join(GRADCAM_FOLDER, gradcam_name)
        try:
            generate_gradcam(image_path, gradcam_path, class_index=None)
        except Exception as grad_error:
            print("Grad-CAM warning:", grad_error)
            gradcam_name = None
        return jsonify({"success": True, "disease": disease, "class": disease, "confidence": round(confidence,2), "description": info["description"], "solution": info["solution"], "handling": info["handling"], "prevention": info["prevention"], "top3": top3, "image": filename, "gradcam": gradcam_name})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )