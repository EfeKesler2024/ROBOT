    def image_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0,0,200), (180,30,255)) # Beyaz için HSV aralığı
        moments = cv2.moments(mask)
        twist = Twist()
        if moments['m00'] > 0:
            cx = int(moments['m10']/moments['m00'])
            width = img.shape[1]
            error = cx - width // 2
            if abs(error) < 30:
                twist.linear.x = 0.2
                twist.angular.z = 0.0
            else:
                twist.linear.x = 0.0
                twist.angular.z = -0.002 * error
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = BallChaser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
