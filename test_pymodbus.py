#!/usr/bin/python3
import PyQt5
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
from pymodbus.register_read_message import ReadHoldingRegistersResponse
import time
import struct
water_sensor=[203,206,209,212,215,218,221,224,227,230,233]
def dev_info() :

    value =client.read_holding_registers(1,10,unit=0x01)
    print(value.registers)

def call_data(_no) :
    idx=0
    value =client.read_holding_registers(_no,2,unit=0x01)
    
    val = struct.unpack('f', struct.pack('HH', value.registers[idx], value.registers[idx+1]))[0]

    
    print(f'{val:.2f}')
    

    
client=ModbusClient('rtu',port='/dev/ttyUSB0',stopbits=1,bytesize=8,parity='N',baudrate=9600,timeout=5)
connection = client.connect()

print(connection)
 


while True : 
    for i in water_sensor : 
       call_data(i)
       time.sleep(0.5)


