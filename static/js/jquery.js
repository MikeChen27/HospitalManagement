var jq=jQuery.noConflict();
jq(document).ready( function(jq) {

    jq('#login').click(function (event) {
            event.preventDefault();
            var id_1 = jq('#id_').val();
            var psw = jq('#password').val();
            if(id_1!==""&&psw!==""){
            jq.ajax({
            url: '/',
            type: 'post',
            contentType:'application/json',
            headers:{'X-CSRFToken': jq('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
            data:JSON.stringify({
            id_: jq('#id_').val(),
            password: jq('#password').val(),
            }),
            success: function (data) {
                if(data.status===0){
                location.href = "/home/";
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






});