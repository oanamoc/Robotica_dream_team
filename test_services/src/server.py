#! /usr/bin/python3
import rospy
from test_services.srv import srvmess, srvmessResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    turn = Twist()
    
    i = 0
    r = rospy.Rate(1)
    start_time = rospy.get_time()
    while start_time + request.duration > rospy.get_time():
        print('still running after ' + str(i) + ' seconds')
        if request.direction == "poz":
            turn.linear.y = 0.5
            print("+")
        elif request.direction == "neg":
            turn.linear.y = -0.5
            print("-")
        else: print("problem")
        pub.publish(turn)
        i = i + 1
        r.sleep()

    turn.linear.y = 0.0
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