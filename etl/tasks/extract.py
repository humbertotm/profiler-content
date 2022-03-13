# Std lib
import zipfile, os, io, sys, logging

# deps
import requests

# Private deps
from etl.utils.logger import LOG_FORMAT

DEST_DIR = os.getcwd() + "/tmp"
SRC_URL = "https://www.sec.gov/files/dera/data/financial-statement-data-sets"
MAX_RETRIES = 5

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)


def extract(year, period, periodicity):
    logging.info(f"Attempting download for year {year}, period {period}, {periodicity}")

    retries = 0
    filename = f"{year}q{period}.zip"
    dest_path = os.path.join(DEST_DIR, str(year), f"q{period}", filename)
    src_url = os.path.join(SRC_URL, filename)

    res = requests.get(src_url)

    while not res.ok:
        if retries < MAX_RETRIES:
            logging.warning("Attempt failed for %s. Retrying.", filename)
            retries += 1
            res = requests.get(src_url)
        else:
            logging.critical(
                "MAX_RETRIES reached while attempting to fetch %s", src_url
            )
            # TODO: return instead of aborting the program execution
            sys.exit()

    logging.info("Successfully downloaded %s", filename)
    logging.info("Writing contents to %s", dest_path)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as f:
        f.write(res.content)
