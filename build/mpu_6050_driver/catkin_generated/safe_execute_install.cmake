execute_process(COMMAND "/home/pnt/catkin_pratik_ws/build/mpu_6050_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/pnt/catkin_pratik_ws/build/mpu_6050_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
