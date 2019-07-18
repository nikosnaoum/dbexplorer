import datetime
from django.utils import timezone
from haystack import indexes
from haystack.fields import CharField

from .models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True, use_template=True,
        template_name='/home/ubuntu/Documents/django-haystack-elasticsearch-master/templates/search/indexes/product_text.txt')
    title = indexes.EdgeNgramField(model_attr='title')
    description = indexes.EdgeNgramField(model_attr="description", null=True)
    price = indexes.EdgeNgramField(model_attr="price", null=True)
    year = indexes.EdgeNgramField(model_attr="year", null=True)
    carmodel = indexes.EdgeNgramField(model_attr="carmodel", null=True)
    distance = indexes.EdgeNgramField(model_attr="distance", null=True)
    power = indexes.EdgeNgramField(model_attr="power", null=True)

    category = indexes.CharField(model_attr='category', faceted=True)

    fuelType = indexes.CharField(model_attr='fuelType', null=True, faceted=True)

    brand = indexes.CharField(model_attr='brand', faceted=True)

    gearBox = indexes.CharField(model_attr='gearBox', null=True, faceted=True)

    repairedDamage = indexes.CharField(model_attr='repairedDamage', null=True, faceted=True)

    # for auto complete
    content_auto = indexes.EdgeNgramField(model_attr='title')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(timestamp__lte=timezone.now())
