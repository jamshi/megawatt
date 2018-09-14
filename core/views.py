from django.shortcuts import render
from .models import Site, SiteDetail
# Create your views here.

def home(request):
    sites = Site.objects.all()
    return render(request, 'sites.html', {'sites': sites})


def site_details(request, id):
    site = Site.objects.get(pk=id)
    site_details = SiteDetail.objects.filter(site=site).order_by('date')
    return render(request, 'site-detail.html', {'site_details': site_details,
                                 'site_name': site.name})


def site_summary_sum(request):
    site_summary = Site.objects.get_sum_grouped()
    return render(request, 'site-summary-sum.html', {'site_summary': site_summary})

def site_summary_average(request):
    site_summary = Site.objects.get_average_grouped()
    return render(request, 'site-summary-avg.html', {'site_summary': site_summary})
