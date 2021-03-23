var jq=jQuery.noConflict();
jq(document).ready( function(jq) {

    jq('#edt_pat').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/patient/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid: jq('#sjid').val(),
            gd: jq('#gd').val(),
            dob: jq('#dob').val(),
            dod: jq('#dod').val(),
            dodh: jq('#dodh').val(),
            dods: jq('#dods').val(),
            ef: jq('#ef').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_cg').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/caregiver/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid: rid,
            cgid: jq('#cgid').val(),
            lb: jq('#lb').val(),
            dsc: jq('#dsc').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_adm').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/admission/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid: jq('#sjid').val(),
            hid: jq('#hid').val(),
            admt: jq('#admt').val(),
            dcht: jq('#dcht').val(),
            dtht: jq('#dtht').val(),
            adm_t: jq('#adm_t').val(),
            adml: jq('#adml').val(),
            dscl: jq('#dscl').val(),
            ins: jq('#ins').val(),
            lg: jq('#lg').val(),
            rlg: jq('#rlg').val(),
            mts: jq('#mts').val(),
            eth: jq('#eth').val(),
            ert: jq('#ert').val(),
            eot: jq('#eot').val(),
            dgn: jq('#dgn').val(),
            hef: jq('#hef').val(),
            hcd: jq('#hcd').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_cpt').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/cpt/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid:jq('#sjid').val(),
            hid:jq('#hid').val(),
            cc:jq('#cc').val(),
            cd:jq('#cd').val(),
            c_c:jq('#c_c').val(),
            cn:jq('#cn').val(),
            cs:jq('#cs').val(),
            tis:jq('#tis').val(),
            sh:jq('#sh').val(),
            ssh:jq('#ssh').val(),
            dsc:jq('#dsc').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_pre').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/prescription/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid:jq('#sjid').val(),
            hid:jq('#hid').val(),
            iid:jq('#iid').val(),
            sd:jq('#sd').val(),
            ed:jq('#ed').val(),
            dt:jq('#dt').val(),
            dr:jq('#dr').val(),
            dnp:jq('#dnp').val(),
            dng:jq('#dng').val(),
            fdc:jq('#fdc').val(),
            gsn:jq('#gsn').val(),
            ndc:jq('#ndc').val(),
            ps:jq('#ps').val(),
            dvr:jq('#dvr').val(),
            dur:jq('#dur').val(),
            fvd:jq('#fvd').val(),
            fud:jq('#fud').val(),
            rt:jq('#rt').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_dt').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/datatimeevent/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid:jq('#sjid').val(),
            hid:jq('#hid').val(),
            iid:jq('#iid').val(),
            itid:jq('#itid').val(),
            ct:jq('#ct').val(),
            st:jq('#st').val(),
            cgid:jq('#cgid').val(),
            vl:jq('#vl').val(),
            vlm:jq('#vlm').val(),
            wn:jq('#wn').val(),
            er:jq('#er').val(),
            rs:jq('#rs').val(),
            stp:jq('#stp').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#edt_lab').click(function (event){
        event.preventDefault();
        var rid = jq('#rid').val();
        if(rid!==""){
            jq.ajax({
            url: '/edit/labevent/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            rid:rid,
            sjid:jq('#sjid').val(),
            hid:jq('#hid').val(),
            itid:jq('#itid').val(),
            ct:jq('#ct').val(),
            vl:jq('#vl').val(),
            vln:jq('#vln').val(),
            vlm:jq('#vlm').val(),
            fl:jq('#fl').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert("Edit Success");
                }
                else{
                alert("wrong");}
                },
            error: function(xhr, err){
                    alert('fail');
                }
             });
             }
             else{
             alert("error");}

    });

    jq('#jp_adm').click(function(event){
        event.preventDefault();
        location.href = "/edit/admission";
    });

    jq('#jp_pat').click(function(event){
        event.preventDefault();
        location.href = "/edit/patient";
    });

    jq('#jp_cg').click(function(event){
        event.preventDefault();
        location.href = "/edit/caregiver";
    });

    jq('#jp_cpt').click(function(event){
        event.preventDefault();
        location.href = "/edit/cpt";
    });

    jq('#jp_dt').click(function(event){
        event.preventDefault();
        location.href = "/edit/datatimeevent";
    });

    jq('#jp_lab').click(function(event){
        event.preventDefault();
        location.href = "/edit/labevent";
    });

    jq('#jp_pre').click(function(event){
        event.preventDefault();
        location.href = "/edit/prescription";
    });

    jq('#h').click(function(event){
        event.preventDefault();
        location.href = "/home";
    });
});