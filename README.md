# CNN_Lidar

CNN_Lidar.ipynb preprocess data from lidar (and velocity) to create an images and train convolution neural network with regression.

run_cnn.py is a ROS node which in real time preprocess data from lidar and put image to CNN model. Output from model is velocity x and rotation. Robot is able to drive through maze.

Video of robot driving in maze
https://youtu.be/KiHUgZ3TXWU
