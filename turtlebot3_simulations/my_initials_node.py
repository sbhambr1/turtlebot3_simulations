#!usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

from math import radians

import sys

def my_initials():

	rospy.init_node('my_initials', anonymous = True)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(5)

	move_cmd = Twist()
	move_cmd.linear.x = 0.5

	turn_left_cmd = Twist()
	turn_left_cmd.linear.x = 0
	turn_left_cmd.angular.z = radians(45)

	turn_right_cmd = Twist()
	turn_right_cmd.linear.x = 0
	turn_right_cmd.angular.z = -radians(45)

	make_semi_cmd = Twist()
	make_semi_cmd.linear.x = 0.5
	make_semi_cmd.angular.z = radians(90)

	while not rospy.is_shutdown():

		rospy.loginfo('Starting trajectory')

		rospy.loginfo('Going straight')	

		for _ in range(20):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Turning')	

		for _ in range(10):
			pub.publish(turn_right_cmd)
			rate.sleep()

		rospy.loginfo('Going straight')	

		for _ in range(10):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Turning')	

		for _ in range(10):
			pub.publish(turn_right_cmd)
			rate.sleep()

		rospy.loginfo('Going straight')	

		for _ in range(20):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Turning')	

		for _ in range(10):
			pub.publish(turn_right_cmd)
			rate.sleep()

		rospy.loginfo('Going straight')	

		for _ in range(10):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Turning')	

		for _ in range(10):
			pub.publish(turn_right_cmd)
			rate.sleep()

		rospy.loginfo('Going straight')	

		for _ in range(10):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Turning')	

		for _ in range(10):
			pub.publish(turn_right_cmd)
			rate.sleep()

		rospy.loginfo('Going straight')	

		for _ in range(10):
			pub.publish(move_cmd)
			rate.sleep()

		rospy.loginfo('Ending trajectory')


if __name__ == "__main__":
	try:
		my_initials()
	except rospy.ROSInterruptException:
		pass
