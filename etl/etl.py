import argparse, os
from .tasks.extract import extract
from .tasks.transform import transform
from .tasks.load import load_tmp_data, load
from .tasks.clean import clean
from .db.db_connector import DBConnector


def generate_periods_sequence(start_year, start_period, end_year, end_period):
    """
    This generates a list of sequences to iterate through as data is processed.
    Input: start_year: 2020, start_period: 3,  end_year: 2020, end_period: 12
    Output: [(2020, 3, 'QUARTER'), (2020, 10, 'MONTH'), (2020, 11, 'MONTH'), (2020, 12, 'MONTH')]
    TODO: handle errors. Assumes the input is valid.
    """
    periods = []

    first_loop = True
    last_loop = False
    for year in range(start_year, end_year + 1):
        if year == end_year:
            last_loop = True

        start_period = start_period if first_loop else 1
        stop = 5 if not last_loop else end_period + 1
        for qtr in range(start_period, stop):
            first_loop = False if first_loop else False
            periods.append((year, qtr, "QUARTER"))

    return periods


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-sy", "--start_year", type=int, required=True)
    parser.add_argument("-ey", "--end_year", type=int, required=True)
    parser.add_argument("-sp", "--start_period", type=int, required=True)
    parser.add_argument("-ep", "--end_period", type=int, required=True)
    args = parser.parse_args()

    periods = generate_periods_sequence(
        args.start_year, args.start_period, args.end_year, args.end_period
    )

    # Initialize db connection
    DBConnector()

    for period in periods:
        year, period, periodicity = period

        extract(year, period, periodicity)
        transform(year, period, periodicity)
        load_tmp_data(year, period)
        load()
        clean(year, period)

    # Terminate db connection
    DBConnector.disconnect()
