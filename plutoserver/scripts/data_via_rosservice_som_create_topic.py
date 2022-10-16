#!/usr/bin/env python
from plutodrone.srv import *
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from plutoserver.msg import PlutoSensorData 
# from std_msgs.msg import String

class request_data():
	"""docstring for request_data"""
	def __init__(self):
		rospy.init_node('drone_board_data')
		data = rospy.Service('PlutoService', PlutoPilot, self.access_data)
		self.pub = rospy.Publisher('drone_data', PlutoSensorData, queue_size=10) 

	def access_data(self, req):
		 self.pub.publish(req.accX,req.accY,req.accZ, req.gyroX,req.gyroY,req.gyroZ, req.magX,req.magY,req.magZ, req.roll,req.pitch,req.yaw, req.alt,req.battery,req.rssi) 
		 rospy.sleep(.02)
		 return PlutoPilotResponse(rcAUX2 =1500)

test = request_data()
rospy.spin()
