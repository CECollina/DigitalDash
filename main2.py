import serial
import time
import obd

# Configure the serial port for the Longan module
ser = serial.Serial('/dev/ttyAMA0', baudrate=9600)  # Adjust the port as needed

# Initialize the CAN bus interface
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Define OBD-II PIDs
PID_ENGIN_PRM = 0x0C
PID_VEHICLE_SPEED = 0x0D
PID_COOLANT_TEMP = 0x05

# Define CAN ID for PIDs
CAN_ID_PID = 0x7DF  # Adjust this if needed

def send_pid(pid):
    data = [0x02, 0x01, pid, 0, 0, 0, 0, 0]
    msg = can.Message(arbitration_id=CAN_ID_PID, data=data, is_extended_id=False)
    bus.send(msg)

def get_speed():
    send_pid(PID_VEHICLE_SPEED)
    timeout = time.time() + 1  # 1-second timeout

    while time.time() < timeout:
        message = bus.recv()
        if message.arbitration_id == CAN_ID_PID and message.data[1] == 0x41:
            return message.data[3]

    return None

def main():
    try:
        while True:
            speed = get_speed()
            if speed is not None:
                print(f"Vehicle Speed: {speed} km/h")
            else:
                print("Failed to retrieve speed data")
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass

    finally:
        ser.close()
        bus.shutdown()

if __name__ == "__main__":
    main()
