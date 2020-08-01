import requests, zipfile, os, io, sys

DEST_DIR = '/tmp/screener-content/tmp'
SRC_URL = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets'
SRC_URL_2020Q1 = 'https://www.sec.gov/files/node/add/data_distribution'
MAX_RETRIES = 5

def extract():
    start_year = int(os.environ['START_YEAR'])
    end_year = int(os.environ['END_YEAR'])

    for year in range(start_year, end_year + 1):
        for q in range(1, 5):
            print('Attempting download for ' + str(year) + 'q' + str(q))
            retries = 0
            filename = str(year) + 'q' + str(q) + '.zip'
            dest_path = os.path.join(DEST_DIR, str(year), ('q' + str(q)))
            src_url = os.path.join(SRC_URL, filename)
            res = requests.get(src_url)
            
            while not res.ok:
                if retries < MAX_RETRIES:
                    print('Attempt failed for ' + filename + '. Retrying.')
                    retries += 1
                    res = requests.get(src_url)
                else:
                    print('MAX_RETRIES reached while attempting to fetch' + src_url)
                    sys.exit()


            print('Successfully downloaded ' + filename)
            print('Extracting contents to ' + dest_path)
            zip = zipfile.ZipFile(io.BytesIO(res.content))
            zip.extractall(dest_path)

