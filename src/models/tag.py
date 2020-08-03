import attr
from src.models.validators import FIELD_FORMATS, convert_to_bool

@attr.s
class Tag(object):
    tag = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['tag']))
    version = attr.ib(validator=attr.validators.matches_re(FIELD_FORMATS['version']))
    custom = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=convert_to_bool
    )
    abstract = attr.ib(
        validator=attr.validators.instance_of(bool),
        converter=convert_to_bool
    )
    datatype = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    iord = attr.ib(validator=attr.validators.matches_re('iord'))
    crdr = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    tlabel = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    doc = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

