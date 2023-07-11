#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Int32MultiArray 

isdDefined=False
a=0
b=0
c=0

def callback(msg):
	global a,b,c
	a = msg.data[0]
	b = msg.data[1]
	c = msg.data[2]

def result():
	res = rospy.Publisher('result_number', Int32, queue_size=10)
	rospy.init_node('result')
	rand_sub =rospy.Subscriber('rand_numbers',Int32MultiArray,callback)
	rate = rospy.Rate(10)			
	while not rospy.is_shutdown():
		result=Int32()
		d=a+b-c
		result.data=d
		res.publish(result)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		result()
	except rospy.ROSInterruptException:
		pass
