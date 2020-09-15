#!/bin/bash
cd /home/alarm/printerServer/Server
rm media/*
#rm lock
#(python3 led.py) & 
python3 manage.py runserver 0.0.0.0:8001 
