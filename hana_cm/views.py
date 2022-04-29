from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Riyousha,YouKaigoDo
from django.shortcuts import redirect
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CreateForm,UpdateForm
#from django.forms import FindForm

# Create your views here.
class IndexView(generic.ListView):
    model = Riyousha

class DetailView(generic.DetailView):
    model = Riyousha
    

class CreateView(generic.edit.CreateView):
    model = Riyousha
    #fields = '__all__'
    form_class = CreateForm
    model = Riyousha
    

class Riyousha_CreateView(generic.edit.CreateView):
    model = Riyousha
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Riyousha
    form_class = UpdateForm
    model = Riyousha
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
    success_url = reverse_lazy('hana_cm:youkaigodo')

''' class youkaigo_update(generic.edit.UpdateView):
    model = YouKaigoDo
    fields = '__all__'  '''

class youkaigo_DetailView(generic.DetailView):
    model = YouKaigoDo

class Find(View):

    def __init__(self):
        self.context = {
            'title': "要介護認定",
            'message':'認定状況',
            'form':FindForm()
        }

    def get(self,request):
        return render(request, 'hana_cm/find.html', self.context)

    def post(self,request):
        self.context['form'] = FindForm(request.POST)
        return render(request, 'hana_cm/find.html', self.context)

class Youkaigodo_IndexView(generic.ListView):
    model = YouKaigoDo

class Youkaigodo_DeleteView(generic.edit.DeleteView):
    model = YouKaigoDo
    success_url = reverse_lazy('hana_cm:youkaigodo')