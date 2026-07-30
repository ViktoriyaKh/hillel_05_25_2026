import csv

def read_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    return rows

file1 = read_csv("random.csv")
file2 = read_csv("random-michaels.csv")

header = file1[0]

rows = file1[1:] + file2[1:]

unique_rows = []
seen = set()

for row in rows:
    if len(row) > len(header):
        row = row[:len(header)]

    key = tuple(row)

    if key not in seen:
        seen.add(key)
        unique_rows.append(row)

with open(
        "result_Khromenko.csv",
        "w",
        newline="",
        encoding="utf-8"
) as file:

    writer = csv.writer(
        file,
        quoting=csv.QUOTE_MINIMAL
    )

    writer.writerow(header)
    writer.writerows(unique_rows)
