from django.contrib import admin

# Register your models here.
from .models import *
from rest_framework.pagination import PageNumberPagination
# Register your models here.

@admin.register(AiInputdataHistory)
class InputdataHistoryAdmin(admin.ModelAdmin):
    list_display=['id', 'in_temp', 'in_rh', 'in_illu', 'in_pm1', 'in_pm25', 'in_pm10', 'in_co2', 'in_room', 'in_tvoc', 'out_temp', 'out_rh', 'out_pm25', 'out_pm10', 
    'set_temp_min_comf', 'set_temp_max_comf', 'set_rh_min_comf', 'set_rh_max_comf', 'set_temp_min_es', 'set_temp_max_es', 'set_rh_min_es', 'set_rh_max_es', 'set_temp_min_heal', 
    'set_temp_max_heal', 'set_rh_min_heal', 'set_rh_max_heal', 'user_set_temp_min_comf', 'user_set_temp_max_comf', 'user_set_rh_min_comf', 'user_set_rh_max_comf', 'acn_ctrl', 
    'acl_ctrl', 'hum_ctrl', 'lig_ctrl', 'hea_ctrl', 'ven_ctrl', 'boi_ctrl_pwr_wire', 'boi_tem_wire', 'ven_ctrl_wire', 'ven_mode_wire', 'ven_wind_wire', 'bli_ctrl_wire', 
    'bli_posi_wire', 'bli_tilt_wire', 'ther_ctrl_pwr_wire', 'ther_tem_pwr_wire', 'acl_ctrl_wire', 'acl_ctrl_wind_wire', 'acl_ctrl_mode_wire', 'delta_t', 'nocc_temp', 'auto_ctrl', 
    'ai_mode', 'ai_comf', 'ai_es', 'ai_heal', 'ai_out', 'occ_decision', 'regdate']
    search_fields=['id']
    list_per_page = 15

@admin.register(AiOutputdataHistory)
class OutputdataHistoryAdmin(admin.ModelAdmin):
    list_display=['id', 'occ', 'acn_on_ir', 'acn_off_ir', 'acl_on_ir', 'acl_off_ir', 'hum_on_ir', 'hum_off_ir', 'hea_on_ir', 'hea_off_ir', 'ven_on_ir', 'ven_off_ir', 
    'lig_on_ir', 'lig_off_ir', 'boi_on_wire', 'boi_off_wire', 'boi_tem_wire', 'ven_on_wire', 'ven_off_wire', 'ven_wind_wire', 'ven_mode_wire', 'bli_up_wire', 'bli_down_wire', 
    'bli_posi_wire', 'bli_tilt_wire','ther_on_wire', 'ther_off_wire', 'ther_tem_wire', 'acl_on_wire', 'acl_off_wire', 'acl_wind_wire', 'acl_mode_wire', 'ai_comf_ctrl', 'ai_es_ctrl', 
    'ai_heal_ctrl', 'ai_out_ctrl', 'push', 'regdate']
    search_fields=['id', 'year', 'occ']
    list_per_page = 15

@admin.register(EnvHistory)
class EnvHistoryAdmin(admin.ModelAdmin):
    list_display=['sid', 'did', 's_num', 'area_code', 'city_code', 'dong_code', 'temp', 'humi', 'co2', 'dust_pm_1', 'dust_pm_25', 'dust_pm_10', 'illuminance', 'voc', 'eco2', 'in_room', 'regdate']
    search_fields=['sid', 'did', 's_num']
    
    list_per_page = 15

