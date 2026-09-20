import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'saved_model', 'efficientnetb0.keras')
LABEL_PATH = os.path.join(BASE_DIR, 'saved_model', 'labels.txt')
IMAGE_SIZE = (224, 224)
