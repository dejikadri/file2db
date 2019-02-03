import argparse
import csv


def process_args():
    parser = argparse.ArgumentParser("A script that loads a csv file into a Sqlite database")
    # parser.add_argument("--days", type=int, help="The number of days to check for duplicates", default=12)

    parser.add_argument("file", type=str, help="The path to the file to load e.g data/file.csv")

    args = parser.parse_args()
    return args.file

# get the headers(first row) of the file
def get_header_row(file_path):
    try:
        with open(file_path, newline='') as fl:
          reader = csv.reader(fl)
          row_header = next(reader)

        return row_header
    except IOError:
        return "Error Unable to read file:", file_path