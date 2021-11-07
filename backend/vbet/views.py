from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from .models import Vbet
from .serializer import SignatureGeneratorSerializers


class SignatureGenerator(viewsets.ModelViewSet):
    queryset = Vbet.objects.all()
    serializer_class = SignatureGeneratorSerializers
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

