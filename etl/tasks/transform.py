# Std lib
import os, io, zipfile, csv, logging

# deps
import attr

# Private deps
from etl.models.submission import Submission, SUBMISSION_FIELDS
from etl.models.tag import Tag, TAG_FIELDS
from etl.models.number import Number, NUMBER_FIELDS
from etl.utils.logger import LOG_FORMAT

DATA_DIR = os.getcwd() + "/tmp"
DATA_OF_INTEREST = ("sub", "tag", "num")
INSTANTIATORS = {"sub": Submission, "tag": Tag, "num": Number}
FIELDS = {"sub": SUBMISSION_FIELDS, "tag": TAG_FIELDS, "num": NUMBER_FIELDS}

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

# For this step, the following is done:
# 1. Extract contents of all zipfiles.
# 2. Extract contents and validate them before writing them to an output tsv file.
def transform(year, period, periodicity):
    zipfile_name = f"{year}q{period}.zip"

    src_zip_path = os.path.join(DATA_DIR, str(year), f"q{period}", zipfile_name)
    dest_path = os.path.join(DATA_DIR, str(year), f"q{period}")

    # TODO: add a check to see if zipfile exists beforehand. Return otherwise.
    logging.info("Extracting %s", src_zip_path)
    with zipfile.ZipFile(src_zip_path, "r") as zf:
        zf.extractall(dest_path)

        src_path = os.path.join(DATA_DIR, str(year), f"q{period}")

    for filename in os.listdir(src_path):
        faulty_lines_count = 0
        total_lines_count = 0
        data_type = filename.split(".")[0]

        if data_type in DATA_OF_INTEREST:
            output_csv_path = os.path.join(src_path, f"{data_type}.csv")

            with open(output_csv_path, "w+") as output_csv:
                fieldnames = FIELDS[data_type]
                writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                src_file = os.path.join(src_path, filename)

                writer.writeheader()

                logging.info("Validating contents in %s", src_file)
                with open(
                    os.path.join(src_path, filename), newline="", encoding="iso-8859-1"
                ) as src_tsv:
                    reader = csv.DictReader(
                        src_tsv, delimiter="\t", quoting=csv.QUOTE_NONE
                    )
                    for row in reader:
                        [s.encode("utf-8") for s in row]
                        try:
                            total_lines_count += 1
                            data_obj = INSTANTIATORS[data_type](**row)
                            writer.writerow(attr.asdict(data_obj))
                        except ValueError:
                            if data_type == DATA_OF_INTEREST[0]:
                                logging.error(f"fault row form type: {row['form']}")
                            faulty_lines_count += 1
                            next

            fault_pct = faulty_line_pct(faulty_lines_count, total_lines_count)
            logging.warning(
                f"{faulty_lines_count} faulty {data_type} records ({fault_pct}%) for {year} period {period}, {periodicity}"
            )


def faulty_line_pct(faulty_lines, total_lines):
    if total_lines == 0:
        return 0
    else:
        return round((faulty_lines / total_lines) * 100, 2)
