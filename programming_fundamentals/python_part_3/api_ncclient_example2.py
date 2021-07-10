#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Marnie Vodounou

api_ncclient_example.py
Illustrate the following concepts:
- Making NETCONF calls using ncclient library
- Intended to be entered into an interactive
  interpreter

Note: This code is based on Hank's code but used the latest IOS sandbox because
the one in the original code was timing out during my test
"""

from ncclient import manager
from pprint import pprint
import xmltodict

router = {"ip": "sandbox-iosxe-latest-1.cisco.com",
          "port": 830,
          "user": "developer",
          "pass": "C1sco12345"}

# This original filter does NOT work with this sandbox
"""
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""
"""

# This new filter I created does NOT work either :(
netconf_filter2 = """
<filter>
  <data>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet1</name>
        </interface>
      </interfaces>
    </native>
  </data>
</filter>
"""


m = manager.connect(host=router["ip"],
                    port=router["port"],
                    username=router["user"],
                    password=router["pass"],
                    hostkey_verify=False)

# Applying the original filter or my 2nd one does NOT work.
# So I am gettin the full running config without filtering
#
#interface_netconf = m.get_config("running", netconf_filter)

interface_netconf = m.get_config("running")
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python["interfaces"][0]["interface"][0]["name"])#["#text"])
print("\n")
pprint(interface_python["interfaces"][0]["interface"][0]["name"]['ipv4']['address']['ip'])
