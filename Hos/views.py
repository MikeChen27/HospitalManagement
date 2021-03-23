from django.shortcuts import render,HttpResponse
from django.db.models import Max
from Hos.models import Caregiver, Datatimeevent, DCpt, Patients, DLabitems, Labevents, Prescriptions, Cpt, Admission
import json
from django.http import JsonResponse,HttpResponseRedirect
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hospital.settings")   # project_name指项目名
django.setup()
from django.core import serializers
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
        if request.method == "GET":
            return render(request, 'login.html')
        if request.method == "POST":
            request_data = request.body
            request_dict = json.loads(request_data.decode('utf-8'))
            id_ = request_dict.get('id_')
            password = request_dict.get('password')
            if id_ == "admin"and password == "123456":
                data = {
                    'status': 0
                }
            else:
                data = {
                    'status': 1
                }
            return JsonResponse(data)


def search_pat(request):
        if request.method == "GET":
            return render(request, 'search_pat.html')
        if request.method == "POST":
            request_data = request.body
            request_dict = json.loads(request_data.decode('utf-8'))
            rid = request_dict.get('rid')
            sjid = request_dict.get('sjid')
            gd = request_dict.get('gd')
            dob = request_dict.get('dob')
            dod = request_dict.get('dod')
            dodh = request_dict.get('dodh')
            dods = request_dict.get('dods')
            ef = request_dict.get('ef')
            a = Patients.objects.all()
            if rid:
                rid = int(rid)
                a = a.filter(row_id=rid)
            if sjid:
                sjid = int(sjid)
                a = a.filter(subject_id=sjid)
            if gd:
                a = a.filter(gender=gd)
            if dob:
                a = a.filter(dob=dob)
            if dod:
                a = a.filter(dod=dod)
            if dodh:
                a = a.filter(dod_hosp=dodh)
            if dods:
                a = a.filter(dod_ssn=dods)
            if ef:
                a = a.filter(expire_flag=ef)
            patientList = list(a)
            dataList = [{} for i1 in range(len(patientList))]
            for i in range(len(patientList)):
                dataList[i].update(row_id=patientList[i].row_id)
                dataList[i].update(subject_id=patientList[i].subject_id)
                dataList[i].update(gender=patientList[i].gender)
                dataList[i].update(dob=patientList[i].dob)
                dataList[i].update(dod=patientList[i].dod)
                dataList[i].update(dod_hosp=patientList[i].dod_hosp)
                dataList[i].update(dod_ssn=patientList[i].dod_ssn)
                dataList[i].update(expire_flag=patientList[i].expire_flag)
            if patientList:
                data = {
                    'status': 0,
                    'patient': dataList
                }
            else:
                data = {
                    'status': 1
                }
            return JsonResponse(data)


def search_cg(request):
    if request.method == "GET":
        return render(request, 'search_cg.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        cgid = request_dict.get('cgid')
        lb = request_dict.get('lb')
        dsc = request_dict.get('dsc')
        a = Caregiver.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if cgid:
            cgid = int(cgid)
            a = a.filter(cgid=cgid)
        if lb:
            a = a.filter(label=lb)
        if dsc:
            a = a.filter(description=dsc)
        cgList = list(a)
        dataList = [{} for i1 in range(len(cgList))]
        for i in range(len(cgList)):
            dataList[i].update(row_id=cgList[i].row_id)
            dataList[i].update(cgid=cgList[i].cgid)
            dataList[i].update(label=cgList[i].label)
            dataList[i].update(description=cgList[i].description)
        if cgList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def search_adm(request):
    if request.method == "GET":
        return render(request, 'search_adm.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        admt = request_dict.get('admt')
        dcht = request_dict.get('dcht')
        dtht = request_dict.get('dtht')
        adm_t = request_dict.get('adm_t')
        adml = request_dict.get('adml')
        dscl = request_dict.get('dscl')
        ins = request_dict.get('ins')
        lg = request_dict.get('lg')
        rlg = request_dict.get('rlg')
        mts = request_dict.get('mts')
        eth = request_dict.get('eth')
        ert = request_dict.get('ert')
        eot = request_dict.get('eot')
        dgn = request_dict.get('dgn')
        hef = request_dict.get('hef')
        hcd = request_dict.get('hcd')
        a = Admission.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if admt:
            a = a.filter(admittime=admt)
        if dcht:
            a = a.filter(dischtime=dcht)
        if dtht:
            a = a.filter(deathtime=dtht)
        if adm_t:
            a = a.filter(admission_type=adm_t)
        if adml:
            a = a.filter(admission_location=adml)
        if dscl:
            a = a.filter(discharge_location=dscl)
        if ins:
            a = a.filter(insurance=ins)
        if lg:
            a = a.filter(language=lg)
        if rlg:
            a = a.filter(religion=rlg)
        if mts:
            a = a.filter(marital_status=mts)
        if eth:
            a = a.filter(ethnicity=eth)
        if ert:
            a = a.filter(edregtime=ert)
        if eot:
            a = a.filter(edouttime=eot)
        if dgn:
            a = a.filter(diagnosis=dgn)
        if hef:
            hef = int(hef)
            a = a.filter(hospital_expire_flag=hef)
        if hcd:
            hcd = int(hcd)
            a = a.filter(has_chartevents_data=hcd)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(admittime=admList[i].admittime)
            dataList[i].update(dischtime=admList[i].dischtime)
            dataList[i].update(deathtime=admList[i].deathtime)
            dataList[i].update(admission_type=admList[i].admission_type)
            dataList[i].update(admission_location=admList[i].admission_location)
            dataList[i].update(discharge_location=admList[i].discharge_location)
            dataList[i].update(insurance=admList[i].insurance)
            dataList[i].update(language=admList[i].language)
            dataList[i].update(religion=admList[i].religion)
            dataList[i].update(marital_status=admList[i].marital_status)
            dataList[i].update(ethnicity=admList[i].ethnicity)
            dataList[i].update(edregtime=admList[i].edregtime)
            dataList[i].update(edouttime=admList[i].edouttime)
            dataList[i].update(diagnosis=admList[i].diagnosis)
            dataList[i].update(hospital_expire_flag=admList[i].hospital_expire_flag)
            dataList[i].update(has_chartevents_data=admList[i].has_chartevents_data)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def search_cpt(request):
    if request.method == "GET":
        return render(request, 'search_cpt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        cc = request_dict.get('cc')
        cd = request_dict.get('cd')
        c_c = request_dict.get('c_c')
        cn = request_dict.get('cn')
        cs = request_dict.get('cs')
        tis = request_dict.get('tis')
        sh = request_dict.get('sh')
        ssh = request_dict.get('ssh')
        dsc = request_dict.get('dsc')

        a = Cpt.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if cc:
            a = a.filter(costcenter=cc)
        if cd:
            a = a.filter(chartdate=cd)
        if c_c:
            a = a.filter(cpt_cd=c_c)
        if cn:
            cn = int(cn)
            a = a.filter(cpt_number=cn)
        if cs:
            a = a.filter(cpt_suffix=cs)
        if tis:
            tis = int(tis)
            a = a.filter(ticket_id_seq=tis)
        if sh:
            a = a.filter(sectionheader=sh)
        if ssh:
            a = a.filter(subsectionheader=ssh)
        if dsc:
            a = a.filter(description=dsc)

        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(costcenter=admList[i].costcenter)
            dataList[i].update(chartdate=admList[i].chartdate)
            dataList[i].update(cpt_cd=admList[i].cpt_cd)
            dataList[i].update(cpt_number=admList[i].cpt_number)
            dataList[i].update(cpt_suffix=admList[i].cpt_suffix)
            dataList[i].update(ticket_id_seq=admList[i].ticket_id_seq)
            dataList[i].update(sectionheader=admList[i].sectionheader)
            dataList[i].update(subsectionheader=admList[i].subsectionheader)
            dataList[i].update(description=admList[i].description)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)
 
 
def search_dt(request):
    if request.method == "GET":
        return render(request, 'search_dt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        st = request_dict.get('st')
        cgid = request_dict.get('cgid')
        vl = request_dict.get('vl')
        vlm = request_dict.get('vlm')
        wn = request_dict.get('wn')
        er = request_dict.get('er')
        rs = request_dict.get('rs')
        stp = request_dict.get('stp')
        a = Datatimeevent.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if iid:
            iid = int(iid)
            a = a.filter(icustay_id=iid)
        if itid:
            itid = int(itid)
            a = a.filter(itemid=itid)
        if ct:
            a = a.filter(charttime=ct)
        if st:
            a = a.filter(storetime=st)
        if cgid:
            cgid = int(cgid)
            a = a.filter(cgid=cgid)
        if vl:
            a = a.filter(value=vl)
        if vlm:
            a = a.filter(valueuom=vlm)
        if wn:
            wn = int(wn)
            a = a.filter(warning=wn)
        if er:
            er = int(er)
            a = a.filter(error=er)
        if rs:
            a = a.filter(resultstatus=rs)
        if stp:
            a = a.filter(stopped=stp)
        
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(icustay_id=admList[i].icustay_id)
            dataList[i].update(itemid=admList[i].itemid)
            dataList[i].update(charttime=admList[i].charttime)
            dataList[i].update(storetime=admList[i].storetime)
            #dataList[i].update(cgid=admList[i].cgid)
            dataList[i].update(value=admList[i].value)
            dataList[i].update(valueuom=admList[i].valueuom)
            dataList[i].update(warning=admList[i].warning)
            dataList[i].update(error=admList[i].error)
            dataList[i].update(resultstatus=admList[i].resultstatus)
            dataList[i].update(stopped=admList[i].stopped)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def search_lab(request):
    if request.method == "GET":
        return render(request, 'search_lab.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        vl = request_dict.get('vl')
        vln = request_dict.get('vln')
        vlm = request_dict.get('vlm')
        fl = request_dict.get('fl')
        a = Labevents.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if itid:
            itid = int(itid)
            a = a.filter(itemid=itid)
        if ct:
            a = a.filter(charttime=ct)
        if vl:
            a = a.filter(value=vl)
        if vln:
            vln = float(vln)
            a = a.filter(valuenum=vln)
        if vlm:
            a = a.filter(valueuom=vlm)
        if fl:
            a = a.filter(flag=fl)

        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            #dataList[i].update(itemid=admList[i].itemid)
            dataList[i].update(charttime=admList[i].charttime)
            dataList[i].update(value=admList[i].value)
            dataList[i].update(valuenum=admList[i].valuenum)
            dataList[i].update(valueuom=admList[i].valueuom)
            dataList[i].update(flag=admList[i].flag)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)
    
    
def search_pre(request):
    if request.method == "GET":
        return render(request, 'search_pre.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        sd = request_dict.get('sd')
        ed = request_dict.get('ed')
        dt = request_dict.get('dt')
        dr = request_dict.get('dr')
        dnp = request_dict.get('dnp')
        dng = request_dict.get('dng')
        fdc = request_dict.get('fdc')
        gsn = request_dict.get('gsn')
        ndc = request_dict.get('ndc')
        ps = request_dict.get('ps')
        dvr = request_dict.get('dvr')
        dur = request_dict.get('dur')
        fvd = request_dict.get('fvd')
        fud = request_dict.get('fud')
        rt = request_dict.get('rt')
        a = Prescriptions.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if iid:
            iid = int(iid)
            a = a.filter(icustay_id=iid)
        if sd:
            a = a.filter(startdate=sd)
        if ed:
            a = a.filter(enddate=ed)
        if dt:
            a = a.filter(drug_type=dt)
        if dr:
            a = a.filter(drug=dr)
        if dnp:
            a = a.filter(drug_name_poe=dnp)
        if dng:
            a = a.filter(drug_name_generic=dng)
        if fdc:
            a = a.filter(formulary_drug_cd=fdc)
        if gsn:
            a = a.filter(gsn=gsn)
        if ndc:
            a = a.filter(ndc=ndc)
        if ps:
            a = a.filter(prod_strength=ps)
        if dvr:
            a = a.filter(dose_val_rx=dvr)
        if dur:
            a = a.filter(dose_unit_rx=dur)
        if fvd:
            a = a.filter(form_val_disp=fvd)
        if fud:
            a = a.filter(form_unit_disp=fud)
        if rt:
            a = a.filter(route=rt)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(icustay_id=admList[i].icustay_id)
            dataList[i].update(startdate=admList[i].startdate)
            dataList[i].update(enddate=admList[i].enddate)
            dataList[i].update(drug_type=admList[i].drug_type)
            dataList[i].update(drug=admList[i].drug)
            dataList[i].update(drug_name_poe=admList[i].drug_name_poe)
            dataList[i].update(drug_name_generic=admList[i].drug_name_generic)
            dataList[i].update(formulary_drug_cd=admList[i].formulary_drug_cd)
            dataList[i].update(gsn=admList[i].gsn)
            dataList[i].update(ndc=admList[i].ndc)
            dataList[i].update(prod_strength=admList[i].prod_strength)
            dataList[i].update(dose_val_rx=admList[i].dose_val_rx)
            dataList[i].update(dose_unit_rx=admList[i].dose_unit_rx)
            dataList[i].update(form_val_disp=admList[i].form_val_disp)
            dataList[i].update(form_unit_disp=admList[i].form_unit_disp)
            dataList[i].update(route=admList[i].route)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def del_adm(request):
    if request.method == "GET":
        return render(request, 'delete_adm.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        admt = request_dict.get('admt')
        dcht = request_dict.get('dcht')
        dtht = request_dict.get('dtht')
        adm_t = request_dict.get('adm_t')
        adml = request_dict.get('adml')
        dscl = request_dict.get('dscl')
        ins = request_dict.get('ins')
        lg = request_dict.get('lg')
        rlg = request_dict.get('rlg')
        mts = request_dict.get('mts')
        eth = request_dict.get('eth')
        ert = request_dict.get('ert')
        eot = request_dict.get('eot')
        dgn = request_dict.get('dgn')
        hef = request_dict.get('hef')
        hcd = request_dict.get('hcd')
        a = Admission.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if admt:
            a = a.filter(admittime=admt)
        if dcht:
            a = a.filter(dischtime=dcht)
        if dtht:
            a = a.filter(deathtime=dtht)
        if adm_t:
            a = a.filter(admission_type=adm_t)
        if adml:
            a = a.filter(admission_location=adml)
        if dscl:
            a = a.filter(discharge_location=dscl)
        if ins:
            a = a.filter(insurance=ins)
        if lg:
            a = a.filter(language=lg)
        if rlg:
            a = a.filter(religion=rlg)
        if mts:
            a = a.filter(marital_status=mts)
        if eth:
            a = a.filter(ethnicity=eth)
        if ert:
            a = a.filter(edregtime=ert)
        if eot:
            a = a.filter(edouttime=eot)
        if dgn:
            a = a.filter(diagnosis=dgn)
        if hef:
            hef = int(hef)
            a = a.filter(hospital_expire_flag=hef)
        if hcd:
            hcd = int(hcd)
            a = a.filter(has_chartevents_data=hcd)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(admittime=admList[i].admittime)
            dataList[i].update(dischtime=admList[i].dischtime)
            dataList[i].update(deathtime=admList[i].deathtime)
            dataList[i].update(admission_type=admList[i].admission_type)
            dataList[i].update(admission_location=admList[i].admission_location)
            dataList[i].update(discharge_location=admList[i].discharge_location)
            dataList[i].update(insurance=admList[i].insurance)
            dataList[i].update(language=admList[i].language)
            dataList[i].update(religion=admList[i].religion)
            dataList[i].update(marital_status=admList[i].marital_status)
            dataList[i].update(ethnicity=admList[i].ethnicity)
            dataList[i].update(edregtime=admList[i].edregtime)
            dataList[i].update(edouttime=admList[i].edouttime)
            dataList[i].update(diagnosis=admList[i].diagnosis)
            dataList[i].update(hospital_expire_flag=admList[i].hospital_expire_flag)
            dataList[i].update(has_chartevents_data=admList[i].has_chartevents_data)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_cpt(request):
    if request.method == "GET":
        return render(request, 'delete_cpt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        cc = request_dict.get('cc')
        cd = request_dict.get('cd')
        c_c = request_dict.get('c_c')
        cn = request_dict.get('cn')
        cs = request_dict.get('cs')
        tis = request_dict.get('tis')
        sh = request_dict.get('sh')
        ssh = request_dict.get('ssh')
        dsc = request_dict.get('dsc')
        a = Cpt.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if cc:
            a = a.filter(costcenter=cc)
        if cd:
            a = a.filter(chartdate=cd)
        if c_c:
            a = a.filter(cpt_cd=c_c)
        if cn:
            cn = int(cn)
            a = a.filter(cpt_number=cn)
        if cs:
            a = a.filter(cpt_suffix=cs)
        if tis:
            tis = int(tis)
            a = a.filter(ticket_id_seq=tis)
        if sh:
            a = a.filter(sectionheader=sh)
        if ssh:
            a = a.filter(subsectionheader=ssh)
        if dsc:
            a = a.filter(description=dsc)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(costcenter=admList[i].costcenter)
            dataList[i].update(chartdate=admList[i].chartdate)
            dataList[i].update(cpt_cd=admList[i].cpt_cd)
            dataList[i].update(cpt_number=admList[i].cpt_number)
            dataList[i].update(cpt_suffix=admList[i].cpt_suffix)
            dataList[i].update(ticket_id_seq=admList[i].ticket_id_seq)
            dataList[i].update(sectionheader=admList[i].sectionheader)
            dataList[i].update(subsectionheader=admList[i].subsectionheader)
            dataList[i].update(description=admList[i].description)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_dt(request):
    if request.method == "GET":
        return render(request, 'delete_dt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        st = request_dict.get('st')
        cgid = request_dict.get('cgid')
        vl = request_dict.get('vl')
        vlm = request_dict.get('vlm')
        wn = request_dict.get('wn')
        er = request_dict.get('er')
        rs = request_dict.get('rs')
        stp = request_dict.get('stp')
        a = Datatimeevent.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if iid:
            iid = int(iid)
            a = a.filter(icustay_id=iid)
        if itid:
            itid = int(itid)
            a = a.filter(itemid=itid)
        if ct:
            a = a.filter(charttime=ct)
        if st:
            a = a.filter(storetime=st)
        if cgid:
            cgid = int(cgid)
            a = a.filter(cgid=cgid)
        if vl:
            a = a.filter(value=vl)
        if vlm:
            a = a.filter(valueuom=vlm)
        if wn:
            wn = int(wn)
            a = a.filter(warning=wn)
        if er:
            er = int(er)
            a = a.filter(error=er)
        if rs:
            a = a.filter(resultstatus=rs)
        if stp:
            a = a.filter(stopped=stp)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(icustay_id=admList[i].icustay_id)
            dataList[i].update(itemid=admList[i].itemid)
            dataList[i].update(charttime=admList[i].charttime)
            dataList[i].update(storetime=admList[i].storetime)
            #dataList[i].update(cgid=admList[i].cgid)
            dataList[i].update(value=admList[i].value)
            dataList[i].update(valueuom=admList[i].valueuom)
            dataList[i].update(warning=admList[i].warning)
            dataList[i].update(error=admList[i].error)
            dataList[i].update(resultstatus=admList[i].resultstatus)
            dataList[i].update(stopped=admList[i].stopped)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_lab(request):
    if request.method == "GET":
        return render(request, 'delete_lab.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        vl = request_dict.get('vl')
        vln = request_dict.get('vln')
        vlm = request_dict.get('vlm')
        fl = request_dict.get('fl')
        a = Labevents.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if itid:
            itid = int(itid)
            a = a.filter(itemid=itid)
        if ct:
            a = a.filter(charttime=ct)
        if vl:
            a = a.filter(value=vl)
        if vln:
            vln = float(vln)
            a = a.filter(valuenum=vln)
        if vlm:
            a = a.filter(valueuom=vlm)
        if fl:
            a = a.filter(flag=fl)

        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            #dataList[i].update(itemid=admList[i].itemid)
            dataList[i].update(charttime=admList[i].charttime)
            dataList[i].update(value=admList[i].value)
            dataList[i].update(valuenum=admList[i].valuenum)
            dataList[i].update(valueuom=admList[i].valueuom)
            dataList[i].update(flag=admList[i].flag)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_pat(request):
    if request.method == "GET":
        return render(request, 'delete_pat.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        gd = request_dict.get('gd')
        dob = request_dict.get('dob')
        dod = request_dict.get('dod')
        dodh = request_dict.get('dodh')
        dods = request_dict.get('dods')
        ef = request_dict.get('ef')
        a = Patients.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if gd:
            a = a.filter(gender=gd)
        if dob:
            a = a.filter(dob=dob)
        if dod:
            a = a.filter(dod=dod)
        if dodh:
            a = a.filter(dod_hosp=dodh)
        if dods:
            a = a.filter(dod_ssn=dods)
        if ef:
            a = a.filter(expire_flag=ef)
        patientList = list(a)
        dataList = [{} for i1 in range(len(patientList))]
        for i in range(len(patientList)):
            dataList[i].update(row_id=patientList[i].row_id)
            dataList[i].update(subject_id=patientList[i].subject_id)
            dataList[i].update(gender=patientList[i].gender)
            dataList[i].update(dob=patientList[i].dob)
            dataList[i].update(dod=patientList[i].dod)
            dataList[i].update(dod_hosp=patientList[i].dod_hosp)
            dataList[i].update(dod_ssn=patientList[i].dod_ssn)
            dataList[i].update(expire_flag=patientList[i].expire_flag)
        if patientList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_cg(request):
    if request.method == "GET":
        return render(request, 'delete_cg.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        cgid = request_dict.get('cgid')
        lb = request_dict.get('lb')
        dsc = request_dict.get('dsc')
        a = Caregiver.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if cgid:
            cgid = int(cgid)
            a = a.filter(cgid=cgid)
        if lb:
            a = a.filter(label=lb)
        if dsc:
            a = a.filter(description=dsc)
        cgList = list(a)
        dataList = [{} for i1 in range(len(cgList))]
        for i in range(len(cgList)):
            dataList[i].update(row_id=cgList[i].row_id)
            dataList[i].update(cgid=cgList[i].cgid)
            dataList[i].update(label=cgList[i].label)
            dataList[i].update(description=cgList[i].description)
        if cgList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def del_pre(request):
    if request.method == "GET":
        return render(request, 'delete_pre.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = request_dict.get('rid')
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        sd = request_dict.get('sd')
        ed = request_dict.get('ed')
        dt = request_dict.get('dt')
        dr = request_dict.get('dr')
        dnp = request_dict.get('dnp')
        dng = request_dict.get('dng')
        fdc = request_dict.get('fdc')
        gsn = request_dict.get('gsn')
        ndc = request_dict.get('ndc')
        ps = request_dict.get('ps')
        dvr = request_dict.get('dvr')
        dur = request_dict.get('dur')
        fvd = request_dict.get('fvd')
        fud = request_dict.get('fud')
        rt = request_dict.get('rt')
        a = Prescriptions.objects.all()
        if rid:
            rid = int(rid)
            a = a.filter(row_id=rid)
        if sjid:
            sjid = int(sjid)
            a = a.filter(subject_id=sjid)
        if hid:
            hid = int(hid)
            a = a.filter(hadm_id=hid)
        if iid:
            iid = int(iid)
            a = a.filter(icustay_id=iid)
        if sd:
            a = a.filter(startdate=sd)
        if ed:
            a = a.filter(enddate=ed)
        if dt:
            a = a.filter(drug_type=dt)
        if dr:
            a = a.filter(drug=dr)
        if dnp:
            a = a.filter(drug_name_poe=dnp)
        if dng:
            a = a.filter(drug_name_generic=dng)
        if fdc:
            a = a.filter(formulary_drug_cd=fdc)
        if gsn:
            a = a.filter(gsn=gsn)
        if ndc:
            a = a.filter(ndc=ndc)
        if ps:
            a = a.filter(prod_strength=ps)
        if dvr:
            a = a.filter(dose_val_rx=dvr)
        if dur:
            a = a.filter(dose_unit_rx=dur)
        if fvd:
            a = a.filter(form_val_disp=fvd)
        if fud:
            a = a.filter(form_unit_disp=fud)
        if rt:
            a = a.filter(route=rt)
        admList = list(a)
        dataList = [{} for i1 in range(len(admList))]
        for i in range(len(admList)):
            dataList[i].update(row_id=admList[i].row_id)
            dataList[i].update(subject_id=admList[i].subject_id)
            dataList[i].update(hadm_id=admList[i].hadm_id)
            dataList[i].update(icustay_id=admList[i].icustay_id)
            dataList[i].update(startdate=admList[i].startdate)
            dataList[i].update(enddate=admList[i].enddate)
            dataList[i].update(drug_type=admList[i].drug_type)
            dataList[i].update(drug=admList[i].drug)
            dataList[i].update(drug_name_poe=admList[i].drug_name_poe)
            dataList[i].update(drug_name_generic=admList[i].drug_name_generic)
            dataList[i].update(formulary_drug_cd=admList[i].formulary_drug_cd)
            dataList[i].update(gsn=admList[i].gsn)
            dataList[i].update(ndc=admList[i].ndc)
            dataList[i].update(prod_strength=admList[i].prod_strength)
            dataList[i].update(dose_val_rx=admList[i].dose_val_rx)
            dataList[i].update(dose_unit_rx=admList[i].dose_unit_rx)
            dataList[i].update(form_val_disp=admList[i].form_val_disp)
            dataList[i].update(form_unit_disp=admList[i].form_unit_disp)
            dataList[i].update(route=admList[i].route)
        if admList:
            data = {
                'status': 0,
                'patient': dataList
            }
        else:
            data = {
                'status': 1
            }
        a.delete()
        return JsonResponse(data)


def edit_pat(request):
    if request.method == "GET":
        return render(request, 'edit_pat.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        gd = request_dict.get('gd')
        dob = request_dict.get('dob')
        dod = request_dict.get('dod')
        dodh = request_dict.get('dodh')
        dods = request_dict.get('dods')
        ef = request_dict.get('ef')
        edtData = Patients.objects.filter(row_id=rid)
        if edtData:
            if sjid:
                sjid = int(sjid)
                edtData.update(subject_id=sjid)
            if gd:
                edtData.update(gender=gd)
            if dob:
                edtData.update(dob=dob)
            if dod:
                edtData.update(dod=dod)
            if dodh:
                edtData.update(dod_hosp=dodh)
            if dods:
                edtData.update(dod_ssn=dods)
            if ef:
                edtData.update(expire_flag=ef)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def edit_cg(request):
    if request.method == "GET":
        return render(request, 'edit_cg.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        cgid = int(request_dict.get('cgid'))
        lb = request_dict.get('lb')
        dsc = request_dict.get('dsc')
        print(rid)
        edtData = Caregiver.objects.filter(row_id=rid)
        if edtData:
            if cgid:
                edtData.update(cgid=cgid)
            if lb:
                edtData.update(label=lb)
            if dsc:
                edtData.update(description=dsc)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)
    
    
def edit_adm(request):
    if request.method == "GET":
        return render(request, 'edit_adm.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        admt = request_dict.get('admt')
        dcht = request_dict.get('dcht')
        dtht = request_dict.get('dtht')
        adm_t = request_dict.get('adm_t')
        adml = request_dict.get('adml')
        dscl = request_dict.get('dscl')
        ins = request_dict.get('ins')
        lg = request_dict.get('lg')
        rlg = request_dict.get('rlg')
        mts = request_dict.get('mts')
        eth = request_dict.get('eth')
        ert = request_dict.get('ert')
        eot = request_dict.get('eot')
        dgn = request_dict.get('dgn')
        hef = request_dict.get('hef')
        hcd = request_dict.get('hcd')
        edtData = Admission.objects.filter(row_id=rid)
        if edtData:
            if sjid:
                sjid = int(sjid)
                edtData.update(subject_id=sjid)
            if hid:
                hid = int(hid)
                edtData.update(hadm_id=hid)
            if admt:
                edtData.update(admittime=admt)
            if dcht:
                edtData.update(dischtime=dcht)
            if dtht:
                edtData.update(deathtime=dtht)
            if adm_t:
                edtData.update(admission_type=adm_t)
            if adml:
                edtData.update(admission_location=adml)
            if dscl:
                edtData.update(discharge_location=dscl)
            if ins:
                edtData.update(insurance=ins)
            if lg:
                edtData.update(language=lg)
            if rlg:
                edtData.update(religion=rlg)
            if mts:
                edtData.update(marital_status=mts)
            if eth:
                edtData.update(ethnicity=eth)
            if ert:
                edtData.update(edregtime=ert)
            if eot:
                edtData.update(edouttime=eot)
            if dgn:
                edtData.update(diagnosis=dgn)
            if hef:
                hef = int(hef)
                edtData.update(hospital_expire_flag=hef)
            if hcd:
                hcd = int(hcd)
                edtData.update(has_chartevents_data=hcd)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)
    
    
def edit_cpt(request):
    if request.method == "GET":
        return render(request, 'edit_cpt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        cc = request_dict.get('cc')
        cd = request_dict.get('cd')
        c_c = request_dict.get('c_c')
        cn = request_dict.get('cn')
        cs = request_dict.get('cs')
        tis = request_dict.get('tis')
        sh = request_dict.get('sh')
        ssh = request_dict.get('ssh')
        dsc = request_dict.get('dsc')
        edtData = Cpt.objects.filter(row_id=rid)
        if edtData:
            if rid:
                rid = int(rid)
                edtData.update(row_id=rid)
            if sjid:
                sjid = int(sjid)
                edtData.update(subject_id=sjid)
            if hid:
                hid = int(hid)
                edtData.update(hadm_id=hid)
            if cc:
                edtData.update(costcenter=cc)
            if cd:
                edtData.update(chartdate=cd)
            if c_c:
                edtData.update(cpt_cd=c_c)
            if cn:
                cn = int(cn)
                edtData.update(cpt_number=cn)
            if cs:
                edtData.update(cpt_suffix=cs)
            if tis:
                tis = int(tis)
                edtData.update(ticket_id_seq=tis)
            if sh:
                edtData.update(sectionheader=sh)
            if ssh:
                edtData.update(subsectionheader=ssh)
            if dsc:
                edtData.update(description=dsc)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def edit_dt(request):
    if request.method == "GET":
        return render(request, 'edit_dt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        st = request_dict.get('st')
        cgid = request_dict.get('cgid')
        vl = request_dict.get('vl')
        vlm = request_dict.get('vlm')
        wn = request_dict.get('wn')
        er = request_dict.get('er')
        rs = request_dict.get('rs')
        stp = request_dict.get('stp')
        edtData = Datatimeevent.objects.filter(row_id=rid)
        if edtData:
            a = edtData
            if sjid:
                sjid = int(sjid)
                a = a.update(subject_id=sjid)
            if hid:
                hid = int(hid)
                a = a.update(hadm_id=hid)
            if iid:
                iid = int(iid)
                a = a.update(icustay_id=iid)
            if itid:
                itid = int(itid)
                a = a.update(itemid=itid)
            if ct:
                a = a.update(charttime=ct)
            if st:
                a = a.update(storetime=st)
            if cgid:
                cgid = int(cgid)
                a = a.update(cgid=cgid)
            if vl:
                a = a.update(value=vl)
            if vlm:
                a = a.update(valueuom=vlm)
            if wn:
                wn = int(wn)
                a = a.update(warning=wn)
            if er:
                er = int(er)
                a = a.update(error=er)
            if rs:
                a = a.update(resultstatus=rs)
            if stp:
                a = a.update(stopped=stp)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def edit_lab(request):
    if request.method == "GET":
        return render(request, 'edit_lab.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        vl = request_dict.get('vl')
        vln = request_dict.get('vln')
        vlm = request_dict.get('vlm')
        fl = request_dict.get('fl')
        edtData = Labevents.objects.filter(row_id=rid)
        if edtData:
            a = edtData
            if sjid:
                sjid = int(sjid)
                a = a.update(subject_id=sjid)
            if hid:
                hid = int(hid)
                a = a.update(hadm_id=hid)
            if itid:
                itid = int(itid)
                a = a.update(itemid=itid)
            if ct:
                a = a.update(charttime=ct)
            if vl:
                a = a.update(value=vl)
            if vln:
                vln = float(vln)
                a = a.update(valuenum=vln)
            if vlm:
                a = a.update(valueuom=vlm)
            if fl:
                a = a.update(flag=fl)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def edit_pre(request):
    if request.method == "GET":
        return render(request, 'edit_pre.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        rid = int(request_dict.get('rid'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        sd = request_dict.get('sd')
        ed = request_dict.get('ed')
        dt = request_dict.get('dt')
        dr = request_dict.get('dr')
        dnp = request_dict.get('dnp')
        dng = request_dict.get('dng')
        fdc = request_dict.get('fdc')
        gsn = request_dict.get('gsn')
        ndc = request_dict.get('ndc')
        ps = request_dict.get('ps')
        dvr = request_dict.get('dvr')
        dur = request_dict.get('dur')
        fvd = request_dict.get('fvd')
        fud = request_dict.get('fud')
        rt = request_dict.get('rt')
        edtData = Prescriptions.objects.filter(row_id=rid)
        a = edtData
        if a:
            if sjid:
                sjid = int(sjid)
                a = a.update(subject_id=sjid)
            if hid:
                hid = int(hid)
                a = a.update(hadm_id=hid)
            if iid:
                iid = int(iid)
                a = a.update(icustay_id=iid)
            if sd:
                a = a.update(startdate=sd)
            if ed:
                a = a.update(enddate=ed)
            if dt:
                a = a.update(drug_type=dt)
            if dr:
                a = a.update(drug=dr)
            if dnp:
                a = a.update(drug_name_poe=dnp)
            if dng:
                a = a.update(drug_name_generic=dng)
            if fdc:
                a = a.update(formulary_drug_cd=fdc)
            if gsn:
                a = a.update(gsn=gsn)
            if ndc:
                a = a.update(ndc=ndc)
            if ps:
                a = a.update(prod_strength=ps)
            if dvr:
                a = a.update(dose_val_rx=dvr)
            if dur:
                a = a.update(dose_unit_rx=dur)
            if fvd:
                a = a.update(form_val_disp=fvd)
            if fud:
                a = a.update(form_unit_disp=fud)
            if rt:
                a = a.update(route=rt)
            data = {
                'status': 0
            }
        else:
            data = {
                'status': 1
            }
        return JsonResponse(data)


def add_pat(request):
    if request.method == "GET":
        return render(request, 'add_pat.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = int(request_dict.get('sjid'))
        gd = request_dict.get('gd')
        dob = request_dict.get('dob')
        dod = request_dict.get('dod')
        dodh = request_dict.get('dodh')
        dods = request_dict.get('dods')
        ef = request_dict.get('ef')
        addData = Patients.objects.filter(subject_id=sjid)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Patients.objects.all()
            max_ = row.aggregate(Max('row_id'))
            obj = Patients.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, gender=gd, dob=dob, dod=dod, dod_hosp=dodh, dod_ssn=dods, expire_flag=ef)
            data = {
                'status': 0,
                'row_id': obj.row_id
            }
        return JsonResponse(data)


def add_cg(request):
    if request.method == "GET":
        return render(request, 'add_cg.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        cgid = int(request_dict.get('cgid'))
        lb = request_dict.get('lb')
        dsc = request_dict.get('dsc')
        addData = Caregiver.objects.filter(cgid=cgid)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Caregiver.objects.all()
            max_ = row.aggregate(Max('row_id'))
            obj = Caregiver.objects.create(row_id=max_['row_id__max']+1, cgid=cgid, label=lb, description=dsc)
            data = {
                'status': 0,
                'row_id': obj.row_id
            }
        return JsonResponse(data)


def add_adm(request):
    if request.method == "GET":
        return render(request, 'add_adm.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        admt = request_dict.get('admt')
        dcht = request_dict.get('dcht')
        dtht = request_dict.get('dtht')
        adm_t = request_dict.get('adm_t')
        adml = request_dict.get('adml')
        dscl = request_dict.get('dscl')
        ins = request_dict.get('ins')
        lg = request_dict.get('lg')
        rlg = request_dict.get('rlg')
        mts = request_dict.get('mts')
        eth = request_dict.get('eth')
        ert = request_dict.get('ert')
        eot = request_dict.get('eot')
        dgn = request_dict.get('dgn')
        hef = request_dict.get('hef')
        hcd = request_dict.get('hcd')
        if sjid:
            sjid = int(sjid)
        else:
            sjid = None
        if hid:
            hid = int(hid)
        else:
            hid = None
        if hef:
            hef = int(hef)
        else:
            hef = None
        if hcd:
            hcd = int(hcd)
        else:
            hcd = None
        addData = Admission.objects.filter(hadm_id=hid)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Admission.objects.all()
            max_ = row.aggregate(Max('row_id'))
            Admission.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, hadm_id=hid, admittime=admt, dischtime=dcht, deathtime=dtht, admission_type=adm_t, admission_location=adml, discharge_location=dscl, insurance=ins, language=lg, religion=rlg, marital_status=mts, ethnicity=eth, edregtime=ert, edouttime=eot, diagnosis=dgn, hospital_expire_flag=hef, has_chartevents_data=hcd)
            data = {
                'status': 0
            }
        return JsonResponse(data)


def add_cpt(request):
    if request.method == "GET":
        return render(request, 'add_cpt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        cc = request_dict.get('cc')
        cd = request_dict.get('cd')
        c_c = request_dict.get('c_c')
        cn = request_dict.get('cn')
        cs = request_dict.get('cs')
        tis = request_dict.get('tis')
        sh = request_dict.get('sh')
        ssh = request_dict.get('ssh')
        dsc = request_dict.get('dsc')
        if sjid:
            sjid = int(sjid)
        else:
            sjid = None
        if hid:
            hid = int(hid)
        else:
            hid = None
        if cn:
            cn = int(cn)
        else:
            cn = None
        if tis:
            tis = int(tis)
        else:
            tis = None
        addData = Cpt.objects.filter(subject_id=sjid, hadm_id=hid, costcenter=cc, chartdate=cd, cpt_cd=c_c, cpt_number=cn, cpt_suffix=cs, ticket_id_seq=tis, sectionheader=sh, subsectionheader=ssh, description=dsc)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Cpt.objects.all()
            max_ = row.aggregate(Max('row_id'))
            Cpt.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, hadm_id=hid, costcenter=cc, chartdate=cd, cpt_cd=c_c, cpt_number=cn, cpt_suffix=cs, ticket_id_seq=tis, sectionheader=sh, subsectionheader=ssh, description=dsc)
            data = {
                'status': 0
            }
        return JsonResponse(data)


def add_dt(request):
    if request.method == "GET":
        return render(request, 'add_dt.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        st = request_dict.get('st')
        cgid = request_dict.get('cgid')
        vl = request_dict.get('vl')
        vlm = request_dict.get('vlm')
        wn = request_dict.get('wn')
        er = request_dict.get('er')
        rs = request_dict.get('rs')
        stp = request_dict.get('stp')
        if sjid:
            sjid = int(sjid)
        else:
            sjid = None
        if hid:
            hid = int(hid)
        else:
            hid = None
        if iid:
            iid = int(iid)
        else:
            iid = None
        if cgid:
            cgid = int(cgid)
        else:
            cgid = None
        if wn:
            wn = int(wn)
        else:
            wn = None
        if er:
            er = int(er)
        else:
            er = None
        addData = Datatimeevent.objects.filter(subject_id=sjid, hadm_id=hid, icustay_id=iid, itemid=itid, charttime=ct, storetime=st, cgid=cgid, value=vl, valueuom=vlm, warning=wn, error=er, resultstatus=rs, stopped=stp)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Datatimeevent.objects.all()
            max_ = row.aggregate(Max('row_id'))
            Datatimeevent.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, hadm_id=hid, icustay_id=iid, itemid=itid, charttime=ct, storetime=st, cgid=cgid, value=vl, valueuom=vlm, warning=wn, error=er, resultstatus=rs, stopped=stp)
            data = {
                'status': 0
            }
        return JsonResponse(data)


def add_lab(request):
    if request.method == "GET":
        return render(request, 'add_lab.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        itid = request_dict.get('itid')
        ct = request_dict.get('ct')
        vl = request_dict.get('vl')
        vln = request_dict.get('vln')
        vlm = request_dict.get('vlm')
        fl = request_dict.get('fl')
        if sjid:
            sjid = int(sjid)
        else:
            sjid = None
        if hid:
            hid = int(hid)
        else:
            hid = None
        if itid:
            itid = int(itid)
        else:
            itid = None
        if vln:
            vln = float(vln)
        else:
            vln = None
        addData = Labevents.objects.filter(subject_id=sjid, hadm_id=hid, itemid=itid, charttime=ct, value=vl, valuenum=vln, valueuom=vlm, flag=fl)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Labevents.objects.all()
            max_ = row.aggregate(Max('row_id'))
            Labevents.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, hadm_id=hid, itemid=itid, charttime=ct, value=vl, valuenum=vln, valueuom=vlm, flag=fl)
            data = {
                'status': 0
            }
        return JsonResponse(data)


def add_pre(request):
    if request.method == "GET":
        return render(request, 'add_pre.html')
    if request.method == "POST":
        request_data = request.body
        request_dict = json.loads(request_data.decode('utf-8'))
        sjid = request_dict.get('sjid')
        hid = request_dict.get('hid')
        iid = request_dict.get('iid')
        sd = request_dict.get('sd')
        ed = request_dict.get('ed')
        dt = request_dict.get('dt')
        dr = request_dict.get('dr')
        dnp = request_dict.get('dnp')
        dng = request_dict.get('dng')
        fdc = request_dict.get('fdc')
        gsn = request_dict.get('gsn')
        ndc = request_dict.get('ndc')
        ps = request_dict.get('ps')
        dvr = request_dict.get('dvr')
        dur = request_dict.get('dur')
        fvd = request_dict.get('fvd')
        fud = request_dict.get('fud')
        rt = request_dict.get('rt')
        if sjid:
            sjid = int(sjid)
        else:
            sjid = None
        if hid:
            hid = int(hid)
        else:
            hid = None
        if iid:
            iid = int(iid)
        else:
            iid = None
        addData = Prescriptions.objects.filter(subject_id=sjid, hadm_id=hid, icustay_id=iid, startdate=sd, enddate=ed, drug_type=dt, drug=dr, drug_name_poe=dnp, drug_name_generic=dng, formulary_drug_cd=fdc, gsn=gsn, ndc=ndc, prod_strength=ps, dose_val_rx=dvr, dose_unit_rx=dur, form_val_disp=fvd, form_unit_disp=fud, route=rt)
        if addData:
            data = {
                'status': 1
            }
        else:
            row = Prescriptions.objects.all()
            max_ = row.aggregate(Max('row_id'))
            Prescriptions.objects.create(row_id=max_['row_id__max']+1, subject_id=sjid, hadm_id=hid, icustay_id=iid, startdate=sd, enddate=ed, drug_type=dt, drug=dr, drug_name_poe=dnp, drug_name_generic=dng, formulary_drug_cd=fdc, gsn=gsn, ndc=ndc, prod_strength=ps, dose_val_rx=dvr, dose_unit_rx=dur, form_val_disp=fvd, form_unit_disp=fud, route=rt)
            data = {
                'status': 0
            }
        return JsonResponse(data)
