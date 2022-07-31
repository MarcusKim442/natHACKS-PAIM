import time
import keyboard


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


if __name__ == '__main__':
    data = []
    file = open("eeg_boiler.csv", "r")
    recent_lines = get_file_recent_lines(file)
    for line in recent_lines:
        # Uncomment for print debug
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
