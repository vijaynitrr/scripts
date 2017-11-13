import sys
import os
import subprocess

prefix_command = "sudo service"
commands_list = [" redis_6379 "," redis-sentinel "," rabbitmq-server "," teamviewerd "," apache2 "," mysql ", " supervisor ", " mongodb ", " aerospike "]
action = "stop"

for curCommand in commands_list:
    service_command = prefix_command + curCommand + action
    returnCode = subprocess.call(service_command,shell=True)
    if returnCode == 0 :
        print curCommand.lstrip() + "is Sucessfully Stopped"
    else:
        print curCommand.lstrip() + "is not Sucessfully Stopped"
