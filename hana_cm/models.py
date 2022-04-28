from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#利用者クラス
class Riyousha(models.Model):
    hihoken_no = models.BigIntegerField()
    name = models.CharField(max_length=50)
    name_kana = models.CharField(max_length=100)
    nyuuryoku_date = models.DateField(auto_now_add=False)
    sex = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    #slug = models.SlugField(max_length=20, blank=True, null=True)
   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hana_cm:detail', kwargs={'pk': self.pk})

class YouKaigoDo(models.Model):
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='Youkaigodo_riyousha')
    
    youkaigodo_nyuuryokuDate = models.DateField(auto_now_add=False)
    kaigodo = models.ForeignKey('Kaigodo', on_delete=models.PROTECT, db_column='kaigodo')
    nintei_date = models.DateField(auto_now_add=False)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        constraints = [
            # 先生-レッスン実施日のペアでユニーク制約
            models.UniqueConstraint(
                fields=["riyousha", "youkaigodo_nyuuryokuDate"],
                name="riyousha_date_unique"
            )
        ]

    def get_absolute_url(self):
        return reverse('hana_cm:kdetail', kwargs={'pk': self.pk}) 

''' class NyuuryokuDate(models.Model):
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='nyuuryoku_riyousha')
    nyuuryoku_date = models.DateField(auto_now_add= False) '''

''' class Youkaigodo_NyuuryokuDate(models.Model):
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='youkaigodo_nyuuryoku_riyousha')
    nyuuryoku_date = models.DateField(auto_now_add= False) '''

class Adress(models.Model):
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='adress_riyousha')
    post_no = models.CharField(max_length=8,)
    adress = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

class CareManager(models.Model):
    riyousha=models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='cm_riyousha')
    cm_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cm_name



class Kaigodo(models.Model):
    ''' riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE,\
        related_name='kaigodo_riyousha') '''
    kaigodo = models.CharField(max_length=4)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kaigodo

class Riyousha_kihon(models.Model):
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE)
    adress = models.ForeignKey('Adress', on_delete=models.CASCADE)
    caremanager = models.ForeignKey('CareManager', on_delete=models.CASCADE)

class Adl_1(models.Model):
    IS_USED_CHOICES = (
        (False, 'なし'),
        (True, 'あり'),
    )
    riyousha = models.ForeignKey('Riyousha', on_delete=models.CASCADE)
    nyuuryoku_date = models.DateField(auto_now_add=False)
    non = models.BooleanField( help_text="「なし」なら、チェックしてください",)
    left_upper_limbs = models.BooleanField( choices=IS_USED_CHOICES,help_text="「左上肢に麻痺」があれば、チェックしてください")
    left_lower_limbs = models.BooleanField( choices=IS_USED_CHOICES,help_text="「左下肢に麻痺」があれば、チェックしてください")
    right_upper_limbs = models.BooleanField( choices=IS_USED_CHOICES,help_text="「右上肢に麻痺」があれば、チェックしてください")
    right_lower_limbs = models.BooleanField( choices=IS_USED_CHOICES,help_text="「右下肢に麻痺」があれば、チェックしてください")
    others = models.BooleanField( help_text="「その他」があれば、チェックしてください。詳細を「麻痺その他」に記入してください")
    paralysis_others = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published',auto_now_add=True)