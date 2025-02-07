import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
from keras.models import load_model
# import tensorflow as tf
from sys import argv
from itertools import chain

model = None
pub = None

def preprocessing(data):
    k = 24
    dim = k*2
    matrix = np.zeros([dim,dim,1])
    
    cut_angle = 90
    
    for i in chain(range(180-cut_angle//2), range(180+cut_angle//2,360)):
      if data[i] < 1:
        angle = np.radians(i)
        r = data[i]
        x = int(r * np.sin(angle) * k + k)
        y = int(r * np.cos(angle) * k + k)
        if 0 <= x < dim and 0 <= y < dim:
                matrix[y,x] = 1

    
    data = matrix
    
    return data

def callback(data):
    global pub
    global model
    data_in = np.asarray(data.ranges)
    rospy.loginfo(data_in.size)
    data_in = preprocessing(data_in)
    
    out = model.predict(np.array([data_in]))
    msg = Twist()
    speed = 1
    msg.linear.x = out[0][0] * speed
    msg.angular.z = out[0][1] * speed
    pub.publish(msg)
    
def run_cnn():
    global pub
    rospy.init_node('run_cnn', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    model = load_model(argv[1])
    run_cnn()
