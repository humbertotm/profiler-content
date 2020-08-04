import os, io, zipfile, csv

DATA_DIR = '/tmp/screener-content/tmp'

def transform():
    start_year = int(os.environ['START_YEAR'])
    end_year = int(os.environ['END_YEAR'])

    # The assumption is that zipfiles have been already downloaded
    for year in range(start_year, end_year + 1):
        for q in range(1, 5):
            zipfile_name = str(year) + 'q' + str(q) + '.zip'
            src_zip_path = os.path.join(DATA_DIR, str(year), ('q' + str(q)), zipfile_name)
            dest_path = os.path.join(DATA_DIR, str(year), ('q' + str(q)))

            print('Extracting ' + src_zip_path)
            with zipfile.ZipFile(src_zip_path, 'r') as zf:
                zf.extractall(dest_path)

                # Now we need to cycle through files
                # sub.txt, tag.txt, num.txt
