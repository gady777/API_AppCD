from rest_framework import viewsets
from .models import Entrepreneur
from .serializers import EntrepreneurSerializer

class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

