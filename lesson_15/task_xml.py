import xml.etree.ElementTree as ET
import logging


logging.basicConfig(
    filename="xml_Khromenko.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_incoming_by_group_number(filename, group_number):
    tree = ET.parse(filename)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = find_incoming_by_group_number("groups.xml", 2)

logging.info(f"Group number 2 incoming value: {result}")

print(result)