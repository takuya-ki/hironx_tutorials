#!/usr/bin/env python

import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler


def orientation_from_euler(r,p,y):
	q = quaternion_from_euler(r,p,y)
	return Quaternion(q[0],q[1],q[2],q[3])


def main():
	rospy.init_node("moveit_command_sender")

	robot = moveit_commander.RobotCommander()

	print , " Robot Groups:"
	print robot.get_group_names()

	print , " Printing robot state"
	print robot.get_current_state()
	print

	rarm = moveit_commander.MoveGroupCommander("right_arm")
	larm = moveit_commander.MoveGroupCommander("left_arm")

	print  " Right arm "
	print , " Reference frame: %s" % rarm.get_planning_frame()
	print , " Reference frame: %s" % rarm.get_end_effector_link()

	print  " Left ight arm "
	print , " Reference frame: %s" % larm.get_planning_frame()
	print , " Reference frame: %s" % larm.get_end_effector_link()

	#Right Arm Initial Pose
	rarm_initial_pose = rarm.get_current_pose().pose
	print , " Printing Right Hand initial pose: "
	print rarm_initial_pose

	#Light Arm Initial Pose
	larm_initial_pose = larm.get_current_pose().pose
	print , " Printing Left Hand initial pose: "
	print larm_initial_pose

	# gripper.soft_close()
	target_pose_r = geometry_msgs.msg.Pose()
	target_pose_r.position.x = 0.325471850974-0.01
	target_pose_r.position.y = -0.182271241593-0.3
	target_pose_r.position.z = 0.0676272396419+0.3
	target_pose_r.orientation = orientation_from_euler(0,-1.57,0)
	rarm.set_pose_target(target_pose_r)

	print ," plan1 ..."
	rarm.go()
	rospy.sleep(1)

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

	print ," plan2 ..."
	larm.go()
	rospy.sleep(1)

	#Clear pose
	rarm.clear_pose_targets()

	#Right Hand
	target_pose_r.position.x = 0.221486843301
	target_pose_r.position.y = -0.0746407547512
	target_pose_r.position.z = 0.642545484602
	target_pose_r.orientation.x = 0.0669013615474
	target_pose_r.orientation.y = -0.993519060661
	target_pose_r.orientation.z = 0.00834224628291
	target_pose_r.orientation.w = 0.0915122442864
	rarm.set_pose_target(target_pose_r)

	print , " plan3..."
	rarm.go()
	rospy.sleep(1)
	# gripper.goto_position(10.0,100.0)

	print ,"Initial pose ..."
	rarm.set_pose_target(rarm_initial_pose)
	larm.set_pose_target(larm_initial_pose)
	rarm.go()
	larm.go()
	rospy.sleep(2)
	exit(0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
