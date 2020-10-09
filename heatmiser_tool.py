#!/usr/bin/env python
# coding=utf-8
#
###############################################################################
#   - heatmiser_tool -
#
#   Copyright 2020 by Joel Midstjärna (joel.midstjarna@gmail.com)
#
#   A Heatmiser WiFi Thermostat communication tool. 
#
#   Supported Heatmiser Thermostats are DT, DT-E, PRT and PRT-E.
#
#   Run 'python heatmiser_tool.py -h' for usage
#
#   All rights reserved.
#   This file is part of the heatmiser_wifi python library and is
#   released under the "MIT License Agreement". Please see the LICENSE
#   file that should have been included as part of this package.
###############################################################################

import sys
from optparse import OptionParser
from collections import OrderedDict
from heatmiser_wifi import Heatmiser
        
def print_dict(dict, level=""):
    for i in dict.items():
        if(isinstance(i[1],OrderedDict)):
            print(level+i[0]+":")
            print_dict(i[1],level + "    ")
        else:
            print(level+str(i[0])+" = "+str(i[1]))
        
def main():
    # This function shows how to use the Heatmiser class. 
    
    parser = OptionParser("Usage: %prog [options] <Heatmiser Thermostat address>")
    parser.add_option("-p", "--port", dest="port", type="int",
                      help="Port of HeatMiser Thermostat (default 8068)", default=8068) 
    parser.add_option("-c", "--pin", dest="pin", type="int",
                      help="Pin code of HeatMiser Thermostat (default 0000)", default=0)
    parser.add_option("-l", "--list", action="store_true", dest="list_all",
                      help="List all parameters in Thermostat", default=False)
    parser.add_option("-r", "--read",  dest="parameter",
                      help="Read one parameter in Thermostat (-r param)", default="")
    parser.add_option("-w", "--write",  dest="param_value", nargs=2,
                      help="Write value to parameter in Thermostat (-w param value)")                       
    (options, args) = parser.parse_args()
    
    if (len(args) != 1):
        parser.error("Wrong number of arguments")
    
    host = args[0]
                      
    # Create a new Heatmiser object
    heatmiser = Heatmiser(host,options.port,options.pin)
    
    # Connect to Thermostat
    heatmiser.connect()
    
    # Read all parameters
    info = heatmiser.get_info()
    
    # Print all parameters in Thermostat
    if(options.list_all):
        print_dict(info)
        
    # Print one parameter in Thermostat
    if(options.parameter != ""):
        if (options.parameter in info):
            print(options.parameter + " = " + str(info[options.parameter]))
        else:
            sys.stderr.write("Error!\n"+
                "Parameter '"+options.parameter+"' does not exist\n")
    
    # Write value to one parameter in Thermostat
    if(options.param_value != None):
        param = options.param_value[0]
        value = options.param_value[1]
        if (param in info):
            try:
                heatmiser.set_value(param,value)
                info2 = heatmiser.get_info()
                print("Before change: " + param + " = " + str(info[param]))
                print("After change:  " + param + " = " + str(info2[param]))
            except Exception as e:
                sys.stderr.write(e.args[0]+"\n")
        else:
            sys.stderr.write("Error!\n"+
                "Parameter '"+param+"' does not exist\n")
    heatmiser.disconnect()
        
if __name__ == '__main__':
    main()
    