#!/usr/bin/env python

import math
import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion, Pose
from tf.transformations import quaternion_from_euler


def orientation_from_euler(r, p, y):
    """Converts euler to quaternion."""
    q = quaternion_from_euler(r, p, y)
    return Quaternion(q[0], q[1], q[2], q[3])


def wave_arms():
    """Moves two arms with specified trajectories."""
    rospy.init_node("moveit_command_sender")
    robot = moveit_commander.RobotCommander()
    botharms = moveit_commander.MoveGroupCommander("botharms")
    botharms.set_max_velocity_scaling_factor(1.0)
    botharms.set_max_acceleration_scaling_factor(1.0)
    torso = moveit_commander.MoveGroupCommander("torso")
    torso.set_max_velocity_scaling_factor(1.0)
    torso.set_max_acceleration_scaling_factor(1.0)

    while not rospy.is_shutdown():
        torso.set_joint_value_target([0.3])
        torso.go()

        target_pose_r = Pose()
        target_pose_l = Pose()
        target_pose_r.position.x = 0.4
        target_pose_r.position.y = -0.3
        target_pose_r.position.z = 0.7
        target_pose_r.orientation.x = 0.0669013615474
        target_pose_r.orientation.y = -0.993519060661
        target_pose_r.orientation.z = 0.00834224628291
        target_pose_r.orientation.w = 0.0915122442864
        target_pose_l.position.x = 0.4
        target_pose_l.position.y = 0.3
        target_pose_l.position.z = 0.7
        target_pose_l.orientation.x = 0.0669013615474
        target_pose_l.orientation.y = -0.993519060661
        target_pose_l.orientation.z = 0.00834224628291
        target_pose_l.orientation.w = 0.0915122442864
        botharms.set_pose_target(target_pose_r, 'RARM_JOINT5_Link')
        botharms.set_pose_target(target_pose_l, 'LARM_JOINT5_Link')
        botharms.go()

        torso.set_joint_value_target([-0.3])
        torso.go()

        q = quaternion_from_euler(0, -math.pi/2, 0)
        target_pose_r.position.x = 0.3
        target_pose_r.position.y = -0.3
        target_pose_r.position.z = 0.0
        target_pose_r.orientation.x = q[0]
        target_pose_r.orientation.y = q[1]
        target_pose_r.orientation.z = q[2]
        target_pose_r.orientation.w = q[3]
        target_pose_l.position.x = 0.3
        target_pose_l.position.y = 0.3
        target_pose_l.position.z = 0.0
        target_pose_l.orientation.x = q[0]
        target_pose_l.orientation.y = q[1]
        target_pose_l.orientation.z = q[2]
        target_pose_l.orientation.w = q[3]
        botharms.set_pose_target(target_pose_r, 'RARM_JOINT5_Link')
        botharms.set_pose_target(target_pose_l, 'LARM_JOINT5_Link')
        botharms.go()


if __name__ == '__main__':
    try:
        wave_arms()
    except rospy.ROSInterruptException:
        pass
