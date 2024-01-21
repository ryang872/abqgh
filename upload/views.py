from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import tipForm
from .models import noTip

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class TipListView(LoginRequiredMixin, ListView):
    model = noTip
    template_name = 'tip_list.html'
    context_object_name = 'tips'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return noTip.objects.filter(first__icontains=query)
        else:
            return noTip.objects.all()

class TipDetailView(LoginRequiredMixin, DetailView):
    model = noTip
    template_name = 'detail.html'
    context_object_name = 'tipDetail'

class UploadTipView(LoginRequiredMixin, CreateView):
    model = noTip
    form_class = tipForm
    success_url = reverse_lazy('tip_list')
    template_name = 'upload_tip.html'


def delete_person(request, pk):
    if request.method == 'POST':
        person = noTip.objects.get(pk=pk)
        person.delete()
    return redirect('tip_list')
