#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Marnie Vodounou

api_requests_example2.py
Illustrate the following concepts:
- Making REST API calls using requests library
- Intended to be entered into an interactive
  interpreter

Note: This code is based on Hank's code but used the latest IOS sandbox because
the one in the original code was timing out during my test
"""


import requests
from pprint import pprint
router2 = {"ip": "sandbox-iosxe-latest-1.cisco.com",
	      "port": "443",
          "user": "developer",
          "pass": "C1sco12345"}

headers = {"Accept": "application/yang-data+json"}

# For all interfaces
# u0 = "https://{}:{}/restconf/data/ietf-interfaces:interfaces

u = "https://{}:{}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

u = u.format(router["ip"], router["port"])

r = requests.get(u,
		     headers = headers,
		     auth=(router2["user"], router2["pass"]),
		     verify=False)

pprint(r.text)

api_data = r.json()
interface_name = api_data["ietf-interfaces:interface"]["name"]
interface_name
