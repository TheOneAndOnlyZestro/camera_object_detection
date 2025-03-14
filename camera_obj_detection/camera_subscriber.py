import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
class CameraObjDetection(Node):
    def __init__(self):
        super().__init__('camera_obj_detection')
        self.subscriber_ = self.create_subscription(
        Image,
        "/camera/camera/color/image_raw",
        self.test_callback,
        10)
        self.bridge = CvBridge()
    def test_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # You can display the image or just print some basic information
        cv2.imshow("RealSense Camera Image", cv_image)
        cv2.waitKey(1)  # Refresh window every 1 ms


#Apply in main function

def main(args=None):
    rclpy.init(args=args)
    cod = CameraObjDetection()

    rclpy.spin(cod)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
