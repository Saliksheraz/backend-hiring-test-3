from rest_framework.response import Response
from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Bookshelf, Volume, ReadingPos, Review


class volumeViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = Volume.objects.all()
        qs_json = serializers.serialize('json', allData)
        return Response(qs_json)

    def post(self, request):
        name = request.POST.get('name')
        Volume.objects.create(name=name)
        return Response(status=200)


class bookshelfViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = Bookshelf.objects.filter(user=request.user) | Bookshelf.objects.filter(is_private=False)
        qs_json = serializers.serialize('json', allData)
        return Response(qs_json)

    def post(self, request):
        name = request.POST.get('name')
        volume = request.POST.get('volume')
        is_private = request.POST.get('is_private')
        if is_private == 'true':
            is_private = True
        else:
            is_private = False
        Bookshelf.objects.create(name=name, user=request.user, is_private=is_private, volume=int(volume))
        return Response(status=200)


class readingPosViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = ReadingPos.objects.filter(user=request.user)
        qs_json = serializers.serialize('json', allData)
        return Response(qs_json)

    def post(self, request):
        val = request.POST.get('val')
        volume = request.POST.get('volume')
        ReadingPos.objects.create(val=val, user=request.user, volume=int(volume))
        return Response(status=200)


class reviewViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = Review.objects.filter(user=request.user)
        qs_json = serializers.serialize('json', allData)
        return Response(qs_json)

    def post(self, request):
        val = request.POST.get('val')
        volume = request.POST.get('volume')
        dublicateCheck = Review.objects.filter(user=request.user, volume_id=int(volume))
        if dublicateCheck:
            return Response(status=404)
        Review.objects.create(val=val, user=request.user, volume=int(volume))
        return Response(status=200)
