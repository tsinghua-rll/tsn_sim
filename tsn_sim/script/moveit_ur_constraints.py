#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# File Name : moveit_baxter.py
# Purpose :
# Creation Date : 06-12-2017
# Last Modified : 2017年12月07日 星期四 01时07分17秒
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msg import JointState


def joint_state_callback(data):
    joint_poses = data.position 
    elbow = joint_poses[0]
    shoulder_lift = joint_poses[1]
    shoulder_pan = joint_poses[2]
    wrist_1 = joint_poses[3]
    wrist_2 = joint_poses[4]
    wrist_3 = joint_poses[5]


def main(args):
    moveit_commander.roscpp_initialize(args)
    rospy.init_node('moveit_ur', anonymous=True)
    rospy.Subscriber("/joint_states", JointState, joint_state_callback)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    print(robot.get_current_state()) # ok for ur
    print(robot.get_group_names())
    group = moveit_commander.MoveGroupCommander("manipulator") # or endeffector(currently, we do not have it)
    print(group.get_current_pose()) # ok for ur
    set_target_pose(group)


def set_target_pose(group):
    # set target pose of end point
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.orientation.x = 0.0
    pose_target.orientation.y = 0.0
    pose_target.orientation.z = 0.0
    pose_target.position.x = 0.4
    pose_target.position.y = 0.1
    pose_target.position.z = 0.5
    # set_pose_target = set_position_target + set_orintation_target
    group.set_pose_target(pose_target)
    
    # set joint target(as a dict) 
    group.set_joint_value_target({
        "elbow_joint" : 0.0,
    })
    
    # set tolarence
    group.set_goal_tolerance(1.0) 



    group.plan()
    print(group.go())  # true for success, false for failed


if __name__ == '__main__':
    main(sys.argv)
