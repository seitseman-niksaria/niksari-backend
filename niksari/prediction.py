from keras.models import load_model  # TensorFlow is required for Keras to work
from teachable_machine import TeachableMachine
import numpy as np


teachable_model = TeachableMachine(model_path="teachable_machine\keras_model.h5", labels_file_path="teachable_machine\labels.txt")

# pip install keras
# pip install teachable_machine
# pip install numpy ?
# pip install opencv-python-headless ?
def predict_image(user_image):

    result = teachable_model.classify_image(user_image)

    print("class_index", result["class_index"])

    print("class_name:::", result["class_name"])

    print("class_confidence:", result["class_confidence"])

    print("predictions:", result["predictions"])

    return result["class_name"]