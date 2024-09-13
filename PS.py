
import serial
import time
ser = serial.Serial('COM4',115200,timeout=1)
time.sleep(2)
def send_fen(fen_string):
    ser.write(fen_string.encode('utf-8'))
    ser.write(b'\n')
    time.sleep(1)
response = ser.readline().decode('utf-8').strip()
if response:
    print("respuesta del ESP32",response)

fen_example = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
send_fen(fen_example)
ser.close()