import os, io, zipfile, attr, csv, logging
from models.submission import Submission, SUBMISSION_FIELDS
from models.tag import Tag, TAG_FIELDS
from models.number import Number, NUMBER_FIELDS
from utils.logger import LOG_FORMAT

DATA_DIR = os.environ['APP_PATH'] + '/tmp'
DATA_OF_INTEREST = ('sub', 'tag', 'num')
INSTANTIATORS = {
    'sub': Submission,
    'tag': Tag,
    'num': Number
}
FIELDS = {
    'sub': SUBMISSION_FIELDS,
    'tag': TAG_FIELDS,
    'num': NUMBER_FIELDS
}

logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

# For this step, the following is done:
# 1. Extract contents of all zipfiles.
# 2. Extract contents and validate them before writing them to an output csv file.
def transform(year, q):
    zipfile_name = str(year) + 'q' + str(q) + '.zip'
    src_zip_path = os.path.join(DATA_DIR, str(year), ('q' + str(q)), zipfile_name)
    dest_path = os.path.join(DATA_DIR, str(year), ('q' + str(q)))

    # TODO: add a check to see if zipfile exists beforehand. Return otherwise.
    
    logging.info('Extracting %s', src_zip_path)
    with zipfile.ZipFile(src_zip_path, 'r') as zf:
        zf.extractall(dest_path)

    src_path = os.path.join(DATA_DIR, str(year), ('q' + str(q)))
    
    for filename in os.listdir(src_path):
        faulty_lines_count = 0
        total_lines_count = 0
        data_type = filename.split('.')[0]

        if data_type in DATA_OF_INTEREST:
            output_csv_path = os.path.join(src_path, (data_type + '.csv'))
                    
            with open(output_csv_path, 'w+') as output_csv:
                fieldnames = FIELDS[data_type]
                writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                src_file = os.path.join(src_path, filename)

                writer.writeheader()
                
                logging.info('Validating contents in %s', src_file)
                with open(os.path.join(src_path, filename), newline='', encoding='iso-8859-1') as src_csv:
                    reader = csv.DictReader(src_csv, delimiter='\t', quoting=csv.QUOTE_NONE)
                    for row in reader:
                        [s.encode('utf-8') for s in row]
                        try:
                            total_lines_count += 1
                            data_obj = INSTANTIATORS[data_type](**row)
                            writer.writerow(attr.asdict(data_obj))
                        except ValueError as e:
                            faulty_lines_count += 1
                            next

        fault_pct = faulty_line_pct(faulty_lines_count, total_lines_count)
        logging.warning(
            '%s faulty %s records (%s %%) for %s q%s',
            str(faulty_lines_count),
            data_type,
            str(fault_pct),
            str(year),
            str(q)
        )
                                    
                    
def faulty_line_pct(faulty_lines, total_lines):
    if total_lines == 0:
        return 0
    else:
        return round((faulty_lines / total_lines) * 100, 2)
                    
