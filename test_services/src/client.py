#! /usr/bin/python3
import rospy
# Import the service message used by the service /trajectory_by_name
from test_services.srv import srvmess, srvmessRequest 

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /move_in_square to be running
rospy.wait_for_service('/move_linear_y')
# Create the connection to the service
move_linear = rospy.ServiceProxy('/move_linear_y', srvmess)
# Create an object of type MoveInSquareRequest
move_linear_obj = srvmessRequest()
move_linear_obj.duration = 5
move_linear_obj.direction = "neg"

# Send through the connection the name of the request
result = move_linear(move_linear_obj)
# Print the result given by the service called
print(result)