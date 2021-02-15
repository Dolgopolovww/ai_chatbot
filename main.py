import numpy as np
from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import os
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" # для исклчение ошибки