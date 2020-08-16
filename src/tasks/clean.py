import os, logging
from utils.logger import LOG_FORMAT

DATA_DIR = '/tmp/screener-content/tmp'
DATA_OF_INTEREST = ('sub', 'tag', 'num')
TABLE_MAPPINGS = {
    'sub': 'submissions_tmp',
    'tag': 'tags_tmp',
    'num': 'numbers_tmp'
}

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

def clean(year):
    # clean data directory
    data_dir = os.path.join(DATA_DIR, str(year))
    rm_data_dir_cmd = 'rm -r %s' % data_dir
    logging.debug('Cleaning data dir cmd: %s', rm_data_dir_cmd)
    logging.info('Cleaning data dir %s', data_dir)
    os.system(rm_data_dir_cmd)

    # Clear tmp data tables
    for data_type in DATA_OF_INTEREST:
        target_table = TABLE_MAPPINGS[data_type]
        truncate_query = 'TRUNCATE TABLE %s' % target_table
        truncate_cmd = 'sudo -u postgres psql screener_dev -c "%s"' % truncate_query
        logging.debug('Executing truncate cmd: %s', truncate_cmd)
        logging.info('Truncating table %s', target_table)
        os.system(truncate_cmd)
