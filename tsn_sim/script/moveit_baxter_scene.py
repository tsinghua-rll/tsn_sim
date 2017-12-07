#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# File Name : moveit_baxter.py
# Purpose :
# Creation Date : 06-12-2017
# Last Modified : 2017年12月07日 星期四 19时36分49秒
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
    l_gripper_l = joint_poses[1]
    l_gripper_r = joint_poses[2]
    l_e0 = joint_poses[3]
    l_e1 = joint_poses[4]
    l_s0 = joint_poses[5]
    l_s1 = joint_poses[6]
    l_w0 = joint_poses[7]
    l_w1 = joint_poses[8]
    l_w2 = joint_poses[9]

    r_gripper_l = joint_poses[10]
    r_gripper_r = joint_poses[11]
    r_e0 = joint_poses[12]
    r_e1 = joint_poses[13]
    r_s0 = joint_poses[14]
    r_s1 = joint_poses[15]
    r_w0 = joint_poses[16]
    r_w1 = joint_poses[17]
    r_w2 = joint_poses[18]


def main(args):
    moveit_commander.roscpp_initialize(args)
    rospy.init_node('moveit_baxter', anonymous=True)
    rospy.Subscriber("/robot/joint_states", JointState, joint_state_callback)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    rospy.sleep(2) # essential for add scene!!!

    print(robot.get_current_state())
    print(robot.get_group_names())
    group = moveit_commander.MoveGroupCommander("right_arm")
    # set planning scene
    desktop_plane = PoseStamped()
    desktop_plane.header.frame_id = robot.get_planning_frame()
    desktop_plane.pose.position.x = 0.8
    desktop_plane.pose.position.y = -0.4
    desktop_plane.pose.position.z = 0.0
    desktop_plane.pose.orientation.w = 1.0
    scene.add_box("table", desktop_plane, (1, 1.2, 0.01))

    print(group.get_current_pose())
    set_target_pose(group)
    rospy.spin()


def set_target_pose(group):
    # just control the target pose of end point
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.orientation.x = 0.0
    pose_target.orientation.y = 0.0
    pose_target.orientation.z = 0.0
    pose_target.position.x = 0.0
    pose_target.position.y = -0.5
    pose_target.position.z = 1.5
    group.set_pose_target(pose_target)
    group.plan()
    print(group.go())  # true for success, false for failed


if __name__ == '__main__':
    main(sys.argv)
