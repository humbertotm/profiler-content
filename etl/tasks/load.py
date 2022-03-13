import os, yaml, logging
from etl.utils.logger import LOG_FORMAT
from etl.db.db_connector import DBConnector

DATA_DIR = os.getcwd() + "/tmp"
DATA_OF_INTEREST = ("sub", "tag", "num")
TABLE_MAPPINGS = {
    "tmp": {"sub": "submissions_tmp", "tag": "tags_tmp", "num": "numbers_tmp"},
    "final": {"sub": "submissions", "tag": "tags", "num": "numbers"},
}
SUBMISSIONS_COPY_QUERY = (
    "INSERT INTO submissions SELECT * FROM submissions_tmp ON CONFLICT DO NOTHING"
)
TAGS_COPY_QUERY = "INSERT INTO tags SELECT * FROM tags_tmp ON CONFLICT DO NOTHING"
NUMBERS_COPY_QUERY = "INSERT INTO numbers SELECT * FROM numbers_tmp ON CONFLICT DO NOTHING"
COPY_QUERIES = {
    "sub": SUBMISSIONS_COPY_QUERY,
    "tag": TAGS_COPY_QUERY,
    "num": NUMBERS_COPY_QUERY,
}

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)


def load():
    db_conn = DBConnector()

    # Order is important since numbers table has a dependecny on submissions and tags.
    for data_type in DATA_OF_INTEREST:
        tmp_table = TABLE_MAPPINGS["tmp"][data_type]
        final_table = TABLE_MAPPINGS["final"][data_type]
        logging.info(
            f"Copying from temp table {tmp_table} to final table {final_table}"
        )
        copy_from_tmp_query = COPY_QUERIES[data_type]

        cur = db_conn.cursor()
        cur.execute(copy_from_tmp_query)
        db_conn.commit()
        cur.close()


# This task will load the previously created data csv into tmp tables.
# Afterwards, data will be copied from tmp tables into final ones.
def load_tmp_data(year, period):
    src_path = os.path.join(DATA_DIR, str(year), f"q{period}")

    # TODO: return if file does not exist
    db_conn = DBConnector()

    for filename in os.listdir(src_path):
        data_type, file_type = filename.split(".")

        if data_type in DATA_OF_INTEREST and file_type == "csv":
            tmp_table = TABLE_MAPPINGS["tmp"][data_type]
            src_csv_file_path = os.path.join(
                DATA_DIR, str(year), f"q{period}", filename
            )
            load_from_csv_query = (
                f"COPY {tmp_table} FROM STDIN DELIMITER ',' CSV HEADER"
            )

            logging.debug(f"Load cmd: {load_from_csv_query}")

            cur = db_conn.cursor()
            with open(src_csv_file_path, "r") as f:
                cur.copy_expert(sql=load_from_csv_query, file=f)
                db_conn.commit()
                cur.close()
