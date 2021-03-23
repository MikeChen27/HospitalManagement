var jq=jQuery.noConflict();
jq(document).ready( function(jq) {

    jq('#add_adm').click(function (event){
        event.preventDefault();
        a = jq('#hid').val();
        if(a!==""){
            jq.ajax({
            url: '/add/admission/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:jq('#sjid').val(),
            hid:a,
            admt:jq('#admt').val(),
            dcht:jq('#dcht').val(),
            dtht:jq('#dtht').val(),
            adm_t:jq('#adm_t').val(),
            adml:jq('#adml').val(),
            dscl:jq('#dscl').val(),
            ins:jq('#ins').val(),
            lg:jq('#lg').val(),
            rlg:jq('#rlg').val(),
            mts:jq('#mts').val(),
            eth:jq('#eth').val(),
            ert:jq('#ert').val(),
            eot:jq('#eot').val(),
            dgn:jq('#dgn').val(),
            hef:jq('#hef').val(),
            hcd:jq('#hcd').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert('Add Success');
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
             alert("error");
             }

    });

    jq('#sbm_addcg').click(function (event){
        event.preventDefault();
        var cgid_add = jq('#cgid').val();
        if(cgid_add!==""){
            jq.ajax({
            url: '/add/caregiver/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            cgid: cgid_add,
            lb: jq('#lb').val(),
            dsc: jq('#dsc').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert(cgid_add+data.row_id);
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
             alert("error");
             }

    });

    jq('#sbm_addpat').click(function (event){
        event.preventDefault();
        var sjid_add = jq('#sjid').val();
        if(sjid_add!==""){
            jq.ajax({
            url: '/add/patient/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:sjid_add,
            gd:jq('#gd').val(),
            dob:jq('#dob').val(),
            dod:jq('#dod').val(),
            dodh:jq('#dodh').val(),
            dods:jq('#dods').val(),
            ef:jq('#ef').val(),
            }),
            success: function (data) {
                if(data.status===0){
                alert('Add Success');
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
             alert("error");
             }

    });

    jq('#add_cpt').click(function (event){
        event.preventDefault();
        a = jq('#sjid').val();
        if(a!==""){
            jq.ajax({
            url: '/add/cpt/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:a,
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
                alert('Add Success');
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
             alert("error");
             }

    });
    
    jq('#add_pre').click(function (event){
        event.preventDefault();
        a = jq('#sjid').val();
        if(a!==""){
            jq.ajax({
            url: '/add/prescription/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:a,
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
                alert('Add Success');
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
             alert("error");
             }

    });

    jq('#add_dt').click(function (event){
        event.preventDefault();
        a = jq('#sjid').val();
        if(a!==""){
            jq.ajax({
            url: '/add/prescription/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:a,
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
                alert('Add Success');
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
             alert("error");
             }
    });

    jq('#add_lab').click(function (event){
        event.preventDefault();
        a = jq('#hid').val();
        if(a!==""){
            jq.ajax({
            url: '/add/labevent/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            sjid:jq('#sjid').val(),
            hid:a,
            itid:jq('#itid').val(),
            ct:jq('#ct').val(),
            vl:jq('#vl').val(),
            vln:jq('#vln').val(),
            vlm:jq('#vlm').val(),
            fl:jq('#fl').val()
            }),
            success: function (data) {
                if(data.status===0){
                alert('Add Success');
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
             alert("error");
             }

    });

    jq('#jp_adm').click(function(event){
        event.preventDefault();
        location.href = "/add/admission";
    });

    jq('#jp_pat').click(function(event){
        event.preventDefault();
        location.href = "/add/patient";
    });

    jq('#jp_cg').click(function(event){
        event.preventDefault();
        location.href = "/add/caregiver";
    });

    jq('#jp_cpt').click(function(event){
        event.preventDefault();
        location.href = "/add/cpt";
    });

        jq('#jp_dt').click(function(event){
        event.preventDefault();
        location.href = "/add/datatimeevent";
    });

        jq('#jp_lab').click(function(event){
        event.preventDefault();
        location.href = "/add/labevent";
    });

        jq('#jp_pre').click(function(event){
        event.preventDefault();
        location.href = "/add/prescription";
    });

    jq('#h').click(function(event){
        event.preventDefault();
        location.href = "/home";
    });
});