# Importamos el dataset CIFAR-10 desde TensorFlow Datasets
import tensorflow_datasets as tfds

# Importamos las clases necesarias para construir la red neuronal
from tensorflow.keras.models import Sequential              # Para crear un modelo secuencial
from tensorflow.keras.layers import Flatten, Dense          # Flatten para aplanar imágenes, Dense para capas densas
from tensorflow.keras.utils import to_categorical           # Para convertir etiquetas a one-hot encoding

# Cargamos el dataset CIFAR-10 desde tensorflow_datasets
# as_supervised=True devuelve tuplas (imagen, etiqueta)
(ds_train, ds_test), ds_info = tfds.load(
    'cifar10',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True
)

# Convertimos los datasets a arrays (opcional: también se puede usar tf.data directamente)
import numpy as np

x_train = []
y_train = []
for image, label in tfds.as_numpy(ds_train):
    x_train.append(image)
    y_train.append(label)

x_test = []
y_test = []
for image, label in tfds.as_numpy(ds_test):
    x_test.append(image)
    y_test.append(label)

x_train = np.array(x_train) / 255.0
x_test = np.array(x_test) / 255.0
y_train = to_categorical(np.array(y_train), 10)
y_test = to_categorical(np.array(y_test), 10)

# Definimos el modelo secuencial
model = Sequential([
    Flatten(input_shape=(32, 32, 3)),
    Dense(1000, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilamos el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamos el modelo
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_test, y_test))

# Guardamos el modelo
model.save('cifar10_model.h5')
