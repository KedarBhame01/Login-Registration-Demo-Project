from django.urls import path,include
from .views import s, student_api, new_login_view, login_api, dashboard_view, login_page_view

urlpatterns = [
    path('',s, name = 's'),
    path('api/',student_api, name='student_api'),
    path('signup/',new_login_view, name='new_login_view'),
    path('login-api/',login_api, name='login_api'),
    path('dashboard/',dashboard_view, name='dashboard_view'),
    path('login/',login_page_view, name='login_page_view'),
]