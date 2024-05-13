#! /usr/bin/env python
import rospy

import actionlib

from nav_msgs.msg import Odometry

from test_actions.msg import actiuneAction, actiuneFeedback, actiuneResult

class NumberSequenceServer:
  def __init__(self):
    self._as = actionlib.SimpleActionServer("number_sequence", actiuneAction, self.execute, False)
    self._odom_sub = rospy.Subscriber("/odom", Odometry, self.odom_callback)
    self.current_orientation_z = 0.0
    self._as.start()

  def odom_callback(self, data):
    self.current_orientation_z = data.pose.pose.orientation.z

  def execute(self, goal):
    r = rospy.Rate(1)
    # create messages that are used to publish feedback/result
    feedback = actiuneFeedback()
    result   = actiuneResult()

    for i in range(0, goal.nr_sec):
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        self._as.set_preempted()
        break
          
      feedback.nr_curent = self.current_orientation_z
      self._as.publish_feedback(feedback)
      result.num_publicate.append(feedback)
      rospy.loginfo('Publishing /odom pose.pose.orientation.z: %f' % self.current_orientation_z)
      r.sleep()  

    self._as.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('number_sequence_server')
    server = NumberSequenceServer()
    rospy.spin()