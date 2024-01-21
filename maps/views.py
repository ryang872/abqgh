
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models, forms
from django.shortcuts import redirect

class MapHome(LoginRequiredMixin, ListView):
    template_name = "maps.html"
    model = models.AptMap
    context_object_name = 'maps'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.AptMap.objects.filter(complex_name__icontains=query)
        else:
            return models.AptMap.objects.all()

class AddNewMap(LoginRequiredMixin, CreateView):
    template_name = 'addmap.html'
    model = models.AptMap
    form_class = forms.MapForm
    success_url = reverse_lazy('map_list')

class MapDetailView(LoginRequiredMixin, DetailView):
    model = models.AptMap
    template_name = 'mapdetail.html'
    context_object_name = 'mapdetail'

def delete_map(request, pk):
    if request.method == 'POST':
        person = models.AptMap.objects.get(pk=pk)
        person.delete()
    return redirect('map_list')
