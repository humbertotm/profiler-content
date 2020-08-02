import attr

@attr.s
class Number(object):
    adsh = attr.ib(validator=[])
    tag = attr.ib(validator=[])
    version = attr.ib(validator=[])
    coreg = attr.ib(validator=[])
    ddate = attr.ib(validator=[])
    qtrs = attr.ib(validator=[])
    uom = attr.ib(validator=[])
    value = attr.ib(validator=[])
    footnote = attr.ib(validator=[])

