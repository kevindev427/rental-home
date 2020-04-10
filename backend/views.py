from django.shortcuts import render
from django.views.generic import ListView

from apps.stays.models import Stay


class ExploreView(ListView):
    """Several Lists of Stay Views"""
    queryset = Stay.objects.all()
    template_name = 'explore.html'

    def get_context_data(self, *args, **kwargs):
        """Method for getting context data"""
        context = super().get_context_data(**kwargs)
        qs = Stay.objects.all()
        context['sf_stays_list'] = qs.filter(city="San Francisco")[:4]
        context['featured_stays_list'] = qs.filter(featured=True)[:4]
        return context


def landing_page(request):
    return render(request, 'landing.html')


class StayCityListView(ListView):
    """Stay for each City List View"""
    queryset = Stay.objects.all()
    template_name = 'city.html'

    def get_context_data(self, *args, **kwargs):
        """Method for getting context data"""
        context = super().get_context_data(**kwargs)
        city = self.kwargs['city']
        context['stays_list'] = Stay.objects.all().filter(city=city)
        context['city'] = city
        return context