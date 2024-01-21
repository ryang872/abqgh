from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from . import models, forms

class GateCodeHome(LoginRequiredMixin, ListView):
    template_name = "gate.html"
    model = models.addGate
    context_object_name = 'gates'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.addGate.objects.filter(complex__icontains=query)
        else:
            return models.addGate.objects.all()

class AddNewCode(LoginRequiredMixin, CreateView):
    template_name = 'addgate.html'
    model = models.addGate
    form_class = forms.gateForm
    success_url = reverse_lazy('gate_list')

class GateDetailView(LoginRequiredMixin, DetailView):
    model = models.addGate
    template_name = 'gatedetail.html'
    context_object_name = 'gatedetail'


def delete_gate(request, pk):
    if request.method == 'POST':
        person = models.addGate.objects.get(pk=pk)
        person.delete()
    return redirect('gate_list')