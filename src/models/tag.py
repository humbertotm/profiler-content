import attr
import models.validators as v

TAG_FIELDS = (
    'tag',
    'version',
    'custom',
    'abstract',
    'datatype',
    'iord',
    'crdr',
    'tlabel',
    'doc'
)

@attr.s
class Tag(object):
    tag = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    version = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    custom = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.instance_of(bool)
    )
    abstract = attr.ib(
        converter=v.convert_to_bool,
        validator=attr.validators.instance_of(bool)
    )
    datatype = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    iord = attr.ib(validator=attr.validators.matches_re(v.FIELD_FORMATS['non_empty_str']))
    crdr = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    tlabel = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    doc = attr.ib(
        converter=v.string_or_none,
        validator=attr.validators.optional(attr.validators.instance_of(str))
    )

