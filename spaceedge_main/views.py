from django.shortcuts import render

# Create your views here.
from django.db.models import Max, Min, Avg, Sum, Count

from spaceedge.models import Device
from .serializers import *

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

# Create your views here.

class PageNumberPagination(PageNumberPagination):
    page_size = 20

class ObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'name': user.username,
            'email': user.email,
            'token':token.key})

class SpaceEdge:
    class Inputdata(ListAPIView):
        queryset = AiInputdata.objects.all()
        serializer_class = InputdataSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
    
    class InputdataOne(RetrieveAPIView):
        queryset = AiInputdata.objects.all()
        serializer_class = InputdataSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]


    class Outputdata(ListAPIView):
        queryset = AiOutputdata.objects.all()
        serializer_class = OutputdataSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

    class OutputdataOne(RetrieveAPIView):
        queryset = AiOutputdata.objects.all()
        serializer_class = OutputdataSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

    class ACNdata(RetrieveUpdateAPIView): # 에어컨
        queryset = AiOutputdata.objects.all()
        serializer_class = ACNdataSerializer
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
    
    class ACLdata(RetrieveUpdateAPIView): # 공기청정기
        queryset = AiOutputdata.objects.all()
        serializer_class = ACLdataSerializer
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

    class Device(ListAPIView):
        queryset = Device.objects.all()
        serializer_class = DeviceSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        def get_queryset(self):
            duplicates= Device.objects.values("s_num").annotate(num_count=Count("s_num")).filter(num_count__gt=1)
            records = Device.objects.filter(s_num__in=[item['s_num'] for item in duplicates])
            duplicates_num = [item.sid for item in records]
            ex_num = max(duplicates_num)
            return Device.objects.exclude(sid=ex_num)

    class DeviceOne(RetrieveAPIView):
        queryset = Device.objects.all()
        serializer_class = DeviceSerializer
        # lookup_field = "s_num"
        # lookup_url_kwarg = "s_num"
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        def get_queryset(self):
            duplicates= Device.objects.values("s_num").annotate(num_count=Count("s_num")).filter(num_count__gt=1)
            records = Device.objects.filter(s_num__in=[item['s_num'] for item in duplicates])
            duplicates_num = [item.sid for item in records]
            ex_num = max(duplicates_num)
            return Device.objects.exclude(sid=ex_num)
        
    class Mbrs(ListAPIView):
        queryset = Mbrs.objects.all()
        serializer_class = MbrsSerializer
        pagination_class = PageNumberPagination
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

    class MbrsOne(RetrieveAPIView):
        queryset = Mbrs.objects.all()
        serializer_class = MbrsSerializer
        lookup_field = "id"
        lookup_url_kwarg = "id"
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]


class Ipark:
    # device 개별
    class Device(RetrieveAPIView):
        queryset = Device.objects.all()
        serializer_class = DeviceClientSerializer
        # lookup_field = "s_num"
        # lookup_url_kwarg = "s_num"
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        def get_queryset(self, *args, **kwargs):
            duplicates = Device.objects.values("s_num").annotate(num_count = Count("s_num")).filter(num_count__gt=1)
            records = Device.objects.filter(s_num__in = [item['s_num'] for item in duplicates])
            duplicates_num = [item.sid for item in records]
            ex_num = max(duplicates_num)
            return Device.objects.filter(m_sid = 136) # & (Device.objects.exclude(sid=ex_num))
        

       
class Jinly:
    # Device 개별
    class Device(RetrieveAPIView):
        queryset = Device.objects.all()
        serializer_class = DeviceClientSerializer
        # lookup_field = "s_num"
        # lookup_url_kwarg = "s_num"
        authentication_classes = [TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        def get_queryset(self):
            duplicates= Device.objects.values("s_num").annotate(num_count=Count("s_num")).filter(num_count__gt=1)
            records = Device.objects.filter(s_num__in=[item['s_num'] for item in duplicates])
            duplicates_num = [item.sid for item in records]
            ex_num = max(duplicates_num)
            return Device.objects.filter(m_sid = 76)  # & Device.objects.exclude(sid=ex_num)