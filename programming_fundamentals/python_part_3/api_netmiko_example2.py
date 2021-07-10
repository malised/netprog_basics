#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Marnie Vodounou

api_netmiko_example.py
Illustrate the following concepts:
- Making CLI calls using netmiko library
- Intended to be entered into an interactive
  interpreter

Note: This code is based on Hank's code but used the latest IOS sandbox because
the one in the original code was timing out during my test
"""

from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
          "host": "sandbox-iosxe-latest-1.cisco.com",
          "port": 22,
          "user": "developer",
          "pass": "C1sco12345"}

net_connect = ConnectHandler(ip=router["host"],
                             port=router["port"],
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show run int Gig1")

# Error while using pprint
print(interface_cli)
