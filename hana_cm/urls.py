from django.urls import path
from . import views

app_name = 'hana_cm'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/k_create/', views.youkaigo_create.as_view(), name='kcreate'),
    path('<int:pk>/k_detail/',views.youkaigo_DetailView.as_view(), name='kdetail'),
    path('<int:pk>/k_update/', views.youkaigo_UpdateView.as_view(), name='kupdate'),
    path(r'',Find.as_view(),name='find'),
]