from datetime import datetime

FIELD_FORMATS = {
    'non_empty_str': '.+',
    'adsh': '^[aA-zZ0-9]{10}-[aA-zZ0-9]{2}-[aA-zZ0-9]{6}$', # nnnnnnnnn-nn-nnnnnn
    'cik': '\d{1,10}',
    'name': '.{1,150}',
    'countryba': '[aA-zZ0-9]{1,2}',
    'cityba': '.{1,30}',
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
    'tag': '.{1,256}',
    'version': '.{1,20}',
    'custom': '[0-1]{1}',
    'abstract': '[0-1]{1}',
    'iord': '.{1}',
    'ddate': '[0-9]{2,4}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', # yyyymmdd
    'qtrs': '[0-9]{1,8}',
    'uom': '.{1,20}',
    'value': '^[0-9]{0,28}(\.[0-9]{1,4})?$', # DECIMAL(28,4)
    'footnote': '.{0,512}',
    'coreg': '\d{0,256}'
}

TIME_FORMATS = {
    'date': '%Y%m%d',
    'datetime': '%Y-%m-%d %H:%M:%S.%f'
}

# When we get empty strings, prefer to treat them as null values instead of storing empty
# strings.
def string_or_none(value):
    if not value:
        return None
    else:
        return value

def float_or_none(value):
    if not value:
        return None
    else:
        return float(value)

def int_or_none(value):
    if not value:
        return None
    else:
        return int(value)
    
def convert_to_date(value):
    return datetime.strptime(value, TIME_FORMATS['date'])

def convert_to_date_or_none(value):
    if not value:
        return None
    else:
        return datetime.strptime(value, TIME_FORMATS['date'])

def convert_to_datetime_or_none(value):
    return datetime.strptime(value, TIME_FORMATS['datetime'])

def convert_to_datetime(value):
    if not value:
        return None
    else:
        return datetime.strptime(value, TIME_FORMATS['datetime'])

def convert_to_bool(value):
    return value == '1'

