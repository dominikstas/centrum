cmake_minimum_required(VERSION 3.10)
project(Centrum C)

set(CMAKE_C_STANDARD 17)

add_executable(Centrum main.c simple.c)

target_compile_options(Centrum PRIVATE -Wall -Wextra)