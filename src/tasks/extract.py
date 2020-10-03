import requests, zipfile, os, io, sys, logging
from utils.logger import LOG_FORMAT

DEST_DIR = os.environ['APP_PATH'] + '/tmp'
SRC_URL = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets'
SRC_URL_2020Q1 = 'https://www.sec.gov/files/node/add/data_distribution'
MAX_RETRIES = 5

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

def extract(year, q):
    logging.info('Attempting download for %sq%s', str(year), str(q))
    retries = 0
    filename = str(year) + 'q' + str(q) + '.zip'
    dest_path = os.path.join(DEST_DIR, str(year), ('q' + str(q)), filename)
    if year == 2020 and q == 1:
        src_url = os.path.join(SRC_URL_2020Q1, filename)
    else:
        src_url = os.path.join(SRC_URL, filename)
        
    
    res = requests.get(src_url)

    while not res.ok:
        if retries < MAX_RETRIES:
            logging.warning('Attempt failed for %s. Retrying.', filename)
            retries += 1
            res = requests.get(src_url)
        else:
            logging.critical('MAX_RETRIES reached while attempting to fetch %s', src_url)
            sys.exit()


    logging.info('Successfully downloaded %s', filename)
    logging.info('Writing contents to %s', dest_path)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'wb') as f:
        f.write(res.content)

