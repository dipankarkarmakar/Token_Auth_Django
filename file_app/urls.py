# from django.urls import path
# from .views import UserCreate
#
#
# urlpatterns = [
#     path('file/', UserCreate),
#
# ]

from django.urls import path
from .views import FileView
urlpatterns = [
    path('file/', FileView),
]