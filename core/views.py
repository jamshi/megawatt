from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from django.http import HttpResponseNotFound
from .models import Site, SiteDetail
# Create your views here.


class HomePageView(TemplateView):

    template_name = "sites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.all()
        return context


def site_details(request, id):
    try:
        site = Site.objects.get(pk=id)
        site_details = SiteDetail.objects.filter(site=site).order_by('date')
        return render(request, 'site-detail.html', {'site_details': site_details,
                                                    'site_name': site.name})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("404: Site Not Found")


class SumView(TemplateView):

    template_name = "site-summary-sum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_summary'] = Site.objects.get_sum_grouped()
        return context


class AvgView(TemplateView):

    template_name = "site-summary-avg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_summary'] = Site.objects.get_average_grouped()
        return context
