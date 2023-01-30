from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('index2',views.index2),
    path('signup/',views.signup),
    path('ragistration/',views.ragistration),       
    path('table/',views.table),
    path('update_view/<int:uid>/',views.update_view),
    path('update_data/',views.update_data),
    path('login/',views.login)

 ]
