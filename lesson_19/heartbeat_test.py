from datetime import datetime
import logging

logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)


def check_heartbeat(file_name):
    filtered_log = []

    with open(file_name, "r") as file:
        for line in file:
            if "Key TSTFEED0300|7E3E|0400" in line:
                filtered_log.append(line)

    for i in range(len(filtered_log) - 1):

        current_line = filtered_log[i]
        next_line = filtered_log[i + 1]

        current_position = current_line.find("Timestamp ")
        next_position = next_line.find("Timestamp ")

        current_time = current_line[current_position + 10:current_position + 18]
        next_time = next_line[next_position + 10:next_position + 18]

        current_time = datetime.strptime(current_time, "%H:%M:%S")
        next_time = datetime.strptime(next_time, "%H:%M:%S")

        heartbeat = (current_time - next_time).seconds

        if heartbeat > 31 and heartbeat < 33:
            logging.warning(
                f"Heartbeat {heartbeat} seconds at {current_time.strftime('%H:%M:%S')}"
            )

        elif heartbeat >= 33:
            logging.error(
                f"Heartbeat {heartbeat} seconds at {current_time.strftime('%H:%M:%S')}"
            )


check_heartbeat("hblog.txt")