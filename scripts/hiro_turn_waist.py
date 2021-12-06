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

	# print " Robot Groups:"
	# print robot.get_group_names()
	# print ""

	# print " Printing robot state"
	# print robot.get_current_state()
	# print ""

	torso = moveit_commander.MoveGroupCommander("torso")

	print " Waist "
	print " Reference frame: %s" % torso.get_planning_frame()
	print " Reference frame: %s" % torso.get_current_joint_values()
	print ""

	# Waist Initial Pose
	print "go initialize"
	torso.set_joint_value_target([0.0])
	torso.go()
	torso_initial_joint = torso.get_current_joint_values()
	print " Printing Head initial joint: "
	print torso_initial_joint
	print ""

	# plan1
	print "go first"
	torso.set_joint_value_target([0.5])
	torso.go()
	rospy.sleep(3)
	print ""

	# plan1
	print "go first"
	torso.set_joint_value_target([-0.5])
	torso.go()
	rospy.sleep(3)
	print ""

	# Back to the Initial pose ...
	torso.set_joint_value_target(torso_initial_joint)
	torso.go()
	rospy.sleep(2)
	exit(0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
