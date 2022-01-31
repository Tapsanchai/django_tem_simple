const GETFullPersonalAddress_ByID = async (con_id) => {
    try {
        let get_con_id = +con_id;
        res = await fetchData(`create_or_update_personal_address/show_list/?con_id=${get_con_id}`, "GET", {});
        console.log("GET success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullCreatePersonal_Address = async (data_form, get_contact_id) => {
    try {
        let get_form = data_form;
        let get_id = get_contact_id
        console.log("get_form =", get_form);
        res = await fetchData(`create_or_update_personal_address/create/${get_id}/`, "POST", { create_personal_address: get_form });
        console.log("POST success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullUpdatePersonal_Address = async (data_form, id) => {
    try {
        if (id || '') {
            let get_id = id;
            let get_form = data_form;
            console.log("get_id =", get_id);
            console.log("get_form =", get_form);
            res = await fetchData(`create_or_update_personal_address/update/${get_id}/`, "POST", { update_personal_address: get_form });
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

const POSTChagePrimaryStatusPersonal_Address = async (get_row_id, this_contact_id) => {
    try {
        let row_id = get_row_id;
        let this_contact = this_contact_id
        res = await fetchData(`create_or_update_personal_address/update/${row_id}/`, "POST", { this_personal_address: this_contact });
        console.log("POST success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullDeletePersonal_Address = async (row_id, contact_id) => {
    try {
        if (row_id || '') {
            let get_id = + row_id;
            let get_contact_id = + contact_id;
            console.log("get_id =", get_id);
            res = await fetchData(`delete_personal_address/${get_id}/`, "POST", { data_by_contact_id: get_contact_id });
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

$(document).ready(function () {

    $('#show_create_personal_address_view').on('hidden.bs.modal', function (event) {
        // $(`form#frm_create_personal_address input`).not(':hidden[name="csrfmiddlewaretoken"]').val(null);
        $('form#frm_create_personal_address')[0].reset();
        $(`form#frm_create_personal_address select option`).removeAttr('selected');
        $(`form#frm_create_personal_address select option:first`).attr('selected', 'selected');
        $(`form#frm_create_personal_address input:checkbox`).removeAttr('checked');
        $('form#frm_create_personal_address').removeAttr('update_to');
        $(`#frm_create_personal_address`).find('input').removeClass([ "is-invalid", "is-valid"]);
        $(`#frm_create_personal_address div[err_for] > div`).remove();

    });

    $('#show_personal_address_view').on('hidden.bs.modal', function (event) { // update coantact detail when close modal
        let call_ready_to_update = ReadyToUpdateContact(get_contact_id);
        call_ready_to_update.then((result) => {
            console.log(result);
        });
    });

    $("a#new_personal_address").click(() => {  // show table personal_address list
        // console.log(get_contact_id);
        let data_personal_address_by_con = GETFullPersonalAddress_ByID(get_contact_id);
        data_personal_address_by_con.then((obj_data) => {
            console.log(obj_data);
            let obj_personal_address = obj_data.data_json.data.data_personal_address;
            console.log(obj_personal_address);
            let all_obj_from_personal_address = RenderHTML_Personal_address_list(obj_personal_address);
            all_obj_from_personal_address.then((personal_address_all_obj) => {
                let { personal_address_html, new_obj, get_contact_by } = personal_address_all_obj; //get 3 value from obj
                $('tbody#show_data_personal_address').html(personal_address_html);
                console.log('pull to html success [personal_address]');
                // call check radio
                let check_list = CheckList_View('personal_address');
                let check_con_id = CheckContact_ID_Personal_Address(get_contact_by, get_contact_id);
                check_con_id.then(() => {
                    let standfor_update_delete = ReadyForUpdateOrDelete_Personal_Address(new_obj);
                });

            });
        });
    });


    $("#btn_save_personal_address").click(function () {  //save create/update personal_address
        let base_form = $("form#frm_create_personal_address");
        let get_form_obj = base_form.serializeJSON();
        console.log(`get_form_obj = ${get_form_obj}`);
        if (base_form.is("[update_to]")) {
            console.log("is update");
            let get_update_id = $(base_form).attr(
                "update_to"
            );
            console.log(`get_update_id = ${get_update_id}`);
            let post_update_personal_byid = POSTFullUpdatePersonal_Address(get_form_obj, get_update_id)
            post_update_personal_byid.then((res_data_form_post) => {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                console.log(data);
                if (!data.data_invalid) {
                    let get_data_personal_address_new = data.data_personal_address;
                    console.log("new_obj_list_from_queryset = ", get_data_personal_address_new);
                    $("#show_create_personal_address_view").modal("hide");
                    let all_obj_from_personal_address = RenderHTML_Personal_address_list(get_data_personal_address_new);
                    all_obj_from_personal_address.then((personal_address_all_obj) => {
                        let { personal_address_html, new_obj, get_contact_by } = personal_address_all_obj; //get 3 value from obj
                        $('tbody#show_data_personal_address').html(personal_address_html);
                        console.log('pull to html success [personal_address]');
                        // call check radio
                        let check_list = CheckList_View('personal_address');
                        let check_con_id = CheckContact_ID_Personal_Address(get_contact_by, get_contact_id);
                        check_con_id.then(() => {
                            let standfor_update_delete = ReadyForUpdateOrDelete_Personal_Address(new_obj);
                        });
                    });
                } else {
                    let get_data_invalid = data.data_invalid;
                    console.log("invaild =", get_data_invalid);
                    let get_data_mes = data.mes_err;
                    let event_name = 'personal_address';
                    CallAlertRequired_ForSub(get_data_mes,event_name);
                }
            });
        } else {
            console.log("is create");
            let post_create_personal = POSTFullCreatePersonal_Address(get_form_obj, get_contact_id)
            post_create_personal.then((res_data_form_post) => {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                console.log(data);
                if (!data.data_invalid) {
                    let get_data_personal_address_new = data.data_personal_address;
                    console.log("new_obj_list_from_queryset = ", get_data_personal_address_new);
                    $("#show_create_personal_address_view").modal("hide");
                    let all_obj_from_personal_address = RenderHTML_Personal_address_list(get_data_personal_address_new);
                    all_obj_from_personal_address.then((personal_address_all_obj) => {
                        let { personal_address_html, new_obj, get_contact_by } = personal_address_all_obj; //get 3 value from obj
                        $('tbody#show_data_personal_address').html(personal_address_html);
                        console.log('pull to html success [personal_address]');
                        // call check radio
                        let check_list = CheckList_View('personal_address');
                        let check_con_id = CheckContact_ID_Personal_Address(get_contact_by, get_contact_id);
                        check_con_id.then(() => {
                            let standfor_update_delete = ReadyForUpdateOrDelete_Personal_Address(new_obj);
                        });
                    });
                } else {
                    let get_data_invalid = data.data_invalid;
                    console.log("invaild =", get_data_invalid);
                    let get_data_mes = data.mes_err;
                    let event_name = 'personal_address';
                    CallAlertRequired_ForSub(get_data_mes,event_name);
                }
            });

        }
    });


    $("#btn_save_personal_address_change_status").click(function () {  // save change primary status | confrirm
        let get_row_id = ($('input[name="select_primary_p-a"]:checked').val())
        let this_contact_id = get_contact_id;
        console.log("this_contact_id", this_contact_id);
        console.log("get_row_id = ", get_row_id);

        if(!isNaN(get_row_id) || get_row_id) {
            let post_new_status = POSTChagePrimaryStatusPersonal_Address(get_row_id, this_contact_id)
            post_new_status.then(function (res_data_form_post) {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                if(!data.mes) {
                    let get_data_personal_address_new = data.data_personal_address;
                    console.log("new_obj_list_from_queryset = ", get_data_personal_address_new);
                    let all_obj_from_personal_address = RenderHTML_Personal_address_list(get_data_personal_address_new);
                    all_obj_from_personal_address.then((personal_address_all_obj) => {
                        let { personal_address_html, new_obj, get_contact_by } = personal_address_all_obj; //get 3 value from obj
                        $('tbody#show_data_personal_address').html(personal_address_html);
                        console.log('pull to html success [personal_address]');
                        // call check radio
                        let check_list = CheckList_View('personal_address');
                        check_list.then(() => {
                            console.log(data);
                            alert('change primay personal_address success');
                            setTimeout(function () {
                                $("#show_personal_address_view").modal("hide");
                            }, 1000);
                        })
                    });
    
                }else {
                    console.log(data.mes);
                    setTimeout(function () {
                        $("#show_personal_address_view").modal("hide");
                    }, 1000);
                }
    
            });
        }else{
            alert('Placese select a radio box');;
        }
    });

});


//check to create or update form
const CheckContact_ID_Personal_Address = async function (contact_by, contact_id) {
    console.log("rew_contact_id = ", contact_id);
    console.log("contact_by = ", contact_by);
    try {
        if (contact_by || "") { // personal list = null/empty
            $("a#new_personal_address").click(function () {
                console.log("open modal create personal_address");
                console.log("rew_contact_id = ", contact_by);
                $('form#frm_create_personal_address input:hidden[id="contact_by_mo_p-a"]').val(contact_by);
            });
        } else {
            $("a#new_personal_address").click(function () {
                console.log("open modal create personal_address");
                console.log("contact_by = ", contact_id);
                $('form#frm_create_personal_address input:hidden[id="contact_by_mo_p-a"]').val(contact_id);
            });
        }
    } catch (err) {
        console.log(err);
    }
};

const ReadyForUpdateOrDelete_Personal_Address = async function (new_obj) {
    try {
        $('a[name="update_personal_address"]').click(function () { //show pop-up update personal_address
            //get id personal email
            let get_id_personal_address = + $(this).attr("target");
            console.log(`get_id_personal_address = ${get_id_personal_address}`);
            //filter obj_personal_address to match ID
            let filter_obj_by_id = new_obj.filter(
                (item) => item.id === get_id_personal_address
            );
            console.log("filter_obj_by_id = ", filter_obj_by_id);
            let push_data_to_form_personal_address = RenderPushDataToFormUpdatePersonal_Address(filter_obj_by_id, get_id_personal_address)
            push_data_to_form_personal_address.then((data_personal_address) => {
                let get_data_personal_address_form = data_personal_address;
                console.log("data_from_render_ferch_to_field = ", get_data_personal_address_form);
            });
        });
        ReadyForDeletePersonal_Address();
    }catch (err) {
        console.log(err);
    }
};

const ReadyForDeletePersonal_Address = async function () {
    try {
        $('a[name="delete_personal_address"]').click(function () { // delete personal_address by id
            let get_personal_address_id = $(this).attr("target");
            console.log(get_personal_address_id);
            let chk_confirm = confirm("Are you sure to delete ?");
            if (chk_confirm) {
                let call_delete_contact = POSTFullDeletePersonal_Address(get_personal_address_id, get_contact_id);
                call_delete_contact.then((res_data_form_post) => {
                    let { data } = res_data_form_post.data_json;
                    console.log(data);
                    if (!data.mes_err) {
                        let get_data_personal_address_new = data.data_personal_address;
                        console.log("new_obj_list_from_queryset = ", get_data_personal_address_new);
                        let all_obj_from_personal_address = RenderHTML_Personal_address_list(get_data_personal_address_new);
                        all_obj_from_personal_address.then((personal_address_all_obj) => {
                            let { personal_address_html, new_obj, get_contact_by } = personal_address_all_obj; //get 3 value from obj
                            $('tbody#show_data_personal_address').html(personal_address_html);
                            console.log('pull to html success [personal_address]');
                            let standfor_update_delete = ReadyForUpdateOrDelete_Personal_Address(new_obj);
                        });
    
                    } else {
                        console.log("mes err =", data.mes_err);
                    }
                });
            } else {
                alert("OK");
            }
        });
    }catch (err) {
        console.log(err);
    }
};
