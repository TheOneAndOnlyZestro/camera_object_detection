import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
class CameraObjDetection(Node):
    def __init__(self):
        super().__init__('camera_obj_detection')
        self.subscriber_ = self.create_subscription(
        Image,
        "/camera/camera/color/image_raw",
        self.test_callback,
        10)
        self.bridge = CvBridge()
        self.publisher_ = self.create_publisher(Image, "/camera_obj_prediction",10)
        self.model = YOLO("best.pt")
        self.model.fuse()
    def test_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        results = self.model(cv_image)
        
        annotated_image = results[0].plot()  
        output_msg = self.bridge.cv2_to_imgmsg(annotated_image, encoding="bgr8")

        self.publisher_.publish(output_msg)
        
        cv2.imshow("YOLOv8 Object Detection", annotated_image)
        cv2.waitKey(1)


#Apply in main function

def main(args=None):
    rclpy.init(args=args)
    cod = CameraObjDetection()

    rclpy.spin(cod)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
