import argparse
import csv
import logging
import sqlite3
import db_helper as dbh
import sys


logging.basicConfig(filename='log/app.log', format='%(asctime)s - %(message)s', level=logging.INFO)


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
    except IOError as e:
        logging.error(e)
        return "Error Unable to read file:", file_path

def create_table():
    pass


def load_file_to_table(file_path, table_name=None):
    """

    :param file_path:
    :param table_name:
    :return:
    """
    try:
        # conn = dbh.connect_db()
        # dbh.close_db_con(conn)
        with open(file_path, newline='') as fl:
          reader = csv.reader(fl, escapechar="'",  quotechar='"', delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=True)

          # skip the header row
          next(reader)
          conn = dbh.connect_db()
          cur = conn.cursor()
          records_inserted = 0

          for row in reader:
              id = int(row[0]) # convert id datatype to integer
              year = int(row[1]) # convert year datatype to integer
              age = int(row[2]) # convert age datatype to integer
              name = row[3]
              movie = row[4]

              print(id, year, age, name, movie, f"INSERT INTO stars VALUES ({id}, {year}, {age}, '{name}', '{movie}')")

              if cur.execute(f"INSERT INTO stars VALUES ({id}, {year}, {age}, '{name}', '{movie}')"):
                  conn.commit()
                  records_inserted += 1


          rows_inserted = cur.execute(f"select count(*) from stars;")
          rows_inserted.fetchone()[0]

        dbh.close_db_con(conn)



    except IOError as e:
        logging.error(e)
        return "Error Unable to read file:", file_path
