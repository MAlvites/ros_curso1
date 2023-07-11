#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Int32 

def callback(msg):
	rospy.loginfo("Result is %s", str(msg.data))

def show_result():
	rospy.init_node('show_result')
	rospy.Subscriber("result_number", Int32, callback)
	rospy.spin()
if __name__ == '__main__':
	show_result()	
