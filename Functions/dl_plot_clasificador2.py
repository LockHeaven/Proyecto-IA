import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.imshow(img.reshape(100, 60), cmap=plt.cm.binary)
    if predictions_array == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel("Pedicted: {} Real: {}".format(predictions_array,
                                true_label),color=color)
    plt.xticks([])
    plt.yticks([])