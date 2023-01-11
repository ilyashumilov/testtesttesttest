from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image, User
from .serializers import ImageSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
import random
import os
from django.db.models.functions import Lower


# Create your views here.


def auth_docorator(func):
    def wrapper(*args):
        if "HTTP_AUTHORIZATION" not in args[1].META:
            return Response(
                {"message": "Not authorized request"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        else:
            try:
                token = args[1].META["HTTP_AUTHORIZATION"].replace("Bearer ", "")
                user = get_object_or_404(User, token=token)
            except:
                return Response(
                    {"Messge": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
                )
        return func(*args)

    return wrapper


class ImageView(APIView):
    @auth_docorator
    def get(self, request):
        queryset = Image.objects.all()
        id = request.data.get("id")
        geolocation = request.data.get("geolocation")
        date = request.data.get("date")
        name = request.data.get("name")

        if id:
            queryset = queryset.filter(id=id)
        if geolocation:
            queryset = queryset.filter(geolocation=geolocation)
        elif date:
            queryset = queryset.filter(date=date)
        elif name:
            queryset = queryset.filter(name__contains=name)

        serializer = ImageSerializer(queryset, many=True)

        return Response(
            serializer.data,
            status=200,
        )

    @auth_docorator
    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "The new Image instance has been created"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class UserCreation(APIView):
    def get(self, request):
        hash = random.getrandbits(128)
        instance = User(token=hash)
        instance.save()

        return Response({"Token": instance.token}, status=status.HTTP_200_OK)
