from rclpy.node import Node
import rclpy
class CameraObjDetection(Node):
    def __init__(self):
        super().__init__('camera_obj_detection')
        self.test = self.create_timer(0.5, self.test_callback)

    def test_callback(self):
        self.get_logger().info("This node is working, again!!!!!!!!!!!")


#Apply in main function

def main(args=None):
    rclpy.init(args=args)
    cod = CameraObjDetection()

    rclpy.spin(cod)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
