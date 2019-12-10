import argparse
import logging
import configparser

from app.actors.extract.theguardian_extract import Extract
from app.actors.load.csv_loader import Load
from app.actors.transform.theguardian_transformer import Transform

config = configparser.ConfigParser()
config.read("config.ini")

SECTION = config["DEFAULT"]["SECTION"]
API_KEY = config["DEFAULT"]["API_KEY"]
PAGE_SIZE = config["DEFAULT"]["PAGE_SIZE"]
URI = config["DEFAULT"]["URI"]
OUTPUT_DIR = config["DEFAULT"]["OUTPUT_DIR"]

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s: %(levelname)s: %(message)s")


def main():
    logging.debug("main() - Initializing ETL process")
    parser = argparse.ArgumentParser(
        description="Extract technology section data from The Guardian website and parse to csv file")

    parser.add_argument("--from-date", required=True, help="date start format YYYY-MM-DD", dest="from_date")
    parser.add_argument("--to-date", required=True, help="date end format YYYY-MM-DD", dest="to_date")

    args = parser.parse_args()
    logging.info("main() - Getting data from {uri} from {from_date} to {to_date}"
                 .format(uri="https://content.guardianapis.com/search", from_date=args.from_date,
                         to_date=args.to_date))
    payload = {
        "section": SECTION,
        "from-date": args.from_date,
        "to-date": args.to_date,
        "api-key": API_KEY,
        "page-size": PAGE_SIZE
    }

    try:
        pages = Extract.run(URI, payload)
        transformed_rows = Transform.run(pages)
        Load.run(transformed_rows, OUTPUT_DIR)
    except Exception:
        logging.error("main() - Something went wrong!")

    logging.info("main() - Finished!")


if __name__ == '__main__':
    main()
