#!/usr/bin/env python

import rospy
import actionlib
from nav_msgs.msg import Odometry
from actions_quiz.action import OrientationAction, OrientationResult, OrientationFeedback

class OrientationServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer("my_action_server", OrientationAction, self.execute, False)
        self.pose_subscriber = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        self.current_orientation_z = 0.0
        self.server.start()
    
    def odom_callback(self, msg):
        self.current_orientation_z = msg.pose.pose.orientation.z
    
    def execute(self, goal):
        rate = rospy.Rate(1) 
        orientations = []
        feedback = OrientationFeedback()
        result = OrientationResult()
        
        for i in range(0, goal.duration):
            if self.server.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                self.server.set_preempted()
                break

            feedback.distance = self.current_orientation_z 
            self.server.publish_feedback(feedback)
            orientations.append(self.current_orientation_z)
            rate.sleep()

        result.success = orientations
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('orientation_server_node')
    server = OrientationServer()
    rospy.spin()
