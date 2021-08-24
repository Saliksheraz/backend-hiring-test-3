from django.http import HttpResponse
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
        return HttpResponse(qs_json, content_type='application/json')

    def post(self, request):
        name = request.POST.get('name')
        Volume.objects.create(name=name)
        content = {'message': 'Volume added successfully'}
        return Response(content)


class bookshelfViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = Bookshelf.objects.filter(user=request.user) | Bookshelf.objects.filter(is_private=False)
        qs_json = serializers.serialize('json', allData)
        return HttpResponse(qs_json, content_type='application/json')

    def post(self, request):
        name = request.POST.get('name')
        volume_id = request.POST.get('volume_id')
        is_private = request.POST.get('is_private')
        if is_private == 'true':
            is_private = True
        else:
            is_private = False
        Bookshelf.objects.create(name=name, user=request.user, is_private=is_private,
                                 volume=Volume.objects.get(id=volume_id))
        content = {'message': 'Bookshelf added successfully'}
        return Response(content)


class readingPosViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = ReadingPos.objects.filter(user=request.user)
        qs_json = serializers.serialize('json', allData)
        return HttpResponse(qs_json, content_type='application/json')

    def post(self, request):
        val = request.POST.get('val')
        volume_id = request.POST.get('volume_id')
        dublicateCheck = ReadingPos.objects.filter(volume=Volume.objects.get(id=volume_id), user=request.user)
        if dublicateCheck:
            content = {'message': 'Reading Position to this volume is already given by this user'}
            return Response(content)
        ReadingPos.objects.create(val=int(val), user=request.user, volume=Volume.objects.get(id=volume_id))
        content = {'message': 'Reading position added successfully'}
        return Response(content)


class reviewViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allData = Review.objects.filter(user=request.user)
        qs_json = serializers.serialize('json', allData)
        return HttpResponse(qs_json, content_type='application/json')

    def post(self, request):
        val = request.POST.get('val')
        volume_id = request.POST.get('volume_id')
        dublicateCheck = Review.objects.filter(user=request.user, volume=Volume.objects.get(id=volume_id))
        if dublicateCheck:
            content = {'message': 'Review to this volume is already given by this user'}
            return Response(content)
        Review.objects.create(val=int(val), user=request.user, volume=Volume.objects.get(id=volume_id))
        content = {'message': 'Review added successfully'}
        return Response(content)
