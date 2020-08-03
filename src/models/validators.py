from datetime import datetime

FIELD_FORMATS = {
    'adsh': '^[aA-zZ0-9]{10}-[aA-zZ0-9]{2}-[aA-zZ0-9]{6}$', # nnnnnnnnn-nn-nnnnnn
    'cik': '\d{1,10}',
    'name': '.{1,150}',
    'countryba': '[aA-zZ0-9]{1,2}',
    'cityba': '[aA-zZ0-9]{1,30}',
    'countryinc': '[aA-zZ0-9]{1,3}',
    'wksi': '[0-1]{1}',
    'fye': '[aA-zZ0-9]{4}',
    'form': '.{1,10}',
    'period': '[0-9]{2,4}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', # yyyymmdd. validate by coercio
    'fy': '[0-9]{4}',
    'fp': '[aA-zZ0-9]{2}',
    'filed': '[0-9]{2,4}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', # yyyymmdd. validate by coercion
    'accepted': '[0-9]{4}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1} [0-2]{1}[0-9]{1}:[0-6]{1}[0-9]{1}:[0-6]{1}[0-9]{1}', # yyyy-mm-dd hh:mm:ss. validate by coercion
    'prevrpt': '[0-1]{1}',
    'detail': '[0-1]{1}',
    'instance': '.{1,32}',
    'nciks': '[0-9]{1,4}',
    'tag': '\w{1,256}',
    'version': '.{1,20}',
    'custom': '[0-1]{1}',
    'abstract': '[0-1]{1}',
    'iord': '\w{1}',
    'ddate': '[0-9]{2,4}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', # yyyymmdd
    'qtrs': '[0-9]{1,8}',
    'uom': '.{1,20}',
    'value': '^[0-9]{0,28}(\.[0-9]{1,4})?$', # DECIMAL(28,4)
    'footnote': '.{0,512}'
}

TIME_FORMATS = {
    'date': '%Y%m%d',
    'datetime': '%Y-%m-%d %H:%M:%S.%f'
}

def convert_to_date(value):
    return datetime.strptime(value, TIME_FORMATS['date'])

def convert_to_datetime(value):
    return datetime.strptime(value, TIME_FORMATS['datetime'])

def convert_to_bool(value):
    return value == '1'

