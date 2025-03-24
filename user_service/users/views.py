from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
def home(request):
    return render(request, 'templates/home.html')