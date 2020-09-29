import cv2
import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


path_modelo = '/home/andalu30/Descargas/modeloKeras/keras_model.h5'

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)


# Load the model
model = tensorflow.keras.models.load_model(path_modelo)
cap = cv2.VideoCapture(0)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


while True:
    ret, frame = cap.read()
    
    if not ret:
        print('Error de captura')
        break

    frame = cv2.resize(frame, (224,224))





    # Normalize the image
    normalized_image_array = (frame.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)


    if prediction[0][0] > prediction[0][1]:
        cv2.putText(frame,'Juan', (25,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),1)
    else:
        cv2.putText(frame,'No Juan', (25,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),1)

    cv2.imshow('frame',frame)


    if chr(cv2.waitKey(16)&255) == 'q':
        break

cv2.DestroyAllWindows()
cap.release()