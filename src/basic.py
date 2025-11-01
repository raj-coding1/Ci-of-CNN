import tensorflow as tf 
from tensorflow.keras import models,layers

model = models.Sequential([
    layers.Conv2D(32,(3,3),activation = 'relu', input_shape = (28,28,3)),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(32,(3,3),activation = 'relu', input_shape = (28,28)),
    layers.MaxPooling2D((2,2))
]
    
)
model.summary()