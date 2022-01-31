var base_page = 1;  //start
var min_page;
var max_page;
var data_contact;
var status_chk;
var total_contact_count;
var obj_for_search ="";

const GetContact_All = async (page_number, obj_for_search) => {
    let start_base_page =+ page_number;
    let get_obj_key_value = obj_for_search;
    console.log('get_obj_key_value', get_obj_key_value);
    try {
        res = await fetchData(`render/?page=${start_base_page}&search_by=${get_obj_key_value.key}&value=${get_obj_key_value.value}`, "GET", {});
        console.log("call data success");
        return res;
    } catch (err) {
        console.log("call data failed error =", err);
    }
};

const CallUpdateOrDelete = async () => {
    try {

        $('a[name="update_contact"]').click(function () {  // show contact details for edit/update by id
            let get_id = $(this).attr("target");
            let call_ready_to_update = ReadyToUpdateContact(get_id);
            call_ready_to_update.then((result) => {
                console.log(result);
            })
        });

        $('a[name="dalete_contact"]').click(function () { // delete_full_contact by id
            let get_contact_id = $(this).attr("target");
            console.log(get_contact_id);
            let chk_confirm = confirm("Are you sure to delete ?");
            if (chk_confirm) {
                let call_delete_contact = POSTFullDeleteContact(get_contact_id);
                call_delete_contact.then((mes) => {
                    console.log(mes);
                    let { data } = mes.data_json;
                    if (data === 'delete contact success') {
                        console.log('data =', data);
                        (async = () => { let get_load = LoadAllContact(); })();
                    }
                });
            } else {
                alert("OK");
            }
        });
    } catch (err) {
        console.log(err);
    }
};

const CallGetPageFromLinkPaginations = async () => {
    try {
        $('li > a.run_count_all_page').click(function () {
            let get_target_page = $(this).attr('target_page');
            if (isNaN(get_target_page) && get_target_page === 'previous') {
                (base_page === min_page ? base_page-- : base_page = min_page-1)
                console.log('base_page = ', base_page);
                console.log('get_target_page = ', get_target_page);
                (async = () => {
                    const get_load = LoadAllContact();
                })();
            } else if (isNaN(get_target_page) && get_target_page === 'next') {
                (base_page === max_page ? base_page++ : base_page = max_page+1)
                    console.log('get_target_page = ', get_target_page);
                    console.log('base_page = ', base_page);
                    (async = () => {
                        const get_load = LoadAllContact();
                    })();
            }
            else {
                let get_int_page = + get_target_page;
                base_page = get_int_page;
                console.log('get_int_page = ', get_int_page);
                console.log('base_page = ', base_page);
                (async = () => {
                    const get_load = LoadAllContact();
                })();
            }

        });
    } catch (err) {
        console.log(err);
    }
};

const CallGetSearchData = async () => {
    try {
        $('#btn_search').click(function () {  //get query from search
            let value = $('#value_search').val();
            let key = $('#key_search').val();
            if (value.trim() !== '') {
                let call_search_by = SerachQueryBy(key, value);
                call_search_by.then((res_obj) => {
                    console.log(res_obj)
                    obj_for_search = res_obj;
                    base_page = 1;
                    (async = () => {
                        const get_load = LoadAllContact();
                    })();
                });
            } else {
                console.log('value is empty');
                obj_for_search ="";
                base_page = 1;
                (async = () => {
                    const get_load = LoadAllContact();
                })();
            }
        });
    } catch (err) {
        console.log(err);
    }
};

const LoadAllContact = async () => {
    let call_clearn_form = ChkContactPopup();
    call_clearn_form.then(() => {
        console.log('clearn form success')
    });

    var now_page = base_page; //call_base_page
    console.log('now_page =', now_page);

    try {
        $('#value_search').val(null);

        let call_contact_obj = GetContact_All(now_page, obj_for_search);
        call_contact_obj.then((contact) => {
            $('ul#show_pagiantion > *').remove();
            console.log(contact);
            let { data } = contact.data_json;
            data_contact = data.data_contact_list;
            total_contact_count = data.data_total_contact; 
            min_page = data.data_minpage;
            max_page = data.data_maxpage;
            status_chk = data.mes;

            console.log(total_contact_count);
            console.log(data_contact);
            let pull_to_render = RenderContactHTML(data_contact, total_contact_count, min_page, max_page);
            pull_to_render.then((contact_for_set_html) => {

                let data_contact_html = contact_for_set_html.show_contact_list;
                let data_page_previous = contact_for_set_html.show_pervious_page;
                let data_page_run = contact_for_set_html.show_page_run;
                let data_page_next = contact_for_set_html.show_nextpage

                // --------- set pagination ---------
                $('tbody#show_data').html(data_contact_html);

                if (status_chk.pervious) {
                    $(data_page_previous).appendTo('ul#show_pagiantion');
                } else {
                    $('li#page_previous').remove();
                    console.log('delete page_previous');
                }

                $(data_page_run).appendTo('ul#show_pagiantion')

                if (status_chk.next) {
                    $(data_page_next).appendTo('ul#show_pagiantion');
                } else {
                    $('li#page_next').remove();
                    console.log('delete page_next');
                }
                // --------- END set pagination ---------

                console.log('pull to html success')
                $('tr td.align-middle').not(".text-center").addClass('pl-2');
                CallUpdateOrDelete();
                CallGetPageFromLinkPaginations();
            });

            
        });
    } catch (err) {
        console.log(err);
    }
}

const ReadyToUpdateContact = async (obj_id) => {
    try {
        await $('form#frm_update_contact input').val(null);
        // await $(`form#frm_update_contact > input`).attr("value", null);
        let data_update_contact_byid = GETFullUpdateContact(obj_id);
        data_update_contact_byid.then((obj_contact) => {
            console.log(obj_contact);
            let call_loaddata = LoadDetailDataContacts(obj_contact)
            call_loaddata.then((final_obj) => {
                console.log('final_data_list =', final_obj, '-->', typeof final_obj);
                let push_data_to_form_contact = RenderPushDataToFormUpdateContact(final_obj);
                push_data_to_form_contact.then((data_contact) => {
                    console.log(data_contact);
                    //call get_contact_id
                    get_contact_id = data_contact.map((item) => {
                        return item.contact_id;
                    });
                    console.log("get contact_id =", get_contact_id);
                });
            })
        });
        // console.log('Update & Load New Detail Success.');
        return 'Update & Load New Detail Success.';
    } catch (err) {
        console.log(err);
    }
};


const LoadDetailDataContacts = async (all_obj) => {
    try {
        let [data_contact, data_alternate_email, data_alternate_phone, data_personal_address] = all_obj.data_json.data;
        let new_data_list = [
            data_contact['data_contact'],
            data_alternate_email['data_alternate_email'],
            data_alternate_phone['data_alternate_phone'],
            data_personal_address['data_personal_address'],
        ];
        // console.log('new_list = ',new_data_list, '-->', typeof new_data_list);
        let custom_all_new_obj = {};
        await new_data_list.map((item) => {
            // console.log('item = ',item);
            item.map((value) => {
                return Object.assign(custom_all_new_obj, value)  //loop copy item to new obj
            });
        });
        final_data_list = [custom_all_new_obj];
        return final_data_list;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullCreateContact = async (data_contact) => {
    try {
        res = await fetchData("create_full_contact/", "POST", {
            data_contact: data_contact,
        });
        console.log("POST success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullUpdateContact = async (data_form, id) => {
    try {
        if (id || '') {
            let get_id = + id;
            let get_form = data_form;
            console.log("get_id =", get_id);
            console.log("get_form =", get_form);
            res = await fetchData(`update_full_contact/${get_id}/`, "POST", { update_this_contact: get_form });
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

const POSTFullDeleteContact = async (con_id) => {
    try {
        if (con_id || '') {
            let get_id = + con_id;
            console.log("get_id =", get_id);
            res = await fetchData(`delete_full_contact/${get_id}/`, "POST", {});
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

const GETFullUpdateContact = async (data_id) => {
    try {
        res = await fetchData(`update_full_contact/${data_id}/`, "GET", {});
        console.log("GET success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const SerachQueryBy = async (main_key, main_value) => {
    console.log('key = ', main_key);
    console.log('value = ', main_value);
    let key_list_for_search = ['hn', 'gender'];
    let new_obj_query = {};
    try {
        if (key_list_for_search.includes(main_key)) {
            async function GetQuserySearch(main_key, main_value) {
                let get_key_match;
                get_key_match = await key_list_for_search.filter(item => { return item === main_key; });
                new_obj_query = {
                    key: get_key_match,
                    value: main_value,
                }
                return new_obj_query;
            }
            return await GetQuserySearch(main_key, main_value);
        }
    } catch (err) {
        console.log(err);
    }
};

const ChkContactPopup = async () => {
    try {
        $('#show_update_view').on('hidden.bs.modal', function (event) {
            $('#frm_update_contact')[0].reset();
            $('input.cal_age').val(null);
            $('input.cal_age').attr('disabled');
            $(`#frm_update_contact`).find('input,select').removeClass([ "is-invalid", "is-valid"]);
            $(`#frm_update_contact div[err_for] > div`).remove();

        });

        $('#show_create_view').on('hidden.bs.modal', function (event) {
            $('#frm_create_contact')[0].reset();
            $('input.cal_age').val(null);
            $('input.cal_age').attr('disabled');
            $(`#frm_create_contact`).find('input,select').removeClass([ "is-invalid", "is-valid"]);
            $(`#frm_create_contact div[err_for] > div`).remove();

        });
    } catch (err) {
        console.log(err);
    }
};

(async = () => { let get_load_searchdata = CallGetSearchData(); })();

const CallAlertRequired  = async (mes_err, event_name) => {
    try {
        let call_event_name = event_name;
        let call_mes;
        let build_tag;
        let get_field_name;
  
        let build_chk_form_fields_list = [];
        let build_get_field_name_list = [];
        let build_get_new_obj = {};

        // console.log(`key = `, call_event_name);
        let get_fields = $(`#frm_${call_event_name}_contact`).serializeArray();
        // console.log('list_form = ',get_fields);
        get_fields.map((field) => {return build_chk_form_fields_list.push(field.name)});
        // console.log('build_chk_fields = ', build_chk_form_fields_list);
        // console.log('alert error message =', mes_err, '-->', typeof mes_err);

        await $.each(mes_err, (field_name, obJ_item) => {
            console.log(`field_name = ${field_name}  obJ_item = ${obJ_item}`);
            build_get_field_name_list.push(field_name);
            get_field_name = field_name; 

            obJ_item.map((item) => {
            build_get_new_obj[get_field_name] = item;
            });

        });

        // console.log('build_get_new_obj = ', build_get_new_obj);
        // console.log('build_get_field_name_list = ', build_get_field_name_list);

        await build_chk_form_fields_list.map((key) => {
            // console.log(`key = ${key}`);
            if(build_get_field_name_list.includes(key)) {   
                call_mes = build_get_new_obj[key].message;
                // console.log(call_mes);    
                build_tag = `<div class="invalid-feedback set_err d-block">${call_mes}</div>`;
                $(`#${key}_${call_event_name}`).removeClass('is-valid').addClass('is-invalid').focus();
                $(`div[err_for="${key}_${call_event_name}"]`).html(build_tag);
            }else {
                if ($(`#${key}_${call_event_name}`).hasClass('is-invalid')) {
                    $(`#${key}_${call_event_name}`).removeClass('is-invalid').addClass('is-valid');
                    $(`div[err_for="${key}_${call_event_name}"] > div`).remove();
                }else {
                    $(`#${key}_${call_event_name}`).removeClass([ "is-invalid", "is-valid" ]);
                    $(`div[err_for="${key}_${call_event_name}"] > div`).remove();
                }
            }
        });
        console.log('show alert success');
        return true;
    }catch (err) {
        console.log(err);
    }
};

$(document).ready(function () {

    //create_full_contact
    $('#btn_save_create_contact_full').click(() => {
        $('input[name="age"]').removeAttr("disabled");
        get_form_obj_contact = $('#frm_create_contact').serializeJSON();
        let post_create_data = POSTFullCreateContact(get_form_obj_contact);
        post_create_data.then((res_obj) => {
            console.log(res_obj)
            let { data } = res_obj.data_json;
            if (!data.data_invalid) {
                let get_data_alternate_email_new = data.data_contact;
                console.log("new_obj_list_from_queryset = ", get_data_alternate_email_new);
                $('#show_create_view').modal('hide');
                (async = () => {
                    obj_for_search ="";
                    const get_load = LoadAllContact();
                })();
            } else {
                let get_data_invalid = data.data_invalid;
                let get_data_mes = data.mes_err;
                let event_name = 'create';
                console.log("invaild =", get_data_invalid);
                let call_alert = CallAlertRequired(get_data_mes,event_name);

            }
        });

    });

    // update_full_contact
    $('#btn_save_update_contact_full').click(() => {
        $('input[name="age"]').removeAttr("disabled");
        let get_form_obj_contact = $('#frm_update_contact').serializeJSON();
        let post_update_data = POSTFullUpdateContact(get_form_obj_contact, get_contact_id);
        post_update_data.then((res_obj) => {
            console.log(res_obj)
            let { data } = res_obj.data_json;
            if (!data.data_invalid) {
                console.log(data);
                $('#show_update_view').modal('hide');
                (async = () => {
                    obj_for_search ="";
                    const get_load = LoadAllContact();
                })();

            } else {
                let get_data_invalid = data.data_invalid;
                let get_data_mes = data.mes_err;
                let event_name = 'update';
                console.log("invaild =", get_data_invalid);
                let call_alert = CallAlertRequired(get_data_mes,event_name);
            }
        })
    });


    // set date_field in contact form
    $('input[name="date_of_birth"]').change(function () {
        let get_date_value = $(this).val();
        // console.log(get_date_value)
        var today = new Date();
        var birthDate = new Date(get_date_value);
        // console.log(birthDate)
        var age = today.getFullYear() - birthDate.getFullYear();
        var m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
            age--;
            // alert('Age is worng');
        }
        // console.log(age)
        (isNaN(age) ? age="" : age);
        $('input.cal_age').val(age);
        $('input.cal_age').attr('value', age);
    });

    $('input[name="date_of_birth"]').click(function () {
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth() + 1; //January is 0 so need to add 1 to make it 1!
        var yyyy = today.getFullYear();
        if (dd < 10) {
            dd = '0' + dd
        }
        if (mm < 10) {
            mm = '0' + mm
        }
        today = yyyy + '-' + mm + '-' + dd;
        $('input[name="date_of_birth"]').prop('max', today)
    });

});

