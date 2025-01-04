import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
import requests

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)



def get_snow_info():
    response = requests.get('https://www.sekisetsu.net/narashinoshi/')
    snow_info = response.json()
    return snow_info['current_snow_depth']
except requests.exceptions.RequestException as e:
    node.get_logger().error(f"エラー: {e}")
    return '情報を取得できませんでした'

def cb():
    msg = Person()
    msg.snow_depth = get_snow_info()
    pub.publish(msg)

def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
