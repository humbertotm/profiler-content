import attr
from datetime import datetime
from . import validators as v

SUBMISSION_FIELDS = (
    "adsh",
    "cik",
    "name",
    "sic",
    "countryba",
    "stprba",
    "cityba",
    "zipba",
    "bas1",
    "bas2",
    "baph",
    "countryma",
    "stprma",
    "cityma",
    "zipma",
    "mas1",
    "mas2",
    "countryinc",
    "stprinc",
    "ein",
    "former",
    "changed",
    "afs",
    "wksi",
    "fye",
    "form",
    "period",
    "fy",
    "fp",
    "filed",
    "accepted",
    "prevrpt",
    "detail",
    "instance",
    "nciks",
    "aciks",
    "pubfloatusd",
    "floatdate",
    "floataxis",
    "floatmems",
)


@attr.s
class Submission(object):
    adsh = attr.ib(
        validator=attr.validators.matches_re(v.FIELD_FORMATS["non_empty_str"])
    )
    cik = attr.ib(
        validator=attr.validators.matches_re(v.FIELD_FORMATS["non_empty_str"])
    )
    name = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    sic = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    countryba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    stprba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    cityba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    zipba = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    bas1 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    bas2 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    baph = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    countryma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    stprma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    cityma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    zipma = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    mas1 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    mas2 = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    countryinc = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    stprinc = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    ein = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    former = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    changed = attr.ib(
        converter=v.convert_to_date_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(datetime)),
    )
    afs = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    wksi = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
    )
    fye = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    form = attr.ib(
        validator=attr.validators.matches_re(v.FIELD_FORMATS["non_empty_str"])
    )
    period = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.optional(attr.validators.instance_of(datetime)),
    )
    fy = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS["non_empty_str"]))
    fp = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS["non_empty_str"]))
    filed = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.optional(attr.validators.instance_of(datetime)),
    )
    accepted = attr.ib(
        converter=v.convert_to_datetime,
        validator=attr.validators.optional(attr.validators.instance_of(datetime)),
    )
    prevrpt = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        converter=v.convert_to_bool,
    )
    detail = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
    )
    instance = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    nciks = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    aciks = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    pubfloatusd = attr.ib(
        converter=v.float_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    floatdate = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    floataxis = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    floatmems = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
