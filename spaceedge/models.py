# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AiInputdata(models.Model):
    id = models.CharField(primary_key=True, db_column='ID', max_length=50, blank=True)  # Field name made lowercase.
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
    delta_t = models.FloatField(db_column='Delta_T')  # Field name made lowercase.
    nocc_temp = models.FloatField(db_column='NOcc_Temp')  # Field name made lowercase.
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
        db_table = 'ai_inputdata'
        app_label = 'spaceedge'
        verbose_name_plural = 'AI InputData'


class AiOutputdata(models.Model):
    id = models.CharField(primary_key=True, db_column='ID', max_length=50, blank=True)  # Field name made lowercase.
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
        db_table = 'ai_outputdata'
        app_label = 'spaceedge'
        verbose_name_plural = 'AI OutputData'


class AiSetInfo(models.Model):
    id = models.CharField(primary_key=True, db_column='ID', max_length=50, blank=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'ai_set_info'
        app_label = 'spaceedge'


class AiUpload(models.Model):
    sid = models.AutoField(primary_key=True)
    file_name = models.TextField(blank=True, null=True)
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ai_upload'
        app_label = 'spaceedge'


class Alarm(models.Model):
    sid = models.AutoField(primary_key=True)
    alarm_type = models.IntegerField()
    title = models.CharField(max_length=50, blank=True, null=True)
    msg = models.CharField(max_length=50, blank=True, null=True)
    solve_flag = models.IntegerField()
    push_date = models.DateTimeField(blank=True, null=True)
    regdate = models.DateTimeField()
    delflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alarm'
        app_label = 'spaceedge'


class AlarmMbrs(models.Model):
    m_sid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'alarm_mbrs'
        app_label = 'spaceedge'


class AlarmSetting(models.Model):
    sid = models.AutoField(primary_key=True)
    alarm_type = models.IntegerField()
    interval = models.IntegerField()
    standard = models.IntegerField()
    start_time = models.CharField(max_length=50, blank=True, null=True)
    end_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm_setting'
        app_label = 'spaceedge'


class Brand(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    brand_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'brand'
        app_label = 'spaceedge'


class BrandCable(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    brand_num = models.IntegerField()
    brand_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'brand_cable'
        app_label = 'spaceedge'


class BuildingUse(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'building_use'
        app_label = 'spaceedge'


class ButtonType(models.Model):
    fac_type = models.IntegerField()
    btn_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'button_type'
        app_label = 'spaceedge'


class CableBtn(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    brand_num = models.IntegerField()
    btn_type = models.IntegerField()
    use_flag = models.IntegerField()
    mode_type = models.IntegerField()
    mode_value = models.CharField(max_length=10)
    regdate = models.DateTimeField()
    delflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cable_btn'
        app_label = 'spaceedge'


class CableConnect(models.Model):
    sid = models.AutoField(primary_key=True)
    s_num = models.CharField(max_length=50)
    fac_type_1 = models.IntegerField(blank=True, null=True)
    status_1 = models.IntegerField(blank=True, null=True)
    fac_type_2 = models.IntegerField(blank=True, null=True)
    status_2 = models.IntegerField(blank=True, null=True)
    fac_type_3 = models.IntegerField(blank=True, null=True)
    status_3 = models.IntegerField(blank=True, null=True)
    fac_type_4 = models.IntegerField(blank=True, null=True)
    status_4 = models.IntegerField(blank=True, null=True)
    fac_type_5 = models.IntegerField(blank=True, null=True)
    status_5 = models.IntegerField(blank=True, null=True)
    regdate = models.DateTimeField()
    delflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cable_connect'
        app_label = 'spaceedge'


class Device(models.Model):
    sid = models.AutoField(primary_key=True)
    m_sid = models.IntegerField()
    s_num = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    room = models.CharField(max_length=50, blank=True, null=True)
    wifi_id = models.TextField()
    wifi_pw = models.CharField(max_length=50, blank=True, null=True)
    room_floor = models.IntegerField(blank=True, null=True)
    room_size = models.FloatField(blank=True, null=True)
    room_direction = models.CharField(max_length=50, blank=True, null=True)
    room_man_cnt = models.IntegerField(blank=True, null=True)
    work_type = models.IntegerField()
    season_type = models.IntegerField()
    temp = models.FloatField(blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    co2 = models.IntegerField(blank=True, null=True)
    dust_pm_1 = models.IntegerField(blank=True, null=True)
    dust_pm_25 = models.IntegerField(blank=True, null=True)
    dust_pm_10 = models.IntegerField(blank=True, null=True)
    illuminance = models.IntegerField(blank=True, null=True)
    voc = models.IntegerField(blank=True, null=True)
    eco2 = models.IntegerField(blank=True, null=True)
    in_room = models.IntegerField(blank=True, null=True)
    env = models.IntegerField()
    in_flag = models.IntegerField()
    regdate = models.DateTimeField()
    delflag = models.IntegerField()
    m_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'
        app_label = 'spaceedge'
        verbose_name_plural = 'device (엣지 사용 정보)'


class Facility(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    fac_kind = models.IntegerField()
    brand_id = models.IntegerField()
    fac_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facility'
        app_label = 'spaceedge'


class FacilityKind(models.Model):
    fac_type = models.IntegerField()
    fac_kind = models.IntegerField()
    kind_name = models.CharField(max_length=50)
    note = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facility_kind'
        app_label = 'spaceedge'


class IrDef(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    brand_id = models.IntegerField()
    remote_type = models.IntegerField()
    def_flag = models.IntegerField(blank=True, null=True)
    ir_code = models.CharField(max_length=5, blank=True, null=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    ir_value = models.TextField()
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ir_def'
        app_label = 'spaceedge'


class IrNew(models.Model):
    sid = models.AutoField(primary_key=True)
    m_sid = models.IntegerField()
    did = models.IntegerField()
    fac_type = models.IntegerField()
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    ir_code = models.CharField(max_length=5)
    remote_id = models.IntegerField()
    access_flag = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    ir_value = models.TextField(blank=True, null=True)
    in_flag = models.IntegerField()
    use_date = models.DateTimeField(blank=True, null=True)
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ir_new'
        app_label = 'spaceedge'


class Mbrs(models.Model):
    sid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    pw = models.CharField(max_length=50, blank=True, null=True)
    login_type = models.IntegerField()
    kakao_id = models.CharField(max_length=50, blank=True, null=True)
    naver_id = models.CharField(max_length=50, blank=True, null=True)
    google_id = models.CharField(max_length=50, blank=True, null=True)
    facebook_id = models.CharField(max_length=50, blank=True, null=True)
    db_name = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=1, blank=True, null=True)
    os_ver = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    nick = models.CharField(max_length=50, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    age = models.CharField(max_length=4, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    token_key = models.TextField(blank=True, null=True)
    alarm_type = models.IntegerField()
    level = models.IntegerField()
    login_cnt = models.IntegerField()
    login_date = models.CharField(max_length=50)
    regdate = models.DateTimeField(blank=True, null=True)
    delflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mbrs'
        app_label = 'spaceedge'
        verbose_name_plural = 'mbrs (어플 가입 정보)'


class Place(models.Model):
    sid = models.AutoField(primary_key=True)
    m_sid = models.IntegerField()
    name = models.CharField(max_length=50)
    area_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=2)
    dong_code = models.CharField(max_length=4)
    area = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    dong = models.CharField(max_length=10)
    building_use = models.CharField(max_length=10)
    floor = models.IntegerField()
    building_size = models.FloatField()
    direction = models.CharField(max_length=50)
    build_year = models.CharField(max_length=4)
    man_cnt = models.IntegerField()
    regdate = models.DateTimeField()
    delflag = models.IntegerField()
    building_year = models.CharField(max_length=255, blank=True, null=True)
    deflag = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'
        app_label = 'spaceedge'


class PlaceArea(models.Model):
    area_type = models.CharField(max_length=1)
    area_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=2, blank=True, null=True)
    dong_code = models.CharField(max_length=4, blank=True, null=True)
    area = models.CharField(max_length=10)
    city = models.CharField(max_length=10, blank=True, null=True)
    dong = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_area'
        app_label = 'spaceedge'


class Remote(models.Model):
    sid = models.AutoField(primary_key=True)
    m_sid = models.IntegerField()
    name = models.CharField(max_length=50)
    did = models.IntegerField()
    s_num = models.CharField(max_length=50)
    fac_type = models.IntegerField()
    fac_kind = models.IntegerField()
    fac_cnt = models.IntegerField()
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    set_year = models.CharField(max_length=4)
    remote_type = models.IntegerField(blank=True, null=True)
    control_type = models.IntegerField(blank=True, null=True)
    ir_type = models.IntegerField()
    onoff_flag = models.PositiveIntegerField()
    btn_1 = models.IntegerField(blank=True, null=True)
    btn_2 = models.IntegerField(blank=True, null=True)
    btn_3 = models.IntegerField(blank=True, null=True)
    btn_4 = models.IntegerField(blank=True, null=True)
    btn_5 = models.IntegerField(blank=True, null=True)
    btn_6 = models.IntegerField(blank=True, null=True)
    btn_7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remote'
        app_label = 'spaceedge'


class RemoteBlaster(models.Model):
    sid = models.AutoField(primary_key=True)
    fac_type = models.IntegerField()
    brand_id = models.IntegerField()
    remote_type = models.IntegerField(blank=True, null=True)
    btn_1 = models.IntegerField(blank=True, null=True)
    btn_2 = models.IntegerField(blank=True, null=True)
    btn_3 = models.IntegerField(blank=True, null=True)
    btn_4 = models.IntegerField(blank=True, null=True)
    btn_5 = models.IntegerField(blank=True, null=True)
    btn_6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remote_blaster'
        app_label = 'spaceedge'


class Room(models.Model):
    num = models.IntegerField()
    buse_name = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'room'
        app_label = 'spaceedge'


class Timer(models.Model):
    s_num = models.CharField(max_length=50)
    remote_id = models.IntegerField()
    use_flag = models.IntegerField()
    timer_type = models.IntegerField()
    off_time = models.DateTimeField()
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'timer'
        app_label = 'spaceedge'


class Weather(models.Model):
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
    regdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'weather'
        app_label = 'spaceedge'


class WeatherArea(models.Model):
    area_type = models.CharField(max_length=1)
    area_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=2, blank=True, null=True)
    dong_code = models.CharField(max_length=4, blank=True, null=True)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null=True)
    dong = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_area'
        app_label = 'spaceedge'
