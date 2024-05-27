#!/usr/bin/env python

import rospy
import actionlib
from actions_quiz.action import OrientationAction, OrientationGoal

def feedback_callback(feedback):
    rospy.loginfo('Received feedback: %d' % feedback.distance)

def client():
    rospy.init_node('client_node')
    client = actionlib.SimpleActionClient('my_action_server', OrientationAction)
    client.wait_for_server()
    
    goal = OrientationGoal(duration=10)
    client.send_goal(goal, feedback_cb=feedback_callback)

if __name__ == '__main__':
    try:
        client()
    except rospy.ROSInterruptException:
        pass
