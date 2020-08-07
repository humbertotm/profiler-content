import attr
from datetime import datetime
import models.validators as v

SUBMISSION_FIELDS = (
    'adsh',
    'cik',
    'name',
    'sic',
    'countryba',
    'stprba',
    'cityba',
    'zipba',
    'bas1',
    'bas2',
    'baph',
    'countryma',
    'stprma',
    'cityma',
    'zipma',
    'mas1',
    'mas2',
    'countryinc',
    'stprinc',
    'ein',
    'former',
    'changed',
    'afs',
    'wksi',
    'fye',
    'form',
    'period',
    'fy',
    'fp',
    'filed',
    'accepted',
    'prevrpt',
    'detail',
    'instance',
    'nciks',
    'aciks'
)

@attr.s
class Submission(object):
    adsh = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['adsh']))
    cik = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['cik']))
    name = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['name']))
    sic = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    countryba = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['countryba']))
    stprba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    cityba = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['cityba']))
    zipba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    bas1 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    bas2 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    baph = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    countryma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    stprma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    cityma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    zipma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    mas1 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    mas2 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    countryinc = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['countryinc']))
    stprinc = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    ein = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    former = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    changed = attr.ib(
        converter=v.convert_to_date_or_none, # TODO: problematic if it is an empty string
        validator=attr.validators.optional(attr.validators.instance_of(datetime))
    )
    afs = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    wksi = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.instance_of(bool)
    )
    fye = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['fye']))
    form = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['form']))
    period = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.instance_of(datetime)
    )
    fy = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['fy']))
    fp = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['fp']))
    filed = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.instance_of(datetime)
    )
    accepted = attr.ib(
        converter=v.convert_to_datetime,
        validator=attr.validators.instance_of(datetime)
    )
    prevrpt = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=v.convert_to_bool
    )
    detail = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.instance_of(bool)
    )
    instance = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['instance']))
    nciks = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['nciks']))
    aciks = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )

