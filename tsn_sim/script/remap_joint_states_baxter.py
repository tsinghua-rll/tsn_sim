#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# File Name : remap_joint_states_baxter.py
# Purpose :
# Creation Date : 06-12-2017
# Last Modified : 2017年12月06日 星期三 21时43分23秒
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

import rospy 
from sensor_msgs.msg import JointState

publisher = None 
joint_state_topic = "/robot/joint_states"
remapped_joint_state_topic = "/joint_states"

def callback(data):
    global publisher 
    publisher.publish(data)


def main():
    global publisher
    rospy.init_node('remapped_joint_state_baxter', anonymous=True)
    publisher = rospy.Publisher(remapped_joint_state_topic, JointState) 
    rospy.Subscriber(joint_state_topic, JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
