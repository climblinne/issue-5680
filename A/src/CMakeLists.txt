set(CMAKE_CXX_COMPILER_WORKS 1)
cmake_minimum_required(VERSION 2.8.12)
project(Hello CXX)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

add_executable(app main.cpp hello.cpp)
target_link_libraries(app ${CONAN_LIBS})
