from django.contrib import admin

# Register your models here.
from .models import *
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

@admin.register(AiInputdata)
class InputdataAdmin(admin.ModelAdmin):
    list_display=['id', 'in_temp', 'in_rh', 'in_illu', 'in_pm1', 'in_pm25', 'in_pm10', 'in_co2', 'in_room', 'in_tvoc', 'out_temp', 'out_rh', 'out_pm25', 'out_pm10', 
                  'auto_ctrl', 'ai_mode', 'ai_comf', 'ai_es', 'ai_heal', 'ai_out', 'regdate']
    search_fields=['id']
    list_per_page = 15
    #'set_temp_min_comf', 'set_temp_max_comf', 'set_rh_min_comf', 'set_rh_max_comf', 'set_temp_min_es', 'set_temp_max_es', 'set_rh_min_es', 'set_rh_max_es', 'set_temp_min_heal', 
    #'set_temp_max_heal', 'set_rh_min_heal', 'set_rh_max_heal', 'user_set_temp_min_comf', 'user_set_temp_max_comf', 'user_set_rh_min_comf', 'user_set_rh_max_comf', 'acn_ctrl', 
    #'acl_ctrl', 'hum_ctrl', 'lig_ctrl', 'hea_ctrl', 'ven_ctrl', 'boi_ctrl_pwr_wire', 'boi_tem_wire', 'ven_ctrl_wire', 'ven_mode_wire', 'ven_wind_wire', 'bli_ctrl_wire', 
    #'bli_posi_wire', 'bli_tilt_wire', 'ther_ctrl_pwr_wire', 'ther_tem_pwr_wire', 'acl_ctrl_wire', 'acl_ctrl_wind_wire', 'acl_ctrl_mode_wire', 'delta_t', 'nocc_temp',  'occ_decision', 

@admin.register(AiOutputdata)
class OutputdataAdmin(admin.ModelAdmin):
    list_display=['id', 'occ', 'acn_on_ir', 'acn_off_ir', 'acl_on_wire', 'acl_off_wire', 'acl_wind_wire', 'acl_mode_wire', 'ai_comf_ctrl', 'ai_es_ctrl', 'ai_heal_ctrl', 
                  'ai_out_ctrl', 'push', 'regdate']
    list_editable = ["acn_on_ir", "acn_off_ir", "acl_on_wire", "acl_off_wire"]
    search_fields=['id', 'year', 'occ']
    list_per_page = 15
    # , , 'acl_on_ir', 'acl_off_ir', 'hum_on_ir', 'hum_off_ir', 'hea_on_ir', 'hea_off_ir', 'ven_on_ir', 'ven_off_ir', 
    #'lig_on_ir', 'lig_off_ir', 'boi_on_wire', 'boi_off_wire', 'boi_tem_wire', 'ven_on_wire', 'ven_off_wire', 'ven_wind_wire', 'ven_mode_wire', 'bli_up_wire', 'bli_down_wire', 
    #'bli_posi_wire', 'bli_tilt_wire','ther_on_wire', 'ther_off_wire', 'ther_tem_wire'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display=['sid', 'm_sid', 's_num', 'name', 'wifi_id', 'wifi_pw', 'temp', 'humi', 'co2', 'dust_pm_1', 'dust_pm_25', 'dust_pm_10', 'illuminance', 'voc', 'eco2', 
                  'in_flag', 'delflag', 'regdate']
    search_fields=['sid', 'm_sid', 's_num']
    list_per_page = 15
    # 'room', 'room_floor', 'room_size', 'room_direction', 'room_man_cnt', 'work_type', 'season_type', 'in_room', 'env', , 'm_id'


@admin.register(Mbrs)
class MbrsAdmin(admin.ModelAdmin):
    list_display=['sid', 'id', 'model', 'nick', 'gender', 'age', 'birthday', 'login_cnt', 'login_date', 'regdate', 'delflag']
    search_fields=['sid', 'id', 'nick']
    list_per_page = 15
    # 'pw', 'login_type', 'kakao_id', 'naver_id', 'google_id', 'facebook_id', 'db_name', 'os', 'os_ver', 'token_key', 'alarm_type', 'level'


# admin.site.register(TestAiInputdata)
# admin.site.register(TestAiOutputdata)
# admin.site.register(TestDevice)
# admin.site.register(TestMbrs)

