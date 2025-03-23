# -*- coding: utf-8 -*-
"""Untitled30.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f_8N8QjehMM-YXPDOBIoPe_Dv3HGlaGh
"""

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_dir = "/content/drive/MyDrive/Image/license plate"
img_width, img_height = 128, 128
batch_size = 32
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode="categorical"
)
validation_datagen = ImageDataGenerator(rescale=1.0/255)
validation_generator = validation_datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)
model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(img_width, img_height, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(5, activation="softmax")
])
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"])
model.summary()
epochs = 100

history = model.fit(train_generator,
                    epochs=epochs,
                    validation_data=validation_generator)
plt.plot(history.history['accuracy'], label="Kết quả huấn luyện")
plt.plot(history.history['val_accuracy'], label="Độ chính xác xác thực")
plt.xlabel("Số lần học")
plt.ylabel("Độ chính xác")
plt.legend()
plt.show()

model.save('model.contraimapdit.h5')

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/license plate/Huế/tải xuống.jpg'
img=load_img(path,target_size=(128,128))
plt.imshow(img)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img_array.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print(license_plate_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print("This license_plate is:", license_plate_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/license plate/Huế/tải xuống (1).jpg'
img=load_img(path,target_size=(128,128))
plt.imshow(img)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img_array.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print(license_plate_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print("This license_plate is:", license_plate_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/license plate/Huế/tải xuống (3).jpg'
img=load_img(path,target_size=(128,128))
plt.imshow(img)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img_array.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print(license_plate_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print("This license_plate is:", license_plate_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/license plate/Vũng tàu/tải xuống (1).jpg'
img=load_img(path,target_size=(128,128))
plt.imshow(img)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img_array.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print(license_plate_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print("This license_plate is:", license_plate_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/license plate/Vũng tàu/tải xuống.jpg'
img=load_img(path,target_size=(128,128))
plt.imshow(img)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img_array.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print(license_plate_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
license_plate_name=class_labels[prediction]
print("This license_plate is:", license_plate_name)