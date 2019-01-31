from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

class TsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = '\t'

        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export

        super(TsvItemExporter, self).__init__(*args, **kwargs)
