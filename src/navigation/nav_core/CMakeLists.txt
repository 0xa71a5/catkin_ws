cmake_minimum_required(VERSION 2.8.3)
project(nav_core)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED
        COMPONENTS
            std_msgs
            geometry_msgs
            tf
            costmap_2d
        )

catkin_package(
    INCLUDE_DIRS
        include
    CATKIN_DEPENDS
            std_msgs
            geometry_msgs
            tf
            costmap_2d
)


## Install project namespaced headers
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE)
