#!/usr/bin/python3

import argparse
from shutil import copy2
import os
from banner import banner
banner()
parser = argparse.ArgumentParser()
parser.add_argument("--shell",help="Enter the shell directory",dest='shell',type=str)
parser.add_argument("--payload",help="Enter the paylaod directory.",dest='payload',type=str)
parser.add_argument("--output",help="Enter the output directory",dest='output',type=str)

args = parser.parse_args()

def payload_readmode(payload_path):
    p= open(payload_path,'r')
    f= p.readlines()
    p.close()
    return f


#making directory where payload are store
try:
    os.mkdir(args.output)
except:
    print('Please Enter a valid output Directory')
try:

    #need payload path from argparse
    payload = payload_readmode(args.payload)     
except:
    print('Please enter the payload dir')
try:
    for i in payload:
        copy2(args.shell,args.output+"shell."+i)
        print ("payload successfully formated to "+i )

except:
    Exception
    




    
