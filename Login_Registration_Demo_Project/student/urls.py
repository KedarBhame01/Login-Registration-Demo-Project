from django.urls import path,include
from .views import s, student_api, new_login_view
urlpatterns = [
    path('',s, name = 's'),
    path('api/',student_api, name='student_api'),
    path('login/',new_login_view, name='new_login_view'),
]
