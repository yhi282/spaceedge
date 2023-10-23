from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import *

admin.site.index_title = "SpaceEdge 관리자"
admin.site.site_header = "SpaceEdge Admin"
admin.site.site_title = "spaceedge admin"

TokenAdmin.raw_id_fields = ['user']

class AuthUser:
    class Meta:
        verbose_name_plural = "API 사용자"