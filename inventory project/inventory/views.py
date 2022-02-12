from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView

from inventory.forms import CreateInventoryForm, UpdateInventoryForm
from .models import Inventories
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
#from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.

#This is the homepage where all equipment will be listed based on user entry
class HomePageListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'invents'
    template_name = 'inventory/index.html'

    def get_queryset(self):
        return Inventories.objects.filter(manager=self.request.user).order_by('seq_number')

    def get_absolute_url(self):
        return reverse('details',
                        args=[
                              self.entry.year,
                              self.entry.month,
                              self.entry.day, self.slug])
    

# This is the logout view
class LogOutView(generic.RedirectView):
    url = reverse_lazy("login")
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


#This is the inventory details view
@login_required
def inventory_details(request, year, month, day, invent):
    invents = Inventories.objects.filter(manager=request.user)
    invent = get_object_or_404(invents, slug=invent,
                                      entry__year=year, 
                                      entry__month=month, 
                                      entry__day=day)
    context = {'invent': invent}
    return render(request, 'inventory/details.html', context)


class CreateInventoryView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Inventories
    form_class = CreateInventoryForm
    template_name = 'inventory/create_inventory.html'
    #fields = ['seq_number', 'equipment_name', 'serial_number', 'tag_number', 'status']

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class UpdateInventoryView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Inventories
    form_class = UpdateInventoryForm
    template_name = 'inventory/update_inventory.html'
    #fields = ['seq_number', 'equipment_name', 'serial_number', 'tag_number', 'status']

    def get_success_url(self):
        return reverse('index')

