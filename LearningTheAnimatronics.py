import tensorflow as tf
from tensorflow import keras
import keras
from keras_video import VideoFrameGenerator
import os
import numpy as np
import pickle

"""
This program trains an ai to determin the difference between each animatronic in Unltimate Custom Night

*May not need this file at all
*Could possibly do this in "UltimateCustomNightNEAT.py"
"""

#Load data/video


#Converts a video to frames
def video_to_frames(video):
    path = os.path.join(config.test_path, 'temporary_images')

    if os.path.exists(path):
        shutil.rmtree(path)
    
    os.makedirs(path)
    video_path = os.path.join(config.test_path, 'video', video)
    
    count = 0
    image_list = []
    # Path to video file
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        
        ret, frame = cap.read()
        
        if ret is False:
            break
        
        cv2.imwrite(os.path.join(config.test_path, 'temporary_images', 'frame%d.jpg' % count), frame)
        image_list.append(os.path.join(config.test_path, 'temporary_images', 'frame%d.jpg' % count))
        count += 1

    cap.release()
    cv2.destroyAllWindows()
    
    return image_list