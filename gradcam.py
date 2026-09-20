import os
import numpy as np
import tensorflow as tf
from PIL import Image
from predict import load_model, preprocess_path

def _find_last_conv(model):
    for layer in reversed(model.layers):
        try:
            shape = layer.output.shape
            if len(shape) == 4:
                return layer
        except Exception:
            continue
    raise ValueError("Layer konvolusi/feature map 4D tidak ditemukan untuk Grad-CAM.")

def generate_gradcam(image_path, output_path, class_index=None):
    model = load_model()
    target = _find_last_conv(model)
    grad_model = tf.keras.models.Model(model.inputs, [target.output, model.output])
    x = preprocess_path(image_path)
    with tf.GradientTape() as tape:
        conv_out, predictions = grad_model(x, training=False)
        if class_index is None:
            class_index = int(tf.argmax(predictions[0]))
        score = predictions[:, class_index]
    grads = tape.gradient(score, conv_out)
    if grads is None:
        raise ValueError("Gradien Grad-CAM tidak tersedia untuk layer target.")
    weights = tf.reduce_mean(grads, axis=(1, 2))
    cam = tf.reduce_sum(weights[:, None, None, :] * conv_out, axis=-1)[0]
    cam = tf.maximum(cam, 0)
    cam = cam / (tf.reduce_max(cam) + 1e-8)
    cam = (cam.numpy() * 255).astype(np.uint8)
    original = Image.open(image_path).convert("RGB")
    cam_img = Image.fromarray(cam).resize(original.size)
    heat = np.asarray(cam_img, dtype=np.float32) / 255.0
    arr = np.asarray(original, dtype=np.float32)
    overlay = arr.copy()
    overlay[..., 0] = np.clip(arr[..., 0] + 180 * heat, 0, 255)
    overlay[..., 1] = np.clip(arr[..., 1] * (1 - 0.35 * heat), 0, 255)
    overlay[..., 2] = np.clip(arr[..., 2] * (1 - 0.35 * heat), 0, 255)
    Image.fromarray(overlay.astype(np.uint8)).save(output_path, quality=92)
    return output_path
