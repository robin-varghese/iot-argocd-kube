#port
#baudrate
#bytesize
#timeout
#stopbits
import time
import serial
import keyboard

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, bytesize=8, timeout=1,
                    stopbits=serial.STOPBITS_ONE)

while True:
    # ser.write("This is the message".encode('Ascii'))
    ser.write("This is the message\r\n".encode('Ascii'))
    # receive = ser.read()
    receive = ser.readline()
    print(receive.decode('Ascii'))
    #TODO: Add the function to send the message (JSON packet) to queue
    time.sleep(0)
    if keyboard.is_pressed('q'):
        print("User need to Quit the application")
        break

ser.close()


