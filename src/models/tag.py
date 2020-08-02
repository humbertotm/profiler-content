import attr

@attr.s
class Tag(object):
    tag = attr.ib(validator=[])
    version = attr.ib(validator=[])
    custom = attr.ib(validator=[])
    abstract = attr.ib(validator=[])
    datatype = attr.ib(validator=[])
    iord = attr.ib(validator=[])
    crdr = attr.ib(validator=[])
    tlabel = attr.ib(validator=[])
    doc = attr.ib(validator=[])

