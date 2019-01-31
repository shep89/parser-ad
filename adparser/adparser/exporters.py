from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter


class TsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = '\t'

        super(TsvItemExporter, self).__init__(*args, **kwargs)
