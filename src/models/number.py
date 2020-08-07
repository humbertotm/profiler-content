import attr
from datetime import datetime
import models.validators as v

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
    adsh = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['adsh']))
    tag = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['tag']))
    version = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['version']))
    coreg = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.matches_re(v.FIELD_FORMATS['coreg']))
    )
    ddate = attr.ib(
        converter=v.convert_to_date,
        validator=attr.validators.instance_of(datetime)
    )
    qtrs = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['qtrs']))
    uom = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['uom']))
    value = attr.ib(
        converter=v.float_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(float))
    )
    footnote = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )

