from django.urls import path
from .views import SpaceEdge, Ipark, Jinly
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    ### 토큰 생성
    path('api-token-auth', obtain_auth_token, name='토큰 생성'),
    ### 전체 데이터
    path('spaceedge/inputdata', SpaceEdge.Inputdata.as_view(), name= 'Input data 전체'), # inputdata
    path('spaceedge/<str:pk>/inputdata', SpaceEdge.InputdataOne.as_view(), name= "Input data 개별(시리얼넘버)"), # inputdata 개별
    path('spaceedge/outputdata', SpaceEdge.Outputdata.as_view(), name="Output data 전체"), # outputdata
    path('spaceedge/<str:pk>/outputdata', SpaceEdge.OutputdataOne.as_view(), name= "Output data 개별(시리얼넘버)"), # outputdata 개별
    path('spaceedge/<str:pk>/acn', SpaceEdge.ACNdata.as_view(), name="에어컨 기기 제어"),
    path('spaceedge/<str:pk>/acl', SpaceEdge.ACLdata.as_view(), name="공기청정기 기기 제어"),
    path('spaceedge/device', SpaceEdge.Device.as_view(), name="Device 전체"), # Device 전체
    path('spaceedge/<str:s_num>/device', SpaceEdge.DeviceOne.as_view(), name= "Device 개별(시리얼넘버)"), # Device 개별
    path('spaceedge/mbrs', SpaceEdge.Mbrs.as_view(), name="Mbrs 어플 유저 전체"), # Mbrs 전체
    path('spaceedge/<str:id>/mbrs', SpaceEdge.MbrsOne.as_view(), name="Mbrs 어플 유저 개별(email)"), # Mbrs 개별

    ### 기기제어
    # path('spaceedge/<str:pk>/acn', All.ACNdata.as_view()), # acndata 에어컨
    # path('spaceedge/<str:pk>/acl', All.ACLdata.as_view()), # acldata 공기청정기

    ### ipark
    path('edge-ipark/<int:pk>/device', Ipark.Device.as_view(), name= "아이파크 환경정보(시리얼넘버)"), # Device 개별

    ### jinly
    path('edge-Jinly/<str:s_num>/device', Jinly.Device.as_view(), name="진리관 환경정보(시리얼넘버)"), # Device 개별
]    
    