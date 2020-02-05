if [ $# -eq 0 ]; then
    roslaunch robot_navigation robot_navigation.launch simulation:=true open_rviz:=true
else
    roslaunch robot_navigation robot_navigation.launch simulation:=true open_rviz:=false
fi
