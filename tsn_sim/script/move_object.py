#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# File Name : move_object.py
# Purpose :
# Creation Date : 05-12-2017
# Last Modified : 2017年12月05日 星期二 23时51分46秒
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

from __future__ import print_function

import sys 
import rospy 
import numpy as np 
from random import randint
from gazebo_msgs.msg import ModelState

available_object = [
    "coke_can",
    "plastic_cup",
    "beer",
    "wood_cube_10cm"
]

move_object_topic = "/gazebo/set_model_state"

def set_object_pose(publisher, object_name, xyz=None):
    state = ModelState()
    state.model_name = object_name 
    if xyz:
        state.pose.position.x = xyz[0]
        state.pose.position.y = xyz[1]
        state.pose.position.z = xyz[2]
    else:
        state.pose.position.x = np.random.rand()
        state.pose.position.y = np.random.rand()
        state.pose.position.z = np.random.rand()

    publisher.publish(state)
    rospy.loginfo("set pose for model {}".format(object_name))

def main(argv):
    pub = rospy.Publisher(move_object_topic, ModelState, queue_size=10)
    rospy.init_node("demo_set_object_pose", anonymous=True) 
    rate = rospy.Rate(1) # 1 Hz
    while not rospy.is_shutdown(): # we must call set_object_pose for more than one time
        # set_object_pose(pub, available_object[randint(0, len(available_object)-1)])
        set_object_pose(pub, 'plastic_cup', [0,-0.9,1.0])
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv)
