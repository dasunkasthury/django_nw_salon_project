from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Freelancer


class IndexView(generic.ListView):
    template_name = 'stylist/index.html'
    context_object_name = 'All_Freelancer'

    def get_queryset(self):
        return Freelancer.objects.all()


class DetailView(generic.DetailView):
    model = Freelancer
    template_name = 'stylist/detail.html'


class FreelancerCreate(CreateView):
    model = Freelancer
    fields = ['freelancer_name', 'age', 'value', 'type', 'time_slot_id', 'image']


class FreelancerUpdate(UpdateView):
    model = Freelancer
    fields = ['freelancer_name', 'age', 'value', 'type', 'time_slot_id', 'image']


class FreelancerDelete(DeleteView):
    model = Freelancer
    success_url = reverse_lazy('stylist:index')



