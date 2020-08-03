import attr
from datetime import datetime
from src.models.validators import FIELD_FORMATS, convert_to_date, convert_to_datetime, convert_to_bool

@attr.s
class Number(object):
    adsh = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['adsh']))
    tag = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['tag']))
    version = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['version']))
    coreg = attr.ib(validator=attr.validators.optional(attr.validators.matches_re(FIELD_FORMATS['coreg'])))
    ddate = attr.ib(
        validator=attr.validators.instance_of(datetime),
        converter=convert_to_date
    )
    qtrs = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['qtrs']))
    uom = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['uom']))
    value = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        converter=float
    )
    footnote = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

