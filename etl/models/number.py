import attr
from datetime import datetime
from . import validators as v

NUMBER_FIELDS = (
    'adsh',
    'tag',
    'version',
    'coreg',
    'ddate',
    'qtrs',
    'uom',
    'value',
    'footnote'
)

@attr.s
class Number(object):
    adsh = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    tag = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    version = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    coreg = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    ddate = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.instance_of(datetime)
    )
    qtrs = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    uom = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    value = attr.ib(
        converter=v.float_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(float))
    )
    footnote = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
