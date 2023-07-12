from django.urls import path
from .views import UserRegisterView, UserEditView

    # $ Here <int:pk> is a Primary_Key value... (SQL column/row)
    # ? http://127.0.0.1:8000/article/1 
    # ! Meaning it is a potential Cyber Risk, for SQL_injections


urlpatterns = [
    path('register/',       UserRegisterView.as_view(),     name='register'),
    path('edit_profile/',   UserEditView.as_view(),         name='edit_profile'),
]
