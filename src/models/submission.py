import attr
from datetime import datetime
from src.models.validators import FIELD_FORMATS, convert_to_date, convert_to_datetime, convert_to_bool

@attr.s
class Submission(object):
    adsh = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['adsh']))
    cik = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['cik']))
    name = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['name']))
    sic = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    countryba = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['countryba']))
    stprba = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    cityba = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['cityba']))
    zipba = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    bas1 = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    bas2 = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    baph = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    countryma = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    stprma = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    cityma = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    zipma = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    mas1 = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    mas2 = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    countryinc = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['countryinc']))
    stprinc = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    ein = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    former = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    changed = attr.ib(
        converter=convert_to_date,
        validator=attr.validators.optional(attr.validators.instance_of(datetime))
    )
    afs = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    wksi = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=convert_to_bool
    )
    fye = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['fye']))
    form = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['form']))
    period = attr.ib(
        validator=attr.validators.instance_of(datetime),
        converter=convert_to_date
    )
    fy = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['fy']))
    fp = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['fp']))
    filed = attr.ib(
        validator=attr.validators.instance_of(datetime),
        converter=convert_to_date
    )
    accepted = attr.ib(validator=attr.validators.instance_of(datetime),
                       converter=convert_to_datetime
    )
    prevrpt = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=convert_to_bool
    )
    detail = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=convert_to_bool
    )
    instance = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['instance']))
    nciks = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['nciks']))
    aciks = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

