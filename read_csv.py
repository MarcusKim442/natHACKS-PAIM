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

# -------------------------------------------------------------------------------------

        # HOW TO READ THE DATA (the muse 2 output)
        # data = [[1,2,3,4], #0
        #         [1,2,3,4]] #1
        #         #0,1,2,3

        # Example: checks to see if the most recent entry of the muse 2 data
        # is above 50 for each of the four streams
        if data[len(data)-1][0] > 50 and data[len(data)-1][1] > 50 and \
                data[len(data)-1][2] > 50 and data[len(data)-1][3] > 50:
            pass

