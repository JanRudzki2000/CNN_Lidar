# CNN_Lidar

CNN_Lidar.ipynb preprocess data from lidar (and velocity) to create an images and train convolution neural network with regression.
run.py is a ROS node which in real time preprocess data from lidar and put image to CNN model. Output from model is velocity x and rotation. Robot is able to drive through maze.
