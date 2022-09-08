from rest_framework import generics

from .models import Data
from .serializers import DataSerializer

class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

