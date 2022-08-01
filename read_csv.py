import time
import keyboard
import time
from ppadb.client import Client as AdbClient


def accept_call(device_):
    # Send the "accept call signal to the connected device
    device_.shell('input keyevent 5')


def get_file_recent_lines(file_):
    # Continuously read the lines
    file_.seek(0, 2)
    while True:
        line = file_.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def format_csv_line(line_):
    # Format numbers from csv (scientific notation) to floats
    numbers = line_.split(',')
    for i in range(len(numbers)):
        numbers[i] = float(numbers[i])
    return numbers


def connect():
    # Entirety of this function provided by https://gist.github.com/1Blademaster/8aae153f2702fb090a1876d94ca8693f
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client


if __name__ == '__main__':
    # Initialize EEG data array
    data = []
    # Initialize connection to phone
    device, client = connect()
    # Connection to csv file
    file = open("eeg_boiler.csv", "r")
    recent_lines = get_file_recent_lines(file)
    # Repeat for every new row in the csv file
    blinked_last = False
    blinked_timeout_max = 40
    blinked_timeout = 0
    for line in recent_lines:
        # Uncomment for print debug:
        # print(line)
        # if keyboard.is_pressed('q'):
        #     for row in data:
        #         print(row)
        #     exit()

        # Put to an array
        row_data = []
        for number in format_csv_line(line):
            row_data.append(number)
        data.append(row_data)
        # HOW TO READ THE DATA (the muse 2 output)
        # data = [[1,2,3,4], #0
        #         [1,2,3,4]] #1
        #         #0,1,2,3

# -------------------------------------------------------------------------------------

        # Primative blink detection use
        blinked_timeout = max(blinked_timeout-1, 0)
        if (800 > data[len(data) - 1][0] and data[len(data) - 1][0] < -900) \
            and (800 > data[len(data) - 1][1] and data[len(data) - 1][0] < -800):
            if not blinked_last and blinked_timeout <= 0:
                # Send call signal
                accept_call(device)
                print("worked")
                blinked_timeout = blinked_timeout_max
            blinked_last = True
        else:
            blinked_last = False


