#########################################################################
# File Name: make_and_simulate_navigation.sh
# Author: Xingcheng Liu
# Email:  anrist@vip.qq.com
# Created Time: Sun 02 Feb 2020 02:18:54 PM CST
#########################################################################
#!/bin/bash
source ~/.bashrc
source devel/setup.bash
catkin_make -j4 && ./launch_navigation_simulate.sh
