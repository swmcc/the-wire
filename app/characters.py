import csv
import json
import sys

def parse_csv(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        headers = []
        for row in reader:
            if headers:
                rows.append(dict(zip(headers, row)))
            else:
                headers = row

    print(json.dumps(rows, indent=4))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage %s <filename>" % (sys.argv[0]))
        sys.exit(1)

    parse_csv(sys.argv[1])