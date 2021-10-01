from django.urls import path
from app.views import user_page

app_name = 'todo'

urlpatterns = [
    path('', user_page, name="user_page"),
    # path('user_edit/<int:pk>', user_edit, name="user_edit")
]