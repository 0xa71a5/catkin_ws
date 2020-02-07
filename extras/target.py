#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
    loop = 0
    ret = False
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()


    while True:
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.header.frame_id = "map"

        if loop % 2 == 1:
            goal.target_pose.pose.position.x = 6.5
            goal.target_pose.pose.position.y = 5.0
            goal.target_pose.pose.orientation.w = 1.0
        else:
            goal.target_pose.pose.position.x = 1.3
            goal.target_pose.pose.position.y = 1.3
            goal.target_pose.pose.orientation.w = 1.0
        loop += 1
        rospy.logerr("Send goal! target is ({:<.1f},{:<.1f})".format(goal.target_pose.pose.position.x, goal.target_pose.pose.position.y))
        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return ret
        else:
            rospy.logerr("Send goal success!")
            ret = client.get_result()


if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
