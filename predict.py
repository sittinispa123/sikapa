import os
import numpy as np
import tensorflow as tf
from PIL import Image
from config import MODEL_PATH, LABEL_PATH, IMAGE_SIZE

_model = None
_labels = None


def load_labels():
    global _labels

    if _labels is None:
        if not os.path.exists(LABEL_PATH):
            raise FileNotFoundError(
                f"labels.txt tidak ditemukan: {LABEL_PATH}"
            )

        with open(LABEL_PATH, "r", encoding="utf-8") as f:
            _labels = [x.strip() for x in f if x.strip()]

    return _labels


def load_model():
    global _model

    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model tidak ditemukan: {MODEL_PATH}"
            )

        _model = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False
        )

    return _model


def preprocess_path(path):
    """
    IMPORTANT:
    Model EfficientNet-B0 di project ini sudah memiliki
    preprocessing internal:
        Rescaling(1/255)
        Normalization
        Rescaling

    Karena itu input dari aplikasi harus berupa piksel
    0..255 dan TIDAK boleh dibagi 255 lagi di sini.
    """

    image = Image.open(path).convert("RGB")

    image = image.resize(
        IMAGE_SIZE,
        Image.Resampling.BILINEAR
    )

    arr = np.asarray(
        image,
        dtype=np.float32
    )

    return np.expand_dims(
        arr,
        axis=0
    )


def predict_complete(path):
    model = load_model()
    labels = load_labels()

    x = preprocess_path(path)

    pred = model.predict(
        x,
        verbose=0
    )[0]

    pred = np.asarray(
        pred,
        dtype=np.float32
    )

    if len(pred) != len(labels):
        raise ValueError(
            f"Output model ({len(pred)}) "
            f"tidak sesuai labels.txt ({len(labels)})."
        )

    # Softmax safeguard
    if not np.isclose(
        float(np.sum(pred)),
        1.0,
        atol=1e-3
    ):
        pred = tf.nn.softmax(pred).numpy()

    order = np.argsort(
        pred
    )[::-1][:3]

    top3 = [
        {
            "label": labels[int(i)],
            "confidence": float(pred[int(i)])
        }
        for i in order
    ]

    best = int(order[0])

    return {
        "disease": labels[best],
        "confidence": float(pred[best]),
        "top3": top3
    }
