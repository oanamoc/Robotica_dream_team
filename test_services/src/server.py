#! /usr/bin/python3
import rospy
from test_services.srv import srvmess, srvmessResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    start_time = rospy.Time.now()
    turn = Twist()
    #rate = rospy.Rate(10)  # 10 Hz

    while (rospy.Time.now().to_sec() - start_time.to_sec() < request.duration):
        if request.direction == "poz":
            turn.linear.y = 0.1
        elif request.direction == "neg":
            turn.linear.y = -0.1
        pub.publish(turn)
        #print('*')
        #rate.sleep()

    turn.linear.x = 0.0
    turn.angular.z = 0.0
    pub.publish(turn)

    response = srvmessResponse()
    response.success = True
    return response

rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

my_service = rospy.Service('/move_linear_y', srvmess , my_callback)
rospy.spin()


#linear
#y
#server si client #serviciul primeste un string care specifica poz sau neg
#si o durata
#se va misca timp de ac durata in dir resp
#returneaza bool