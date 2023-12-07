import os
import argparse
import cv2
import numpy as np
import sys
import glob
import importlib.util
import firebase_admin

from firebase_admin import credentials
from firebase_admin import db
from picamera import PiCamera
from time import sleep
from brightpi import *

MODEL_NAME = 'detect'
GRAPH_NAME = 'detect.tflite'
LABELMAP_NAME = 'labelmap.txt'

IM_NAME = 'test.jpg'
#IM_DIR = args.imagedir

# Import TensorFlow libraries
# If tflite_runtime is installed, import interpreter from tflite_runtime, else import from regular tensorflow
# If using Coral Edge TPU, import the load_delegate library
pkg = importlib.util.find_spec('tflite_runtime')
if pkg:
    from tflite_runtime.interpreter import Interpreter
    if use_TPU:
        from tflite_runtime.interpreter import load_delegate
else:
    from tensorflow.lite.python.interpreter import Interpreter
    if use_TPU:
        from tensorflow.lite.python.interpreter import load_delegate

# If using Edge TPU, assign filename for Edge TPU model
if use_TPU:
    # If user has specified the name of the .tflite file, use that name, otherwise use default 'edgetpu.tflite'
    if (GRAPH_NAME == 'detect.tflite'):
        GRAPH_NAME = 'edgetpu.tflite'


# Get path to current working directory
CWD_PATH = os.getcwd()