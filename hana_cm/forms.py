''' from django import forms
from .models import YouKaigoDo

class YoykaigoDoForm(forms.ModelForm):
    
    class Meta:
        model = YouKaigoDo
        fields = ['riyousha', 'youkaigodo_nyuuryokuDate', 'nintei_date',
        ]
 '''
class FindForm(forms.Form):
    find = forms.CharField(max_length=255, label='利用者名',required=False,\
        widget=forms.TextInput(attrs = {'class':'form-controle'})) 
        