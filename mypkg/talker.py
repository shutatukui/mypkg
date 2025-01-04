import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
from datetime import datetime


rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)


def get_current_month():
    return datetime.now().month

def get_seasonal_fish(month):
    fish_info = {
            1: {"name": "ブリ", "season": "冬"},
            2: {"name": "フグ", "season": "冬"},
            3: {"name": "サワラ", "season": "春"},
            4: {"name": "シラウオ", "season": "春"},
            5: {"name": "カツオ", "season": "春"},
            6: {"name": "アジ", "season": "夏"},
            7: {"name": "アユ", "season": "夏"},
            8: {"name": "ウナギ", "season": "夏"},
            9: {"name": "サンマ", "season": "秋"},
            10: {"name": "サケ", "season": "秋"},
            11: {"name": "タラ", "season": "秋"},
            12: {"name": "マダイ", "season": "冬"}
        }
    return fish_info.get(month, {"name": "不明", "season": "不明"})

def cb():
    current_month = get_current_month()
    fish_info = get_seasonal_fish(current_month)

    msg = Person()
    msg.name = fish_info["name"]
    msg.age = current_month
    pub.publish(msg)


def main():
    node.create_timer(1.0, cb) 
    rclpy.spin(node)


if __name__ == '__main__':
    main()
