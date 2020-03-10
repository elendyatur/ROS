#!/usr/bin/env python
# license removed for brevity
# importar librerias (rospy)
import rospy
import time

from std_msgs.msg import Float64				#  elimina o anade el tipo de mensaje 

def talker():		# definir funciones
    pub = rospy.Publisher('move_Servo', Float64, queue_size=10)	# nombre del topic
								# queue_size: limita la cantidad de mensajes si algun suscriptor no recibe suficientemente rapido
    rospy.init_node('servo_talker', anonymous=True)		# nombre del nodo
    rate = rospy.Rate(5) 					# realiza el bucle a 10Hz

    while not rospy.is_shutdown():
        rospy.loginfo("2.5")
        pub.publish(2.5)
	time.sleep(5)

        rospy.loginfo("6")
        pub.publish(6)
	time.sleep(5)

        rospy.loginfo("10.5")
        pub.publish(10.5)
	time.sleep(5)

        rospy.loginfo("10.5")
        pub.publish(10.5)
	time.sleep(0.5)

        rospy.loginfo("6")
        pub.publish(6)
	time.sleep(5)

        rospy.loginfo("2.5")
        pub.publish(2.5)
	time.sleep(5)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
