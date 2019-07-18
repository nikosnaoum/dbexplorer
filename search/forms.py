from haystack.forms import FacetedSearchForm


class FacetedProductSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.categories = data.get('category', [])
        self.brands = data.get('brand', [])
        self.fuelTypes = data.get('fuelType', [])
        self.gearBoxs = data.get('gearBox', [])
	self.repairedDamages = data.get('repairedDamage', [])
        super(FacetedProductSearchForm, self).__init__(*args, **kwargs)

    def search(self):
        sqs = super(FacetedProductSearchForm, self).search()
        if self.categories:
            query = None
            for category in self.categories:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(category)
            sqs = sqs.narrow(u'category_exact:%s' % query)
        if self.brands:
            query = None
            for brand in self.brands:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(brand)
            sqs = sqs.narrow(u'brand_exact:%s' % query)

	if self.fuelTypes:
            query = None
            for fuelType in self.fuelTypes:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(fuelType)
            sqs = sqs.narrow(u'fuelType_exact:%s' % query)

	if self.gearBoxs:
            query = None
            for gearBox in self.gearBoxs:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(gearBox)
            sqs = sqs.narrow(u'gearBox_exact:%s' % query)

	if self.repairedDamages:
            query = None
            for repairedDamage in self.repairedDamages:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(repairedDamage)
            sqs = sqs.narrow(u'repairedDamage_exact:%s' % query)

        return sqs
