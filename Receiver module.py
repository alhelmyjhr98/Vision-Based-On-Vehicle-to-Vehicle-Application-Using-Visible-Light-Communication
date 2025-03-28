from machine import Pin, I2C
import time

# I2C Setup (Adjust SDA, SCL for your board)
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

# Receiver Pin (Adjust based on hardware setup)
receiver = Pin(15, Pin.IN)  # GPIO15 as input

# Variables
data_bits = []
displayCount = 0

def decode(dataList):
    """Decodes received bits into warning signals"""
    if dataList == [1, 0, 1, 0]:  
        print("⚠️ WARNING! Object Too Close!")
    else:
        print("✅ No Warning - Normal Distance")

while True:
    data_bits = []  # Reset buffer
    
    # Wait for signal start
    while receiver.value() == 0:
        pass
    
    # Read 4-bit sequence
    for _ in range(4):
        data_bits.append(receiver.value())
        time.sleep(0.1)  # Adjust timing if needed
    
    # Decode signal
    decode(data_bits)
    
    time.sleep(1)  # Delay before next read
