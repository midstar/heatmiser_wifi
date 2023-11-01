This repository is forked from the original (https://github.com/midstar/heatmiser_wifi) and updated for my personal requirements only. Feel free to use it as is or clone and take over the responsibility for public maintenance.

# Heatmiser WiFi - python library and tool
[![AppVeyor](https://ci.appveyor.com/api/projects/status/github/midstar/heatmiser_wifi?svg=true)](https://ci.appveyor.com/api/projects/status/github/midstar/heatmiser_wifi)

## Overview
A [Heatmiser](http://www.heatmiser.com/) WiFi Thermostat communication tool and library for python.

Supported Heatmiser Thermostats are DT, DT-E, PRT and PRT-E.

This fork adds support for the PRT-HW WiFi thermostat, and adds the following functionality (for PRT-HW, maybe others):
* Setting timers for heating (should work for all models)
* Setting timers for hot water (for PRT-HW)
* Setting clock on thermostat with option offset (should work for all models)
* Note I only have a PRT-HW so can only test functionality on that model

The main class of the library is Heatmiser. It supports retrieval of all Thermostat parameters as a dictionary. It also supports setting of most (but not all) of the Thermostat parameters. 

## Supported platforms
The application is written in Python and has been successfully tested with Python version 2.7 and 3.4.

Both Windows and Linux has been tested successfully. Mac OS X has not been tested, but should work as well.

## Installation
Run 

    python -m pip install git+https://github.com/iainbullock/heatmiser_wifi

This will install both the library and the command line tool.

Alternatively, since this is just one python file, you can download heatmiser_wifi.py and include it in your project.
  
### Using libary

See how the library/class is used in the main() function of heatmiser_wifi.py.

### Using command line tool

To list all parameters write:

    heatmiser_wifi -c <pincode> <themostat_ip_address> -l 

It is also possible to read and write specific parameters. For instructions, write:

    heatmiser_wifi -h

When setting triggers for heating / hot water use comma separated values for the trigger parameters
For heating triggers: Time1Hour,Time1Minute,Time1Temp,Time2Hour,Time2Minute,Time2Temp,Time3Hour,Time3Minute,Time3Temp,Time4Hour,Time4Minute,Time4Temp
For hot water triggers: Time1OnHour,Time1OnMinute,Time1OffHour,Time1OffMinute,Time2OnHour,Time2OnMinute,Time2OffHour,Time2OffMinute,Time3OnHour,Time3OnMinute,Time3OffHour,Time3OffMinute,Time4OnHour,Time4OnMinute,Time4OffHour,Time4OffMinute
Note the thermostat only allows minutes to be either 0 or 30
For example:
    
    heatmiser_wifi -c <pincode> <themostat_ip_address> -w mon_triggers 7,30,20,9,0,5,16,0,22,22,0,5
    heatmiser_wifi -c <pincode> <themostat_ip_address> -w tue_hw_triggers 7,30,8,0,9,0,9,30,13,30,14,30,22,0,23,0

When setting date / time, the parameter is an offset which added to the system date before sending to the themrostat. I use this to partuially get round the limitation on trigger minute only being 0 or 30
For example, this will set the thermostat clock to be 15 mins ahead of the system time:

    heatmiser_wifi -c <pincode> <themostat_ip_address> -w date_time 15

### Author and license
This application is written by Joel Midstjärna and is licensed under the MIT License. This fork is updated by Iain Bullock and licensed under the MIT License.
