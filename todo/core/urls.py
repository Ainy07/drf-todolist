from django.urls import path
from core import views
urlpatterns = [
    path('',views.Homeview),
    path('DetailView/<int:pk>/',views.DetailView),
    path('CreateView/',views.CreateView),
    path('UpdateView/<int:pk>/',views.UpdateView),
    path('DeleteView/<int:pk>/',views.DeleteView)
]
