'''
Experiment name: Serial port communication
Version: v1.0
Date: 2021.1
Author: 01Studio
Description： Serial port communication is achieved through programming, with the computer serial port assistant to achieve data sending and receiving.
'''

#importing serial modules
from machine import UART

uart=UART(1,115200) #set serial port number 3 and baud rate,TX--Y9,RX--Y10

uart.write('Hello 01Studio!')#send a data

while True:

    #determining whether a message has been received
    if uart.any():

        text=uart.read(128) #receive 128 characters
        print(text) #printing data received by serial port 3 via REPL
