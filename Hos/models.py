# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admission(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject = models.ForeignKey('Patients', on_delete=models.DO_NOTHING, db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    hadm_id = models.IntegerField(db_column='HADM_ID', unique=True)  # Field name made lowercase.
    admittime = models.CharField(db_column='ADMITTIME', max_length=50)  # Field name made lowercase.
    dischtime = models.CharField(db_column='DISCHTIME', max_length=50)  # Field name made lowercase.
    deathtime = models.CharField(db_column='DEATHTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    admission_type = models.CharField(db_column='ADMISSION_TYPE', max_length=50)  # Field name made lowercase.
    admission_location = models.CharField(db_column='ADMISSION_LOCATION', max_length=50)  # Field name made lowercase.
    discharge_location = models.CharField(db_column='DISCHARGE_LOCATION', max_length=50)  # Field name made lowercase.
    insurance = models.CharField(db_column='INSURANCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='LANGUAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='RELIGION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='MARITAL_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='ETHNICITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    edregtime = models.CharField(db_column='EDREGTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edouttime = models.CharField(db_column='EDOUTTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(db_column='DIAGNOSIS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hospital_expire_flag = models.IntegerField(db_column='HOSPITAL_EXPIRE_FLAG', blank=True, null=True)  # Field name made lowercase.
    has_chartevents_data = models.IntegerField(db_column='HAS_CHARTEVENTS_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admission'


class Caregiver(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    cgid = models.IntegerField(db_column='CGID', unique=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caregiver'


class Cpt(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject = models.ForeignKey('Patients', models.DO_NOTHING, db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    hadm = models.ForeignKey(Admission, models.DO_NOTHING, db_column='HADM_ID')  # Field name made lowercase.
    costcenter = models.CharField(db_column='COSTCENTER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chartdate = models.CharField(db_column='CHARTDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpt_cd = models.CharField(db_column='CPT_CD', max_length=10)  # Field name made lowercase.
    cpt_number = models.IntegerField(db_column='CPT_NUMBER', blank=True, null=True)  # Field name made lowercase.
    cpt_suffix = models.CharField(db_column='CPT_SUFFIX', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ticket_id_seq = models.IntegerField(db_column='TICKET_ID_SEQ', blank=True, null=True)  # Field name made lowercase.
    sectionheader = models.CharField(db_column='SECTIONHEADER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subsectionheader = models.CharField(db_column='SUBSECTIONHEADER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cpt'


class DCpt(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    category = models.SmallIntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    sectionrange = models.CharField(db_column='SECTIONRANGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sectionheader = models.CharField(db_column='SECTIONHEADER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subsectionrange = models.CharField(db_column='SUBSECTIONRANGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subsectionheader = models.CharField(db_column='SUBSECTIONHEADER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    codesuffix = models.CharField(db_column='CODESUFFIX', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mincodeinsubsection = models.IntegerField(db_column='MINCODEINSUBSECTION', blank=True, null=True)  # Field name made lowercase.
    maxcodeinsubsection = models.IntegerField(db_column='MAXCODEINSUBSECTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_cpt'


class DLabitems(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ITEMID', unique=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fluid = models.CharField(db_column='FLUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loinc_code = models.CharField(db_column='LOINC_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_labitems'


class Datatimeevent(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject = models.ForeignKey('Patients', on_delete=models.DO_NOTHING, db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    hadm = models.ForeignKey(Admission, models.DO_NOTHING, db_column='HADM_ID', blank=True, null=True)  # Field name made lowercase.
    icustay_id = models.IntegerField(db_column='ICUSTAY_ID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ITEMID', blank=True, null=True)  # Field name made lowercase.
    charttime = models.CharField(db_column='CHARTTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storetime = models.CharField(db_column='STORETIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cgid = models.ForeignKey('Caregiver', models.DO_NOTHING, db_column='CGID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valueuom = models.CharField(db_column='VALUEUOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warning = models.SmallIntegerField(db_column='WARNING', blank=True, null=True)  # Field name made lowercase.
    error = models.SmallIntegerField(db_column='ERROR', blank=True, null=True)  # Field name made lowercase.
    resultstatus = models.CharField(db_column='RESULTSTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stopped = models.CharField(db_column='STOPPED', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datatimeevent'


class Labevents(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    hadm_id = models.IntegerField(db_column='HADM_ID')  # Field name made lowercase.
    itemid = models.ForeignKey(DLabitems, models.DO_NOTHING, db_column='ITEMID', blank=True, null=True)  # Field name made lowercase.
    charttime = models.CharField(db_column='CHARTTIME', max_length=50)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    valuenum = models.FloatField(db_column='VALUENUM', blank=True, null=True)  # Field name made lowercase.
    valueuom = models.CharField(db_column='VALUEUOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='FLAG', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labevents'


class Patients(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID', unique=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(db_column='DOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dod = models.CharField(db_column='DOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dod_hosp = models.CharField(db_column='DOD_HOSP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dod_ssn = models.CharField(db_column='DOD_SSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expire_flag = models.CharField(db_column='EXPIRE_FLAG', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients'


class Prescriptions(models.Model):
    row_id = models.IntegerField(db_column='ROW_ID', primary_key=True)  # Field name made lowercase.
    subject = models.ForeignKey('Patients', on_delete=models.DO_NOTHING, db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    hadm = models.ForeignKey(Admission, models.DO_NOTHING, db_column='HADM_ID', blank=True, null=True)  # Field name made lowercase.
    icustay_id = models.IntegerField(db_column='ICUSTAY_ID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.CharField(db_column='STARTDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='ENDDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drug_type = models.CharField(db_column='DRUG_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    drug = models.CharField(db_column='DRUG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    drug_name_poe = models.CharField(db_column='DRUG_NAME_POE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    drug_name_generic = models.CharField(db_column='DRUG_NAME_GENERIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formulary_drug_cd = models.CharField(db_column='FORMULARY_DRUG_CD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    gsn = models.CharField(db_column='GSN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ndc = models.CharField(db_column='NDC', max_length=120, blank=True, null=True)  # Field name made lowercase.
    prod_strength = models.CharField(db_column='PROD_STRENGTH', max_length=120, blank=True, null=True)  # Field name made lowercase.
    dose_val_rx = models.CharField(db_column='DOSE_VAL_RX', max_length=120, blank=True, null=True)  # Field name made lowercase.
    dose_unit_rx = models.CharField(db_column='DOSE_UNIT_RX', max_length=120, blank=True, null=True)  # Field name made lowercase.
    form_val_disp = models.CharField(db_column='FORM_VAL_DISP', max_length=120, blank=True, null=True)  # Field name made lowercase.
    form_unit_disp = models.CharField(db_column='FORM_UNIT_DISP', max_length=120, blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriptions'
