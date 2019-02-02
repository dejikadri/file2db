import argparse


def process_args():
    parser = argparse.ArgumentParser("A script that loads a csv file into a Sqlite database")
    # parser.add_argument("--days", type=int, help="The number of days to check for duplicates", default=12)

    parser.add_argument("file", type=str, help="The path to the file to load e.g data/file.csv")

    args = parser.parse_args()
    return args.file