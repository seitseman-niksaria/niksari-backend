from keras.models import load_model  # TensorFlow is required for Keras to work
from teachable_machine import TeachableMachine
import numpy as np


teachable_model = TeachableMachine(model_path="teachable_machine\keras_model.h5", labels_file_path="teachable_machine\labels.txt")

# predicting user image using teachable machine library
def predict_image(user_image):

    result = teachable_model.classify_image(user_image)

    print("class_index", result["class_index"])

    print("class_name:", result["class_name"])

    print("class_confidence:", result["class_confidence"])

    print("predictions:", result["predictions"])

    
    class_name = result["class_name"]
    class_index = result["class_index"]
    class_confidence = result["class_confidence"]

    return {
        "class_name": class_name,
        "class_index": class_index,
        "class_confidence": class_confidence
    }