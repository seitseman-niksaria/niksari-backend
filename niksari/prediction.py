from keras.models import load_model  # TensorFlow is required for Keras to work
from teachable_machine import TeachableMachine
import numpy as np
from .models import FurnitureModel

teachable_model = TeachableMachine(model_path="teachable_machine\keras_model.h5", labels_file_path="teachable_machine\labels.txt")

# predicting user image using teachable machine library
def predict_image(user_image):

    result = teachable_model.classify_image(user_image)
    db_index = getIndex(result["class_index"]) # calling getIndex
    model = FurnitureModel.objects.values().get(pk=db_index) #Getting data from database with index
    return model

# Changin the "class_index" to corresponding database index
def getIndex(class_index):
    newIndex = {0:1, 1:24, 2:48}
    newValue = newIndex.get(class_index)
    return newValue