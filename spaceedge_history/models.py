# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AiInputdataHistory(models.Model):
    sid = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='Hour', blank=True, null=True)  # Field name made lowercase.
    minute = models.IntegerField(db_column='Minute', blank=True, null=True)  # Field name made lowercase.
    second = models.IntegerField(db_column='Second', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    in_temp = models.FloatField(db_column='In_Temp', blank=True, null=True)  # Field name made lowercase.
    in_rh = models.IntegerField(db_column='In_RH', blank=True, null=True)  # Field name made lowercase.
    in_illu = models.IntegerField(db_column='In_Illu', blank=True, null=True)  # Field name made lowercase.
    in_pm1 = models.IntegerField(db_column='In_PM1', blank=True, null=True)  # Field name made lowercase.
    in_pm25 = models.IntegerField(db_column='In_PM25', blank=True, null=True)  # Field name made lowercase.
    in_pm10 = models.IntegerField(db_column='In_PM10', blank=True, null=True)  # Field name made lowercase.
    in_co2 = models.IntegerField(db_column='In_CO2', blank=True, null=True)  # Field name made lowercase.
    in_room = models.IntegerField(db_column='In_Room', blank=True, null=True)  # Field name made lowercase.
    in_tvoc = models.IntegerField(db_column='In_TVOC', blank=True, null=True)  # Field name made lowercase.
    out_temp = models.FloatField(db_column='Out_Temp', blank=True, null=True)  # Field name made lowercase.
    out_rh = models.IntegerField(db_column='Out_RH', blank=True, null=True)  # Field name made lowercase.
    out_pm25 = models.IntegerField(db_column='Out_PM25', blank=True, null=True)  # Field name made lowercase.
    out_pm10 = models.IntegerField(db_column='Out_PM10', blank=True, null=True)  # Field name made lowercase.
    set_temp_min_comf = models.FloatField(db_column='Set_Temp_Min_Comf', blank=True, null=True)  # Field name made lowercase.
    set_temp_max_comf = models.FloatField(db_column='Set_Temp_Max_Comf', blank=True, null=True)  # Field name made lowercase.
    set_rh_min_comf = models.IntegerField(db_column='Set_RH_Min_Comf', blank=True, null=True)  # Field name made lowercase.
    set_rh_max_comf = models.IntegerField(db_column='Set_RH_Max_Comf', blank=True, null=True)  # Field name made lowercase.
    set_temp_min_es = models.FloatField(db_column='Set_Temp_Min_ES', blank=True, null=True)  # Field name made lowercase.
    set_temp_max_es = models.FloatField(db_column='Set_Temp_Max_ES', blank=True, null=True)  # Field name made lowercase.
    set_rh_min_es = models.IntegerField(db_column='Set_RH_Min_ES', blank=True, null=True)  # Field name made lowercase.
    set_rh_max_es = models.IntegerField(db_column='Set_RH_Max_ES', blank=True, null=True)  # Field name made lowercase.
    set_temp_min_heal = models.FloatField(db_column='Set_Temp_Min_Heal', blank=True, null=True)  # Field name made lowercase.
    set_temp_max_heal = models.FloatField(db_column='Set_Temp_Max_Heal', blank=True, null=True)  # Field name made lowercase.
    set_rh_min_heal = models.IntegerField(db_column='Set_RH_Min_Heal', blank=True, null=True)  # Field name made lowercase.
    set_rh_max_heal = models.IntegerField(db_column='Set_RH_Max_Heal', blank=True, null=True)  # Field name made lowercase.
    user_set_temp_min_comf = models.FloatField(db_column='User_Set_Temp_Min_Comf', blank=True, null=True)  # Field name made lowercase.
    user_set_temp_max_comf = models.FloatField(db_column='User_Set_Temp_Max_Comf', blank=True, null=True)  # Field name made lowercase.
    user_set_rh_min_comf = models.IntegerField(db_column='User_Set_RH_Min_Comf', blank=True, null=True)  # Field name made lowercase.
    user_set_rh_max_comf = models.IntegerField(db_column='User_Set_RH_Max_Comf', blank=True, null=True)  # Field name made lowercase.
    acn_ctrl = models.IntegerField(db_column='ACN_Ctrl', blank=True, null=True)  # Field name made lowercase.
    acl_ctrl = models.IntegerField(db_column='ACL_Ctrl', blank=True, null=True)  # Field name made lowercase.
    hum_ctrl = models.IntegerField(db_column='HUM_Ctrl', blank=True, null=True)  # Field name made lowercase.
    lig_ctrl = models.IntegerField(db_column='LIG_Ctrl', blank=True, null=True)  # Field name made lowercase.
    hea_ctrl = models.IntegerField(db_column='HEA_Ctrl', blank=True, null=True)  # Field name made lowercase.
    ven_ctrl = models.IntegerField(db_column='VEN_Ctrl', blank=True, null=True)  # Field name made lowercase.
    boi_ctrl_pwr_wire = models.IntegerField(db_column='BOI_Ctrl_Pwr_Wire', blank=True, null=True)  # Field name made lowercase.
    boi_tem_wire = models.IntegerField(db_column='BOI_tem_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_ctrl_wire = models.IntegerField(db_column='VEN_Ctrl_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_mode_wire = models.IntegerField(db_column='VEN_Mode_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_wind_wire = models.IntegerField(db_column='VEN_Wind_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_ctrl_wire = models.IntegerField(db_column='BLI_Ctrl_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_posi_wire = models.IntegerField(db_column='BLI_Posi_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_tilt_wire = models.IntegerField(db_column='BLI_Tilt_Wire', blank=True, null=True)  # Field name made lowercase.
    ther_ctrl_pwr_wire = models.IntegerField(db_column='Ther_Ctrl_Pwr_Wire', blank=True, null=True)  # Field name made lowercase.
    ther_tem_pwr_wire = models.IntegerField(db_column='Ther_Tem_Pwr_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_ctrl_wire = models.IntegerField(db_column='ACL_Ctrl_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_ctrl_wind_wire = models.IntegerField(db_column='ACL_Ctrl_Wind_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_ctrl_mode_wire = models.IntegerField(db_column='ACL_Ctrl_Mode_Wire', blank=True, null=True)  # Field name made lowercase.
    delta_t = models.FloatField(db_column='Delta_T', blank=True, null=True)  # Field name made lowercase.
    nocc_temp = models.FloatField(db_column='NOcc_Temp', blank=True, null=True)  # Field name made lowercase.
    auto_ctrl = models.IntegerField(db_column='Auto_Ctrl', blank=True, null=True)  # Field name made lowercase.
    ai_mode = models.IntegerField(db_column='AI_Mode', blank=True, null=True)  # Field name made lowercase.
    ai_comf = models.IntegerField(db_column='AI_Comf', blank=True, null=True)  # Field name made lowercase.
    ai_es = models.IntegerField(db_column='AI_ES', blank=True, null=True)  # Field name made lowercase.
    ai_heal = models.IntegerField(db_column='AI_Heal', blank=True, null=True)  # Field name made lowercase.
    ai_out = models.IntegerField(db_column='AI_Out', blank=True, null=True)  # Field name made lowercase.
    occ_decision = models.IntegerField(db_column='Occ_Decision', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ai_inputdata_history'
        app_label = 'spaceedge_history'
        verbose_name_plural = 'AI InputData History'


class AiOutputdataHistory(models.Model):
    sid = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='Hour', blank=True, null=True)  # Field name made lowercase.
    minute = models.IntegerField(db_column='Minute', blank=True, null=True)  # Field name made lowercase.
    second = models.IntegerField(db_column='Second', blank=True, null=True)  # Field name made lowercase.
    occ = models.IntegerField(db_column='Occ', blank=True, null=True)  # Field name made lowercase.
    acn_on_ir = models.IntegerField(db_column='ACN_On_IR', blank=True, null=True)  # Field name made lowercase.
    acn_off_ir = models.IntegerField(db_column='ACN_Off_IR', blank=True, null=True)  # Field name made lowercase.
    acl_on_ir = models.IntegerField(db_column='ACL_On_IR', blank=True, null=True)  # Field name made lowercase.
    acl_off_ir = models.IntegerField(db_column='ACL_Off_IR', blank=True, null=True)  # Field name made lowercase.
    hum_on_ir = models.IntegerField(db_column='HUM_On_IR', blank=True, null=True)  # Field name made lowercase.
    hum_off_ir = models.IntegerField(db_column='HUM_Off_IR', blank=True, null=True)  # Field name made lowercase.
    hea_on_ir = models.IntegerField(db_column='HEA_On_IR', blank=True, null=True)  # Field name made lowercase.
    hea_off_ir = models.IntegerField(db_column='HEA_Off_IR', blank=True, null=True)  # Field name made lowercase.
    ven_on_ir = models.IntegerField(db_column='VEN_On_IR', blank=True, null=True)  # Field name made lowercase.
    ven_off_ir = models.IntegerField(db_column='VEN_Off_IR', blank=True, null=True)  # Field name made lowercase.
    lig_on_ir = models.IntegerField(db_column='LIG_On_IR', blank=True, null=True)  # Field name made lowercase.
    lig_off_ir = models.IntegerField(db_column='LIG_Off_IR', blank=True, null=True)  # Field name made lowercase.
    boi_on_wire = models.IntegerField(db_column='BOI_On_Wire', blank=True, null=True)  # Field name made lowercase.
    boi_off_wire = models.IntegerField(db_column='BOI_Off_Wire', blank=True, null=True)  # Field name made lowercase.
    boi_tem_wire = models.IntegerField(db_column='BOI_Tem_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_on_wire = models.IntegerField(db_column='VEN_On_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_off_wire = models.IntegerField(db_column='VEN_Off_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_wind_wire = models.IntegerField(db_column='VEN_Wind_Wire', blank=True, null=True)  # Field name made lowercase.
    ven_mode_wire = models.IntegerField(db_column='VEN_Mode_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_up_wire = models.IntegerField(db_column='BLI_UP_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_down_wire = models.IntegerField(db_column='BLI_Down_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_posi_wire = models.IntegerField(db_column='BLI_Posi_Wire', blank=True, null=True)  # Field name made lowercase.
    bli_tilt_wire = models.IntegerField(db_column='BLI_Tilt_Wire', blank=True, null=True)  # Field name made lowercase.
    ther_on_wire = models.IntegerField(db_column='Ther_On_Wire', blank=True, null=True)  # Field name made lowercase.
    ther_off_wire = models.IntegerField(db_column='Ther_Off_Wire', blank=True, null=True)  # Field name made lowercase.
    ther_tem_wire = models.IntegerField(db_column='Ther_Tem_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_on_wire = models.IntegerField(db_column='ACL_On_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_off_wire = models.IntegerField(db_column='ACL_Off_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_wind_wire = models.IntegerField(db_column='ACL_Wind_Wire', blank=True, null=True)  # Field name made lowercase.
    acl_mode_wire = models.IntegerField(db_column='ACL_Mode_Wire', blank=True, null=True)  # Field name made lowercase.
    ai_comf_ctrl = models.IntegerField(db_column='AI_Comf_Ctrl', blank=True, null=True)  # Field name made lowercase.
    ai_es_ctrl = models.IntegerField(db_column='AI_ES_Ctrl', blank=True, null=True)  # Field name made lowercase.
    ai_heal_ctrl = models.IntegerField(db_column='AI_Heal_Ctrl', blank=True, null=True)  # Field name made lowercase.
    ai_out_ctrl = models.IntegerField(db_column='AI_Out_Ctrl', blank=True, null=True)  # Field name made lowercase.
    push = models.CharField(db_column='Push', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ai_outputdata_history'
        app_label = 'spaceedge_history'
        verbose_name_plural = 'AI OutputData History'


class EnvHistory(models.Model):
    sid = models.AutoField(primary_key=True)
    did = models.IntegerField()
    s_num = models.CharField(max_length=50)
    area_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=2)
    dong_code = models.CharField(max_length=4)
    temp = models.FloatField()
    humi = models.IntegerField()
    co2 = models.IntegerField()
    dust_pm_1 = models.IntegerField()
    dust_pm_25 = models.IntegerField()
    dust_pm_10 = models.IntegerField()
    illuminance = models.IntegerField()
    voc = models.IntegerField()
    eco2 = models.IntegerField()
    in_room = models.IntegerField()
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'env_history'
        app_label = 'spaceedge_history'
        verbose_name_plural = 'Env History'


class RemoteHistory(models.Model):
    sid = models.AutoField(primary_key=True)
    m_sid = models.IntegerField()
    did = models.IntegerField()
    fac_type = models.IntegerField()
    remote_id = models.IntegerField()
    brand_id = models.IntegerField()
    remote_type = models.IntegerField(blank=True, null=True)
    ir_type = models.IntegerField()
    work_type = models.IntegerField()
    season_type = models.IntegerField()
    btn_type = models.IntegerField(blank=True, null=True)
    btn_id = models.IntegerField(blank=True, null=True)
    onoff_flag = models.IntegerField(blank=True, null=True)
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'remote_history'
        app_label = 'spaceedge_history'


class WeatherHistory(models.Model):
    sid = models.AutoField(primary_key=True)
    area_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=2)
    dong_code = models.CharField(max_length=4)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dong = models.CharField(max_length=50)
    temp = models.FloatField(blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    dust_pm_25 = models.IntegerField(blank=True, null=True)
    dust_pm_10 = models.IntegerField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    co2 = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    so2 = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    vec = models.IntegerField(blank=True, null=True)
    wsd = models.FloatField(blank=True, null=True)
    rn = models.FloatField(blank=True, null=True)
    mj = models.FloatField(blank=True, null=True)
    skc = models.IntegerField(blank=True, null=True)
    hr = models.FloatField(blank=True, null=True)
    sky = models.IntegerField(blank=True, null=True)
    pty = models.IntegerField(blank=True, null=True)
    now_weather = models.IntegerField(blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_history'
        app_label = 'spaceedge_history'
