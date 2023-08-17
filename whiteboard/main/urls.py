from django.urls import path
from main import views

# urlpatterns = [
#     path('', views.index, name = "index"),

# ]
# whiteboard_app/urls.py

from django.urls import path
from .views import WhiteboardListCreateView, WhiteboardRetrieveView
app_name = 'main' 
urlpatterns = [
    path('', views.index, name = "index"),
    path('whitebaords/', WhiteboardListCreateView.as_view(), name='whiteboard-list-create'),
    path('whitebaords/<int:pk>/', WhiteboardRetrieveView.as_view(), name='whiteboard-retrieve'),
]
