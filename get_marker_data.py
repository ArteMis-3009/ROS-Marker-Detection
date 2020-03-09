#!/usr/bin/env python

from __future__ import print_function

import rospy
import roslib
import tf

from geometry_msgs.msg import PoseArray
#


# Defining a class
class Marker_detect():

    def __init__(self):
        # initializing a ros node with name marker_detection
        rospy.init_node('marker_detection', anonymous=False)

        self.whycon_marker = {}  # Declaring dictionaries
        #

        rospy.Subscriber(
            '/whycon/poses',
            PoseArray,
            self.whycon_data)  # Subscribing to topic

    # Callback for /whycon/poses

    def whycon_data(self, msg):
        for index, marker in enumerate(msg.poses):
            self.whycon_marker[index] = [
                marker.position.x,
                marker.position.y,
                marker.position.z]

        
        print(self.whycon_marker)
        


if __name__ == "__main__":

    marker = Marker_detect()

    while not rospy.is_shutdown():
		rospy.spin()
