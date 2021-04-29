# Pursuit-Evasion Game using Turtlebot3 in ROS
Simulating TurtleBot3 in custom worlds &amp; playing the evader-pursuer game.

This project was divided into two parts:
1. We build a custom Gazebo world environment and make the Turtlebot3 robot (Waffle_Pi) traverse through the scene.
2. We create maps of two Gazebo worlds using SLAM and deploy an object detection based node for the Turtlebot3 robot to be able to follow the evader.

## Part 1

#### Task 1: Building a custom Gazebo world

##### Description: 
The custom world environment was built using Gazebo, a software primarily used for performing robotic simulation experiments by running algorithms on a simulated robot in a custom environment and obtaining the required observations. For this specific project, the ultimate goal is to be able to simulate a pursuit evasion game in a custom world environment. As a first step, we designed a custom floor plan in the Gazebo environment using the Building Editor. This allowed us to design the outline of the sample one floor house with a living room, a kitchen, a store room and two bedrooms. All the spaces are well connected to each other and have doors leading the robot inside each of the rooms.

#### Task 2 Traversing the custom Gazebo world using the Turtlebot3 robot

##### Description: 
As the second step, we operated a Turtlebot3 robot in the custom world. This allowed us to understand the motion of the robot in the custom designed environment. The custom world is launched using a launch file and the robot is simulated using a python script where the constructed ROS node published to the node ‘cmd_vel’.
