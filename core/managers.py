from django.db import models
from django.db.models import Sum


class SiteManager(models.Manager):
    def get_sum_grouped(self):
        result = self.annotate(a_value_sum=Sum('sitedetail__a_value'))\
                        .annotate(b_value_sum=Sum('sitedetail__b_value'))
        return result

    def get_average_grouped(self):
        query = self.raw("""
                SELECT s.id, s.name, AVG(p.a_value) as a_value_avg,
                AVG(p.b_value) as b_value_avg
                FROM core_sitedetail p, core_site s
                WHERE p.site_id = s.id
                GROUP BY s.id
                ORDER BY s.id""")
        return query
