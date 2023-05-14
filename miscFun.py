# This file contains necesasry functions to run the PINN algorithm


# import libraries
#import sys
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
import tensorflow as tf
from keras import backend as K
from tensorflow.keras.layers import Multiply
#, Add, Subtract
from bokeh.layouts import column, row
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh import palettes

import random

# functions
#mse = tf.keras.losses.MeanSquaredError()

def set_seeds(seed=0):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    tf.random.set_seed(seed)
    np.random.seed(seed)
def set_global_determinism(seed=0):
    set_seeds(seed=seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    os.environ['TF_CUDNN_DETERMINISTIC'] = '1'
    tf.config.threading.set_inter_op_parallelism_threads(1)
    tf.config.threading.set_intra_op_parallelism_threads(1)

# figure font adjustments
def figure_settings(fig,label_font_size='12pt',legend_fix=True):
    fig.yaxis.axis_label_text_font_size  = '16pt'
    fig.xaxis.major_label_text_font_size = label_font_size
    fig.yaxis.major_label_text_font_size = label_font_size
    fig.yaxis.major_label_text_font_style = "bold"
    fig.xaxis.major_label_text_font_style = "bold"
    fig.xaxis.axis_label_text_font_size  = '16pt'
    fig.axis.axis_label_text_font_style = 'bold'
    
    # fig.legend.location = 'bottom_right'
    if legend_fix:
        fig.legend.label_text_font_size = '14pt'
        fig.legend.title_text_font = 'Arial'
    return fig