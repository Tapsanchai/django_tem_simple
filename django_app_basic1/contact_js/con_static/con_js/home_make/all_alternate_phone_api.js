const GETFullAlternatePhone_ByID = async (con_id) => {
    try {
        let get_con_id = +con_id;
        res = await fetchData(`create_or_update_alternate_phone/show_list/?con_id=${get_con_id}`, "GET", {});
        console.log("GET success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullCreateAlternate_Phone = async (data_form, get_contact_id) => {
    try {
        let get_form = data_form;
        let get_id = get_contact_id
        console.log("get_form =", get_form);
        res = await fetchData(`create_or_update_alternate_phone/create/${get_id}/`, "POST", { create_alternate_phone: get_form });
        console.log("POST success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullUpdateAlternate_Phone = async (data_form, id) => {
    try {
        if (id || '') {
            let get_id = id;
            let get_form = data_form;
            console.log("get_id =", get_id);
            console.log("get_form =", get_form);
            res = await fetchData(`create_or_update_alternate_phone/update/${get_id}/`, "POST", { update_alternate_phone: get_form });
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

const POSTChagePrimaryStatusAlternate_Phone = async (get_row_id, this_contact_id) => {
    try {
        let row_id = get_row_id;
        let this_contact = this_contact_id
        res = await fetchData(`create_or_update_alternate_phone/update/${row_id}/`, "POST", { this_alternate_phone: this_contact });
        console.log("POST success");
        return res;
    } catch (err) {
        console.log(err);
    }
};

const POSTFullDeleteAlternate_Phone = async (row_id, contact_id) => {
    try {
        if (row_id || '') {
            let get_id = + row_id;
            let get_contact_id = + contact_id;
            console.log("get_id =", get_id);
            res = await fetchData(`delete_alternate_phone/${get_id}/`, "POST", { data_by_contact_id: get_contact_id });
            console.log("POST success");
            return res;
        }
    } catch (err) {
        console.log(err);
    }
};

$(document).ready(function () {

    $('#show_create_alternate_phone_view').on('hidden.bs.modal', function (event) {
        // $(`form#frm_create_alternate_phone input`).not(':hidden[name="csrfmiddlewaretoken"]').val(null);
        $('form#frm_create_alternate_phone')[0].reset();
        $(`form#frm_create_alternate_phone select option`).removeAttr('selected');
        $(`form#frm_create_alternate_phone select option:first`).attr('selected', 'selected');
        $(`form#frm_create_alternate_phone input:checkbox`).removeAttr('checked');
        $('form#frm_create_alternate_phone').removeAttr('update_to');
        $(`#frm_create_alternate_phone`).find('input,select,textarea').removeClass([ "is-invalid", "is-valid"]);
        $(`#frm_create_alternate_phone div[err_for] > div`).remove();
    });

    $('#show_alternate_phone_view').on('hidden.bs.modal', function (event) { // update coantact detail when close modal
        let call_ready_to_update = ReadyToUpdateContact(get_contact_id);
        call_ready_to_update.then((result) => {
            console.log(result);
        });
    });


    $("a#new_alternate_phone").click(() => {  // show table alternate_phone list
        // console.log(get_contact_id);
        let data_alternate_phone_by_con = GETFullAlternatePhone_ByID(get_contact_id);
        data_alternate_phone_by_con.then((obj_data) => {
            console.log(obj_data);
            let obj_alternate_phone = obj_data.data_json.data.data_alternate_phone;
            console.log(obj_alternate_phone);
            let all_obj_from_alternate_phone = RenderHTML_Alternate_phone_list(obj_alternate_phone);
            all_obj_from_alternate_phone.then((alternate_phone_all_obj) => {
                let { alternate_phone_html, new_obj, get_contact_by } = alternate_phone_all_obj; //get 3 value from obj
                $('tbody#show_data_alternate_phone').html(alternate_phone_html);
                console.log('pull to html success [alternate_phone]');
                // call check radio
                let check_list = CheckList_View('alternate_phone');
                let check_con_id = CheckContact_ID_Alternate_Phone(get_contact_by, get_contact_id);
                check_con_id.then(() => {
                    let standfor_update_delete = ReadyForUpdateOrDelete_Alternate_Phone(new_obj);
                });

            });
        });
    });


    $("#btn_save_alternate_phone").click(function () {  //save create/update alternate_phone
        let base_form = $("form#frm_create_alternate_phone");
        let get_form_obj = base_form.serializeJSON();
        console.log(`get_form_obj = ${get_form_obj}`);
        if (base_form.is("[update_to]")) {
            console.log("is update");
            let get_update_id = $(base_form).attr(
                "update_to"
            );
            console.log(`get_update_id = ${get_update_id}`);
            let post_update_alternate_byid = POSTFullUpdateAlternate_Phone(get_form_obj, get_update_id)
            post_update_alternate_byid.then((res_data_form_post) => {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                console.log(data);
                if (!data.data_invalid) {
                    let get_data_alternate_phone_new = data.data_alternate_phone;
                    console.log("new_obj_list_from_queryset = ", get_data_alternate_phone_new);
                    $("#show_create_alternate_phone_view").modal("hide");
                    let all_obj_from_alternate_phone = RenderHTML_Alternate_phone_list(get_data_alternate_phone_new);
                    all_obj_from_alternate_phone.then((alternate_phone_all_obj) => {
                        let { alternate_phone_html, new_obj, get_contact_by } = alternate_phone_all_obj; //get 3 value from obj
                        $('tbody#show_data_alternate_phone').html(alternate_phone_html);
                        console.log('pull to html success [alternate_phone]');
                        // call check radio
                        let check_list = CheckList_View('alternate_phone');
                        let check_con_id = CheckContact_ID_Alternate_Phone(get_contact_by, get_contact_id);
                        check_con_id.then(() => {
                            let standfor_update_delete = ReadyForUpdateOrDelete_Alternate_Phone(new_obj);
                        });
                    });
                } else {
                    let get_data_invalid = data.data_invalid;
                    console.log("invaild =", get_data_invalid);
                    let get_data_mes = data.mes_err;
                    let event_name = 'alternate_phone';
                    CallAlertRequired_ForSub(get_data_mes,event_name);
                }
            });
        } else {
            console.log("is create");
            let post_create_alternate = POSTFullCreateAlternate_Phone(get_form_obj, get_contact_id)
            post_create_alternate.then((res_data_form_post) => {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                console.log(data);
                if (!data.data_invalid) {
                    let get_data_alternate_phone_new = data.data_alternate_phone;
                    console.log("new_obj_list_from_queryset = ", get_data_alternate_phone_new);
                    $("#show_create_alternate_phone_view").modal("hide");
                    let all_obj_from_alternate_phone = RenderHTML_Alternate_phone_list(get_data_alternate_phone_new);
                    all_obj_from_alternate_phone.then((alternate_phone_all_obj) => {
                        let { alternate_phone_html, new_obj, get_contact_by } = alternate_phone_all_obj; //get 3 value from obj
                        $('tbody#show_data_alternate_phone').html(alternate_phone_html);
                        console.log('pull to html success [alternate_phone]');
                        // call check radio
                        let check_list = CheckList_View('alternate_phone');
                        let check_con_id = CheckContact_ID_Alternate_Phone(get_contact_by, get_contact_id);
                        check_con_id.then(() => {
                            let standfor_update_delete = ReadyForUpdateOrDelete_Alternate_Phone(new_obj);
                        });
                    });
                } else {
                    let get_data_invalid = data.data_invalid;
                    console.log("invaild =", get_data_invalid);
                    let get_data_mes = data.mes_err;
                    let event_name = 'alternate_phone';
                    CallAlertRequired_ForSub(get_data_mes,event_name);
                }
            });

        }
    });


    $("#btn_save_alternate_phone_change_status").click(function () {  // save change primary status | confrirm
        let get_row_id = ($('input[name="select_primary_a-p"]:checked').val())
        let this_contact_id = get_contact_id;
        console.log("this_contact_id", this_contact_id);
        console.log("get_row_id = ", get_row_id);

        if(!isNaN(get_row_id) || get_row_id) {
            let post_new_status = POSTChagePrimaryStatusAlternate_Phone(get_row_id, this_contact_id)
            post_new_status.then(function (res_data_form_post) {
                console.log(res_data_form_post);
                let { data } = res_data_form_post.data_json;
                if(!data.mes) {
                    let get_data_alternate_phone_new = data.data_alternate_phone;
                    console.log("new_obj_list_from_queryset = ", get_data_alternate_phone_new);
                    let all_obj_from_alternate_phone = RenderHTML_Alternate_phone_list(get_data_alternate_phone_new);
                    all_obj_from_alternate_phone.then((alternate_phone_all_obj) => {
                        let { alternate_phone_html, new_obj, get_contact_by } = alternate_phone_all_obj; //get 3 value from obj
                        $('tbody#show_data_alternate_phone').html(alternate_phone_html);
                        console.log('pull to html success [alternate_phone]');
                        // call check radio
                        let check_list = CheckList_View('alternate_phone');
                        check_list.then(() => {
                            console.log(data);
                            alert('change primay alternate_phone success');

                            setTimeout(function () {
                                $("#show_alternate_phone_view").modal("hide");
                            }, 1000);
                        })
                    });
    
                }else {
                    console.log(data.mes);
                    setTimeout(function () {
                        $("#show_alternate_phone_view").modal("hide");
                    }, 1000);
                }
    
            });
        }else{
            alert('Placese select a radio box');
        }
    });

});


//check to create or update form
const CheckContact_ID_Alternate_Phone = async function (contact_by, contact_id) {
    console.log("rew_contact_id = ", contact_id);
    console.log("contact_by = ", contact_by);
    try {
        if (contact_by || "") { // alternate list = null/empty
            $("a#new_alternate_phone").click(function () {
                console.log("open modal create alternate_phone");
                console.log("rew_contact_id = ", contact_by);
                $('form#frm_create_alternate_phone input:hidden[id="contact_by_mo_a-p"]').val(contact_by);
            });
        } else {
            $("a#new_alternate_phone").click(function () {
                console.log("open modal create alternate_phone");
                console.log("contact_by = ", contact_id);
                $('form#frm_create_alternate_phone input:hidden[id="contact_by_mo_a-p"]').val(contact_id);
            });
        }
    } catch (err) {
        console.log(err);
    }
};

const ReadyForUpdateOrDelete_Alternate_Phone = async function (new_obj) {
    try {
        $('a[name="update_alternate_phone"]').click(function () { //show pop-up update alternate_phone
            //get id alternate email
            let get_id_alternate_phone = + $(this).attr("target");
            console.log(`get_id_alternate_phone = ${get_id_alternate_phone}`);
            //filter obj_alternate_phone to match ID
            let filter_obj_by_id = new_obj.filter(
                (item) => item.id === get_id_alternate_phone
            );
            console.log("filter_obj_by_id = ", filter_obj_by_id);
            let push_data_to_form_alternate_phone = RenderPushDataToFormUpdateAlternate_Phone(filter_obj_by_id, get_id_alternate_phone)
            push_data_to_form_alternate_phone.then((data_alternate_phone) => {
                let get_data_alternate_phone_form = data_alternate_phone;
                console.log("data_from_render_ferch_to_field = ", get_data_alternate_phone_form);
            });
        });
        ReadyForDeleteAlternate_Phone();
    }catch (err) {
        console.log(err);
    }
};

const ReadyForDeleteAlternate_Phone = async function () {
    try {
        $('a[name="delete_alternate_phone"]').click(function () { // delete alternate_phone by id
            let get_alternate_phone_id = $(this).attr("target");
            console.log(get_alternate_phone_id);
            let chk_confirm = confirm("Are you sure to delete ?");
            if (chk_confirm) {
                let call_delete_contact = POSTFullDeleteAlternate_Phone(get_alternate_phone_id, get_contact_id);
                call_delete_contact.then((res_data_form_post) => {
                    let { data } = res_data_form_post.data_json;
                    console.log(data);
                    if (!data.mes_err) {
                        let get_data_alternate_phone_new = data.data_alternate_phone;
                        console.log("new_obj_list_from_queryset = ", get_data_alternate_phone_new);
                        let all_obj_from_alternate_phone = RenderHTML_Alternate_phone_list(get_data_alternate_phone_new);
                        all_obj_from_alternate_phone.then((alternate_phone_all_obj) => {
                            let { alternate_phone_html, new_obj, get_contact_by } = alternate_phone_all_obj; //get 3 value from obj
                            $('tbody#show_data_alternate_phone').html(alternate_phone_html);
                            console.log('pull to html success [alternate_phone]');
                            ReadyForUpdateOrDelete_Alternate_Phone();
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
