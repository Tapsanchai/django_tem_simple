const PostRegisMember = async (form_data) => {
    let data = form_data
    console.log(data)

    res = await fetchData("../register/", "POST", {'data':data})
    console.log(res)
    if (res.success) {
        if(res.data_json.data === null) {
            link = res.data_json.url;
            console.log('go to URL =' + link);
            window.location.href = res.data_json.url;
        }else {
            if (res.data_json.messages_error) {
                console.log("have some error");
                let get_all_messages = res.data_json.messages_error;
    
                $.each(get_all_messages, (field_name, mes) => {
                        $(`input[name="${field_name}"]`)
                        .removeClass("is-valid").addClass("is-invalid").focus();
                        mes.map((item) => {
                            // if (field_name === "__all__") {
                            //     $(`input.validate_login`)
                            //     .removeClass("is-valid").addClass("is-invalid").focus();
                            //     alert(item.message);
                            // }else{
                                $(`.make_validate[validate="${field_name}_error"]`).text(item.message)
                            // }
                        });
                    });
                } 
        }
    } else {
        console.log('register error: ' + res.success);
    }
}

$(document).ready(() => {
    $('#submit_frm_regis_member').click(() => {
        let get_regis_obj = $('#frm_regis_member').serializeJSON();
        console.log('obj' ,get_regis_obj);
        PostRegisMember(get_regis_obj);

        let get_fields = $('.validate_register').serializeJSON();
        let convert_obj = JSON.parse(get_fields);
        console.log("convert_obj = " ,convert_obj);
        $.each(convert_obj, (key, mes) => {
            if(mes || ''){ 
                $(`input[name="${key}"]`)
                .removeClass("is-invalid")
                .addClass("is-valid");
            }
        });

    });
});
