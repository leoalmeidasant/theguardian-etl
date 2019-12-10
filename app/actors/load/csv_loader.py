import csv
import sys
import logging
from datetime import datetime


class Load(object):

    @staticmethod
    def run(row_list, output_dir):
        logging.info("Load.run() - Creating csv file")
        csv_file = "{output}/theguardian-technology-{timestamp}.csv" \
            .format(timestamp=int(datetime.now().timestamp()), output=output_dir)
        csv_columns = row_list[0].keys()

        try:
            with open(csv_file, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                for row in row_list:
                    logging.info("Load.run() - Writing rows to csv file")
                    writer.writerow(row)
                logging.info("Load.run() - Complete writing with successful")
        except IOError as strerror:
            sys.exit(1)
            print("I/O error(): {0}".format(strerror))
