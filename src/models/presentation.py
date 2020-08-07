import attr

PRESENTATION_FIELDS = (
    'adsh',
    'report',
    'line',
    'stmt',
    'inpth',
    'rfile',
    'tag',
    'version',
    'plabel',
    'negating'
)

@attr.s
class Presentation(object):
    adsh = attr.ib(validator=[])
    report = attr.ib(validator=[])
    line = attr.ib(validator=[])
    stmt = attr.ib(validator=[])
    inpth = attr.ib(validator=[])
    rfile = attr.ib(validator=[])
    tag = attr.ib(validator=[])
    version = attr.ib(validator=[])
    plabel = attr.ib(validator=[])

