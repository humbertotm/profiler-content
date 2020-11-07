import os, logging
from utils.logger import LOG_FORMAT
from db.db_connector import DBConnector

DATA_DIR = os.environ['APP_PATH'] + '/tmp'
DATA_OF_INTEREST = ('sub', 'tag', 'num')
TABLE_MAPPINGS = {
    'sub': 'submissions_tmp',
    'tag': 'tags_tmp',
    'num': 'numbers_tmp'
}

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

# TODO: fix bug where data is not cleaned if etl is aborted due to being unable to pull data
# from SEC's servers
def clean(year, q):
    # clean data directory
    qtr_dir_path = 'q' + str(q)
    data_dir = os.path.join(DATA_DIR, str(year), qtr_dir_path)
    rm_data_dir_cmd = 'rm -r %s' % data_dir
    db_conn = DBConnector()
    cur = db_conn.cursor()

    # TODO: exit program execution if dir does not exist. It means no more data is available

    logging.debug('Cleaning data dir cmd: %s', rm_data_dir_cmd)
    logging.info('Cleaning data dir %s', data_dir)
    os.system(rm_data_dir_cmd)

    # Clear tmp data tables
    for data_type in DATA_OF_INTEREST:
        target_table = TABLE_MAPPINGS[data_type]
        truncate_query = 'TRUNCATE TABLE %s' % target_table
        truncate_cmd = 'sudo -u postgres psql screener_dev -c "%s"' % truncate_query

        logging.info('Truncating table %s', target_table)
        cur.execute(truncate_query)
        db_conn.commit()

    cur.close()

