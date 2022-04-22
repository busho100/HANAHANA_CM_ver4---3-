from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Riyousha,YouKaigoDo
#from .forms import YoykaigoDoForm
from django.shortcuts import redirect
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render, get_object_or_404

# Create your views here.
class IndexView(generic.ListView):
    model = Riyousha

class DetailView(generic.DetailView):
    model = Riyousha
    

class CreateView(generic.edit.CreateView):
    model = Riyousha
    fields = '__all__'

class Riyousha_CreateView(generic.edit.CreateView):
    model = Riyousha
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Riyousha
    fields = '__all__'
    success_url = reverse_lazy('hana_cm:index')

class DeleteView(generic.edit.DeleteView):
    model = Riyousha
    success_url = reverse_lazy('hana_cm:index')

''' class DetailView(generic.DetailView):
    model = Riyousha '''

class youkaigo_create(generic.edit.CreateView):
    model = YouKaigoDo
    fields = '__all__'
    ''' widgets = {
            'date_field': AdminDateWidget(),
    } '''

class youkaigo_UpdateView(generic.edit.UpdateView):
    model = YouKaigoDo
    fields = '__all__'
    success_url = reverse_lazy('hana_cm:index')

''' class youkaigo_update(generic.edit.UpdateView):
    model = YouKaigoDo
    fields = '__all__'  '''

class youkaigo_DetailView(generic.DetailView):
    model = YouKaigoDo
    