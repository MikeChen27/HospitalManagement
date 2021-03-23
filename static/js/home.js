var jq=jQuery.noConflict();
jq(document).ready( function(jq) {

    jq('#jp_ser').click(function(event){
        event.preventDefault();
        location.href = "/search/patient";
    });

    jq('#jp_add').click(function(event){
        event.preventDefault();
        location.href = "/add/patient";
    });

    jq('#jp_edt').click(function(event){
        event.preventDefault();
        location.href = "/edit/patient";
    });

    jq('#jp_del').click(function(event){
        event.preventDefault();
        location.href = "/delete/patient";
    });



});