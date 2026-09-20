"""
diagnose_model.py
Run:
    python diagnose_model.py path/to/image.jpg
"""
import sys
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL = "saved_model/efficientnetb0.keras"
LABELS = "saved_model/labels.txt"

if len(sys.argv) != 2:
    raise SystemExit("Usage: python diagnose_model.py path/to/image.jpg")

labels = [x.strip() for x in open(LABELS, encoding="utf-8") if x.strip()]
model = tf.keras.models.load_model(MODEL, compile=False)

img = Image.open(sys.argv[1]).convert("RGB").resize((224,224))
x = np.expand_dims(np.asarray(img, dtype=np.float32), 0)

p = model.predict(x, verbose=0)[0]
for i in np.argsort(p)[::-1]:
    print(f"{labels[int(i)]:25s} {float(p[int(i)])*100:7.2f}%")
