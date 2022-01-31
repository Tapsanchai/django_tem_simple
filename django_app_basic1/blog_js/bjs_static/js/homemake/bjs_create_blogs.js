
const PostCreateBlog = async (form_data) => {
    // console.log('form_data =' + form_data);
    let data = form_data
    console.log(data)

    let get_fields = $('.validate_create_blog').serializeJSON();
    let convert_obj = JSON.parse(get_fields);
    console.log("convert_obj = " ,convert_obj);
    var chk_blog_hashtags = convert_obj.blog_hashtags;
    $.each(convert_obj, (key, mes) => {
        if(mes || ''){ 
            if(key === 'blog_hashtags'){
                if(chk_blog_hashtags.length > 0) {
                    $(":checked")                    
                    .removeClass("is-invalid")
                    .addClass("is-valid");

                    $(":checkbox,:checkbox.is-valid").not(":checked").removeClass("is-valid").addClass("is-invalid");
                }
            }else {
                $(`[name="${key}"]`)
                .removeClass("is-invalid")
                .addClass("is-valid");
            }
        }
        // if(chk_blog_hashtags.length == 2) {
        //     alert("kuy")
        // }
    });

    res = await fetchData("../create_blog/", "POST", {'data':data})
    console.log(res)
    if (res.success) {
        if(res.data_json.data !== null) {
            link = res.data_json.url;
            console.log('go to URL =' + link);
            window.location.href = res.data_json.url;
        }else {
            if (res.data_json.messages_error) {
                console.log("have some error");
                let get_all_messages = res.data_json.messages_error;
                $.each(get_all_messages, (field_name, mes) => {
                        if (!chk_blog_hashtags) {
                            $(`[name="${field_name}"],[name="${field_name}[]"]`)
                            .removeClass("is-valid").addClass("is-invalid").focus();
                        }else {
                            // console.log("blog_hashtags =", chk_blog_hashtags.length);
                            if(chk_blog_hashtags.length > 0) {
                                $(`[name="${field_name}"]`)
                                .removeClass("is-valid").addClass("is-invalid").focus();
                            }
                            if(chk_blog_hashtags.length >= 2) {
                                $(`div[validate="blog_hashtags_error"]`).text("");
                                $(":checkbox").not(":checked").removeClass("is-invalid");
                            }
                        }
                        // if(chk_blog_hashtags) {
                        //     $(`[name="${field_name}"]`)
                        //     .removeClass("is-valid").addClass("is-invalid").focus();
                        //     if(chk_blog_hashtags.length >= 2) {
                        //         $(`div[validate="blog_hashtags_error"]`).text("");
                        //         $(":checkbox").not(":checked").removeClass("is-invalid");
                        //     }
                        // }

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
        console.log('create blog error: ' + res.success);
    }
};


$(document).ready(() => {

    $('#submit_frm_create_blogs').click(() => {
        // alert('click get form')
        var obj = $('#frm_create_blogs').serializeJSON();
        var form_jsonstring = JSON.stringify(obj);
        // console.log("Get Form obj=" + obj);
        // console.log("Get Form jsonstring=" + form_jsonstring);
        PostCreateBlog(obj);
        
    })
});