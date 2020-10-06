import os
from utils.logger import LOG_FORMAT
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load_tmp_data, load
from tasks.clean import clean
from db.db_connector import DBConnector

def main():
    start_year = int(os.environ['START_YEAR'])
    end_year = int(os.environ['END_YEAR'])
    start_qtr = int(os.environ['START_QTR'])

    # Initialize db connection
    DBConnector()
    
    for year in range(start_year, end_year + 1):
        for q in range(start_qtr, 5):
            extract(year, q)
            transform(year, q)
            load_tmp_data(year, q)

        load()
        clean(year)

    # Terminate db connection
    DBConnector.disconnect()

if __name__ == '__main__':
    main()

