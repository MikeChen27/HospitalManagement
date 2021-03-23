var jq=jQuery.noConflict();
jq(document).ready( function(jq) {

    jq('#del_pat').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#gd').val();
        d = jq('#dob').val();
        e = jq('#dod').val();
        f = jq('#dodh').val();
        g = jq('#dods').val();
        h = jq('#ef').val();
        if(a||b||c||d||e||f||g||h){
            jq.ajax({
                url: '/delete/patient/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                gd: c,
                dob:d,
                dod:e,
                dodh:f,
                dods:g,
                ef:h
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['gender'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dob'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dod'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dod_hosp'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dod_ssn'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['expire_flag'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert("Delete Success");
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_cg').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#cgid').val();
        c = jq('#lb').val();
        d = jq('#dsc').val();
        if(a||b||c||d){
            jq.ajax({
                url: '/delete/caregiver/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                cgid: b,
                lb: c,
                dsc: d
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['cgid'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['label'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['description'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert("Delete Success");
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_adm').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#hid').val(),
        d = jq('#admt').val();
        e = jq('#dcht').val();
        f = jq('#dtht').val();
        g = jq('#adm_t').val();
        h = jq('#adml').val();
        i = jq('#dscl').val();
        j = jq('#ins').val();
        k = jq('#lg').val();
        l = jq('#rlg').val();
        m = jq('#mts').val();
        n = jq('#eth').val();
        o = jq('#ert').val();
        p = jq('#eot').val();
        q = jq('#dgn').val();
        r = jq('#hef').val();
        s = jq('#hcd').val()
        if(a||b||c||d||e||f||g||h||i||j||k||l||m||n||o||p||q||r||s){
            jq.ajax({
                url: '/delete/admission/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                hid: c,
                admt: d,
                dcht:e,
                dtht:f,
                adm_t:g,
                adml:h,
                dscl:i,
                ins:j,
                lg:k,
                rlg:l,
                mts:m,
                eth:n,
                ert:o,
                eot:p,
                dgn:q,
                hef:r,
                hcd:s
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hadm_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['admittime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dischtime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['deathtime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['admission_type'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['admission_location'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['discharge_location'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['insurance'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['language'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['religion'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['marital_status'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['ethnicity'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['edregtime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['edouttime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['diagnosis'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hospital_expire_flag'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['has_chartevents_data'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert('Delete Success')
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_cpt').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#hid').val();
        d = jq('#cc').val();
        e = jq('#cd').val();
        f = jq('#c_c').val();
        g = jq('#cn').val();
        h = jq('#cs').val();
        i = jq('#tis').val();
        j = jq('#sh').val();
        k = jq('#ssh').val();
        l = jq('#dsc').val();
        if(a||b||c||d||e||f||g||h||i||j||k||l){
            jq.ajax({
                url: '/delete/cpt/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                hid: c,
                cc:d,
                cd:e,
                c_c:f,
                cn:g,
                cs:h,
                tis:i,
                sh:j,
                ssh:k,
                dsc:l
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hadm_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['costcenter'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['chartdate'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['cpt_cd'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['cpt_number'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['cpt_suffix'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['ticket_id_seq'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['sectionheader'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subsectionheader'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['description'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert('Delete Success')
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_pre').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#hid').val(),
        d = jq('#iid').val();
        e = jq('#sd').val();
        f = jq('#ed').val();
        g = jq('#dt').val();
        h = jq('#dr').val();
        i = jq('#dnp').val();
        j = jq('#dng').val();
        k = jq('#fdc').val();
        l = jq('#gsn').val();
        m = jq('#ndc').val();
        n = jq('#ps').val();
        o = jq('#dvr').val();
        p = jq('#dur').val();
        q = jq('#fvd').val();
        r = jq('#fud').val();
        s = jq('#rt').val()
        if(a||b||c||d||e||f||g||h||i||j||k||l||m||n||o||p||q||r||s){
            jq.ajax({
                url: '/delete/prescription/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                hid: c,
                iid: d,
                sd:e,
                ed:f,
                dt:g,
                dr:h,
                dnp:i,
                dng:j,
                fdc:k,
                gsn:l,
                ndc:m,
                ps:n,
                dvr:o,
                dur:p,
                fvd:q,
                fud:r,
                rt:s
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hadm_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['icustay_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['startdate'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['enddate'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['drug_type'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['drug'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['drug_name_poe'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['drug_name_generic'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['formulary_drug_cd'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['gsn'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['ndc'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['prod_strength'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dose_val_rx'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['dose_unit_rx'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['form_val_disp'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['form_unit_disp'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['route'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert('Delete Success')
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_dt').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#hid').val(),
        d = jq('#iid').val();
        e = jq('#itid').val();
        f = jq('#ct').val();
        g = jq('#st').val();
        h = jq('#cgid').val();
        i = jq('#vl').val();
        j = jq('#vlm').val();
        k = jq('#wn').val();
        l = jq('#er').val();
        m = jq('#rs').val();
        n = jq('#stp').val();
        if(a||b||c||d||e||f||g||h||i||j||k||l||m||n){
            jq.ajax({
                url: '/delete/datatimeevent/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                hid: c,
                iid: d,
                itid:e,
                ct:f,
                st:g,
                cgid:h,
                vl:i,
                vlm:j,
                wn:k,
                er:l,
                rs:m,
                stp:n
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                        '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hadm_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['icustay_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['itemid'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['charttime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['storetime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['cgid'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['value'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['valueuom'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['warning'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['error'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['resultstatus'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['stopped'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert('Delete Success')
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#del_lab').click(function (event) {
        event.preventDefault();
        a = jq('#rid').val();
        b = jq('#sjid').val();
        c = jq('#hid').val(),
        d = jq('#itid').val();
        e = jq('#ct').val();
        f = jq('#vl').val();
        g = jq('#vln').val();
        h = jq('#vlm').val();
        i = jq('#fl').val();
        if(a||b||c||d||e||f||g||h||i){
            jq.ajax({
                url: '/delete/labevent/',
                type: 'post',
                contentType:'application/json',
                headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data:JSON.stringify({
                rid: a,
                sjid: b,
                hid: c,
                itid: d,
                ct:e,
                vl:f,
                vln:g,
                vlm:h,
                fl:i
                }),
                success: function(data){
                    if(data.status===0){
                        var htmlText2 = "";
                        for(var i =0;i <data.patient.length;i++){
                        htmlText2 +=' <tr>\n' +
                         '<th scope="row">'+ data.patient[i]['row_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['subject_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['hadm_id'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['itemid'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['charttime'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['value'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['valuenum'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['valueuom'] +'</th>\n' +
                        '<th scope="row">'+ data.patient[i]['flag'] +'</th>\n' +
                        '</tr>'
                        }
                    $('#databody').empty()
                    $('#databody').append(htmlText2)
                    alert('Delete Success')
                    }
                    else{
                        alert("Not Found");
                    }
                },
                error: function(xhr, err){
                    alert(err);
                }
            });
        }
        else{
            alert("No Input!");
        }
    });

    jq('#jp_adm').click(function(event){
        event.preventDefault();
        location.href = "/delete/admission";
    });

    jq('#jp_pat').click(function(event){
        event.preventDefault();
        location.href = "/delete/patient";
    });

    jq('#jp_cg').click(function(event){
        event.preventDefault();
        location.href = "/delete/caregiver";
    });

    jq('#jp_cpt').click(function(event){
        event.preventDefault();
        location.href = "/delete/cpt";
    });

    jq('#jp_dt').click(function(event){
        event.preventDefault();
        location.href = "/delete/datatimeevent";
    });

    jq('#jp_lab').click(function(event){
        event.preventDefault();
        location.href = "/delete/labevent";
    });

    jq('#jp_pre').click(function(event){
        event.preventDefault();
        location.href = "/delete/prescription";
    });

    jq('#h').click(function(event){
        event.preventDefault();
        location.href = "/home";
    });
    

});