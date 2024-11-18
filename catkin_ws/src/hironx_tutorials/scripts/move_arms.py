#!/usr/bin/env python

import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler


def orientation_from_euler(r, p, y):
    """Converts euler to quaternion."""
    q = quaternion_from_euler(r, p, y)
    return Quaternion(q[0], q[1], q[2], q[3])


def move_arms():
    """Moves two arms with specified trajectories."""
    rospy.init_node("moveit_command_sender")
    robot = moveit_commander.RobotCommander()
    rarm = moveit_commander.MoveGroupCommander("right_arm")
    larm = moveit_commander.MoveGroupCommander("left_arm")

    rarm_initial_pose = rarm.get_current_pose().pose
    larm_initial_pose = larm.get_current_pose().pose

    rospy.loginfo("Start moving right arm...")
    target_pose_r = geometry_msgs.msg.Pose()
    target_pose_r.position.x = 0.325471850974-0.01
    target_pose_r.position.y = -0.182271241593-0.3
    target_pose_r.position.z = 0.0676272396419+0.3
    target_pose_r.orientation = orientation_from_euler(0, -1.57, 0)
    rarm.set_pose_target(target_pose_r)
    rarm.go()
    rospy.sleep(rospy.Duration.from_sec(1))

    rospy.loginfo("Start moving lefts arm...")
    target_pose_l = [
        target_pose_r.position.x,
        -target_pose_r.position.y,
        target_pose_r.position.z,
        target_pose_r.orientation.x,
        target_pose_r.orientation.y,
        target_pose_r.orientation.z,
        target_pose_r.orientation.w
    ]
    larm.set_pose_target(target_pose_l)
    larm.go()
    rospy.sleep(rospy.Duration.from_sec(1))
    rarm.clear_pose_targets()

    rospy.loginfo("Moving right arm again...")
    target_pose_r.position.x = 0.221486843301
    target_pose_r.position.y = -0.0746407547512
    target_pose_r.position.z = 0.642545484602
    target_pose_r.orientation.x = 0.0669013615474
    target_pose_r.orientation.y = -0.993519060661
    target_pose_r.orientation.z = 0.00834224628291
    target_pose_r.orientation.w = 0.0915122442864
    rarm.set_pose_target(target_pose_r)
    rarm.go()
    rospy.sleep(rospy.Duration.from_sec(1))

    rospy.loginfo("Back to initia poses.")
    rarm.set_pose_target(rarm_initial_pose)
    larm.set_pose_target(larm_initial_pose)
    rarm.go()
    larm.go()
    rospy.sleep(rospy.Duration.from_sec(2))


if __name__ == '__main__':
    try:
        move_arms()
    except rospy.ROSInterruptException:
        pass
