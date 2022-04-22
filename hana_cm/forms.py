''' from django import forms
from .models import YouKaigoDo

class YoykaigoDoForm(forms.ModelForm):
    
    class Meta:
        model = YouKaigoDo
        fields = ['riyousha', 'youkaigodo_nyuuryokuDate', 'nintei_date',
        ]
 '''