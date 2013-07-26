from record.models import Record
from haystack import indexes


class RecordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)

    def get_model(self):
        return Record

    def prepare(self, object):
        self.prepared_data = super(RecordIndex, self).prepare(object)
        self.prepared_data.update(object.all_metadata())
        return self.prepared_data
