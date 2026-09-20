PALMCARE AI - SKRIPSI FINAL
===========================

Fitur:
- Mobile-first responsive website
- EfficientNet-B0 inference
- 6 kelas penyakit daun kelapa sawit
- Confidence dan Top-3 prediction
- Knowledge-Based System: deskripsi, solusi, penanganan, pencegahan
- Grad-CAM
- Upload dan preview gambar

STRUKTUR:
app.py
predict.py
gradcam.py
config.py
data/disease_info.py
templates/index.html
saved_model/efficientnetb0.keras
saved_model/labels.txt
static/uploads/
static/gradcam/

INSTALASI WINDOWS:
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python app.py
5. Buka http://127.0.0.1:5000

Catatan: Model disimpan di saved_model/efficientnetb0.keras dan labels.txt berasal dari model project yang tersedia. Prediksi tetap bergantung pada kualitas model dan data uji.
