import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
 
class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')

    self.subscription = self.create_subscription(
      Image, 
      '/video_frames', 
      self.listener_callback, 
      10)
    self.subscription
      
    self.br = CvBridge()
   

  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.br.imgmsg_to_cv2(data)

    ################# color detection ############################
    
    lower = np.array([170, 70, 50], dtype = "uint8")
    upper = np.array([180, 255, 255], dtype = "uint8")

    hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower, upper)

    #cv2.imshow("camera", mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    with_contours = cv2.drawContours(current_frame, contours, -1,(0,255,0),3)

    cv2.imshow('Detected contours', with_contours)

    ###############################################################
    
    #cv2.imshow("camera", current_frame)

    cv2.waitKey(1)
  

def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  
  rclpy.spin(image_subscriber)

  image_subscriber.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()