#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Shuta Tsukui
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msgs.msg import Person


class SeasonalFishListener(Node):
    def __init__(self):
        super().__init__('seasonal_fish_listener')
        self.subscription = self.create_subscription(
            Person,
            'person',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Received fish info: {msg.name} (Month: {msg.age})')

def main(args=None):
    rclpy.init(args=args)
    seasonal_fish_listener = SeasonalFishListener()
    rclpy.spin(seasonal_fish_listener)
    seasonal_fish_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
