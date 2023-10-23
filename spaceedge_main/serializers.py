from rest_framework import serializers
from spaceedge.models import *
from spaceedge_history.models import *

# space_edge
class InputdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiInputdata
        fields = "__all__"

class OutputdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiOutputdata
        fields = "__all__"
class ACNdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiOutputdata
        fields = ["id", "acn_on_ir", "acn_off_ir"]
        read_only_fields = ["id"]
class ACLdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiOutputdata
        fields = ["id", "acl_on_wire", "acl_off_wire"]
        read_only_fields = ["id"]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"

class DeviceClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        # fields = "__all__"
        fields = ["sid", "m_sid", "s_num", "name", "temp", "humi", "co2", "dust_pm_1", "dust_pm_25", "dust_pm_10", "voc", "regdate"]  # field 지정
        # exclude = []  # field 제외

class MbrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbrs
        fields = "__all__"

# space_edge_history
class InputdataHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AiInputdataHistory
        fields = "__all__"
class OutputdataHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AiOutputdataHistory
        fields = "__all__"
class EnvHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvHistory
        fields = "__all__"


