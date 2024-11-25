#!/usr/bin/env python3
from pymodbus.client import ModbusSerialClient
import time

#init modbus device
client = ModbusSerialClient(method='rtu', port='/dev/ttyACM0', baudrate=9600)
joni = False

def testBatch():
    getTemp1 = client.read_holding_registers(4, 3, slave = 7)
    getTemp2 = client.read_holding_registers(0, 3, slave = 8)
    getElect = client.read_holding_registers(0, 29, slave = 2)
    getPLC = client.read_holding_registers(54, 5, slave = 1)
    #writePLC = client.write_register(501, 0, slave = 1)
    #writePLC = client.write_register(502, 0, slave = 1)
    #writeRly = client.write_coil(0, False, slave = 3)
    print(getTemp1.registers)
    print(getTemp2.registers)
    print(getElect.registers)
    print(getPLC.registers)
    print(writePLC)
    #print(writeRly)
    print("~~~")

#Loop
if joni:
    while True:
        testBatch()
        time.sleep(2)
        
else:   
    testBatch()
