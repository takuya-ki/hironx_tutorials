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

	print " Robot Groups:"
	print robot.get_group_names()
	print ""

	print " Printing robot state"
	print robot.get_current_state()
	print ""

	head = moveit_commander.MoveGroupCommander("head")

	print " Head "
	print " Reference frame: %s" % head.get_planning_frame()
	print " Reference frame: %s" % head.get_end_effector_link()
	print ""

	#Head Initial Pose
	print "go initialize"
	head.set_joint_value_target([0.0, 0.0])
	head.go()
	head_initial_joint = head.get_current_joint_values()
	print " Printing Head initial joint: "
	print head_initial_joint
	print ""

	# plan1
	print "go first"

	head.set_joint_value_target([0.0, 0.5])
	head.go()
	rospy.sleep(3)
	print ""
#
	#plan2
	# print "go second"
	# head.set_joint_value_target([0.5, -0.3])
	# head.go()
	# rospy.sleep(3)
	# print ""
#
	#plan3
	# print "go third"
	# head.set_joint_value_target([-0.5, -0.3])
	# head.go()
	# rospy.sleep(3)
	# print ""
#
	#plan4
	# print "go fourth"
	# head.set_joint_value_target([-0.5, 0.5])
	# head.go()
	# rospy.sleep(3)
	# print ""
#
	#Back to the Initial pose ...
	# head.set_joint_value_target(head_initial_joint)
	# head.go()
	# rospy.sleep(2)
	# exit(0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
