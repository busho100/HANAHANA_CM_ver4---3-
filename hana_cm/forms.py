from django import forms
from .models import YouKaigoDo,Riyousha
#from bootstrap_datepicker_plus import DatePickerInput

''' class YoykaigoDoForm(forms.ModelForm):
    
    class Meta:
        model = YouKaigoDo
        fields = ['riyousha', 'youkaigodo_nyuuryokuDate', 'nintei_date',
        ]
 '''
class FindForm(forms.Form):
    find = forms.CharField(max_length=255, label='利用者名',required=False,\
        widget=forms.TextInput(attrs = {'class':'form-controle'})) 


class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Riyousha
        ''' widgets = {'nyuuryoku_date':DatePickerInput(format='%y-%m-%d')
        } '''
        
        fields = ('hihoken_no','name','name_kana','nyuuryoku_date','sex')
        labels = {
            'hihoken_no':'被保険者番号',
            'name':'氏名',
            'name_kana':'氏名カナ',
            'nyuuryoku_date':'入力日',
            'sex':'性別',
        }

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Riyousha
        ''' widgets = {'nyuuryoku_date':DatePickerInput(format='%y-%m-%d')
        } '''
        
        fields = ('hihoken_no','name','name_kana','nyuuryoku_date','sex')
        labels = {
            'hihoken_no':'被保険者番号',
            'name':'氏名',
            'name_kana':'氏名カナ',
            'nyuuryoku_date':'入力日',
            'sex':'性別',
        }
         

        