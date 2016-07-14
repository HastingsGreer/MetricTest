cmake_minimum_required(VERSION 2.8)

project(Main)

# Find ITK.
find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

add_executable(Main main.cxx )

target_link_libraries(Main ${ITK_LIBRARIES})
