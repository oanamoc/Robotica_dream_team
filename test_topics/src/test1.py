#! /usr/bin/python3

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    while msg.ranges[0] > 1:
        print ("\nMerg spre perete!!!") 
        print (msg.ranges[0])
        turn.linear.x = 0.1
        pub.publish(turn) 
        time.sleep(0.1)
    while msg.ranges[0] < 0.6:
        print ("\nMerg la spate!!!")
        print (msg.ranges[0])
        turn.linear.x = -0.1
        time.sleep(0.1)                  	
    print ("\nMa invart!!!") 
    print (msg.ranges[0])
    turn.linear.x = 0
    turn.angular.z = -1
    pub.publish(turn) 
    time.sleep(2)
    print ("\nMerg la fata!!!")
    print (msg.ranges[0])
    turn.angular.z = 0
    turn.linear.x = 0.1
    pub.publish(turn) 
    time.sleep(2)
    print ("\nMerg la spate!!!")
    print (msg.ranges[0])
    turn.linear.x = -1
    time.sleep(10)
                        
turn = Twist()
turn.linear.x = 0

rospy.init_node('test_topics')         
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)          	
sub = rospy.Subscriber('/scan', LaserScan, callback)   	                                                 			
                                                      			
rospy.spin()                                          			