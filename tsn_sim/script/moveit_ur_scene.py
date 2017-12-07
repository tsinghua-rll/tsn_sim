#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# File Name : moveit_baxter.py
# Purpose :
# Creation Date : 06-12-2017
# Last Modified : 2017年12月07日 星期四 21时42分50秒
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped


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
    rospy.sleep(2) # essential for add scene!!!

    print(robot.get_current_state()) # ok for ur
    print(robot.get_group_names())
    group = moveit_commander.MoveGroupCommander("manipulator") # or endeffector(currently, we do not have it)
    # set planning scene
    desktop_plane = PoseStamped()
    desktop_plane.header.frame_id = robot.get_planning_frame()
    desktop_plane.pose.position.x = 1.0
    desktop_plane.pose.position.y = 0.0
    desktop_plane.pose.position.z = -0.1
    desktop_plane.pose.orientation.w = 1.0
    scene.add_box("table", desktop_plane, (3, 1.2, 0.01))

    print(group.get_current_pose()) # ok for ur
    # set_target_pose(group)
    rospy.spin()


def set_target_pose(group):
    # just control the target pose of end point
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.orientation.x = 0.0
    pose_target.orientation.y = 0.0
    pose_target.orientation.z = 0.0
    pose_target.position.x = 0.4
    pose_target.position.y = 0.1
    pose_target.position.z = 0.5
    group.set_pose_target(pose_target)
    group.plan()
    print(group.go())  # true for success, false for failed


if __name__ == '__main__':
    main(sys.argv)
