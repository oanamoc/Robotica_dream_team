#! /usr/bin/env python
import rospy

import actionlib

from test_actions.msg import actiuneAction, actiuneGoal

def feedback_cb(feedback):
    rospy.loginfo('Received feedback: %d' % feedback.nr_curent)

rospy.init_node('number_sequence_client')
client = actionlib.SimpleActionClient('number_sequence', actiuneAction)
client.wait_for_server()
    
goal = actiuneGoal(nr_sec=5)
client.send_goal(goal, feedback_cb=feedback_cb)
    
client.wait_for_result()
result = client.get_result()
#rospy.loginfo('Result: %s' % str(result.num_publicate))
print('Result: %s' % str(result.num_publicate))