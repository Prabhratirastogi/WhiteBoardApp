from django.shortcuts import render
from rest_framework import generics
from .models import Whiteboard, DrawingAction
from .serializers import WhiteboardSerializer

# Create your views here.
def index(request):
    return render(request, "index.html")


# whiteboard_app/views.py


class WhiteboardListCreateView(generics.ListCreateAPIView):
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer

class WhiteboardRetrieveView(generics.RetrieveAPIView):
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer
