if [ "$1"x == "rviz"x ]; then
    roslaunch robot_navigation robot_slam_laser.launch simulation:=true open_rviz:=true
else
    roslaunch robot_navigation robot_slam_laser.launch simulation:=true open_rviz:=false
fi
