#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Int32MultiArray 

def random_numbers():
	num_pub = rospy.Publisher('rand_numbers', Int32MultiArray, queue_size=10)
	rospy.init_node('random_numbers')
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		a=random.randint(0,9)
		b=random.randint(0,9)
		c=random.randint(0,9)
		msg=Int32MultiArray()
		msg.data=[a,b,c]
		num_pub.publish(msg)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		random_numbers()
	except rospy.ROSInterruptException:
		pass
