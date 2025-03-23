# -*- coding: utf-8 -*-
"""Untitled39.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V6_oTbdtFQxcfG0jSTlD1Qg7c7MyWMwY
"""

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_dir = "/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát"
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
    Dense(3, activation="softmax")
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

model.save('model_contraimapdit.h5')

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát/Trần Vĩnh Phát/z6390301286479_2707ca43fee2393823bb3dc1f0a3e8c9.jpg'
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
Face_name=class_labels[prediction]
print(Face_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
Face_name=class_labels[prediction]
print("This Face is:", Face_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát/Trần Vĩnh Phát/z6390301278662_45f41fd3826de8159b87948118f27a1b.jpg'
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
Face_name=class_labels[prediction]
print(Face_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
Face_name=class_labels[prediction]
print("This Face is:", Face_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát/Trần Vĩnh Phát/z6390301272853_c41dca55bc5215c852707f0dcb79c1af.jpg'
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
Face_name=class_labels[prediction]
print(Face_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
Face_name=class_labels[prediction]
print("This Face is:", Face_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát/Đình Trí/z6390450952643_dcfe07ef4945a183d645b4e99b56bf2c.jpg'
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
Face_name=class_labels[prediction]
print(Face_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
Face_name=class_labels[prediction]
print("This Face is:", Face_name)

from tensorflow.keras.utils import load_img
import numpy as np
path = '/content/drive/MyDrive/Image/Face/Trần Vĩnh Phát/Kiều Thành Đức/z6389406409680_a5629cb41257bf01cce7c7bed8643163.jpg'
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
Face_name=class_labels[prediction]
print(Face_name)
plt.show()
img_array=np.array(img)
img_array=img_array/255.0
img=img.reshape(1,128,128,3)
prediction=np.argmax(model.predict(img))
print(prediction)
class_labels={v:k for k,v in train_generator.class_indices.items()}
print(class_labels)
Face_name=class_labels[prediction]
print("This Face is:", Face_name)