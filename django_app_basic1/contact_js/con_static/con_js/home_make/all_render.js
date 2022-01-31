// set Render Contact
const RenderContactHTML = async (data, total_data, min_page, max_page) => {
    let show_contact_list = "";
    let show_pervious_page = "";
    let show_page_run = "";
    let show_nextpage = "";

    let get_contact_obj = data;
    let get_total_contact = total_data;
    let get_min_page = min_page;
    let get_max_page = max_page;

    console.log('get_total_contact =',get_total_contact);
    console.log('get_min_page =',get_min_page);
    console.log('get_max_page =',get_max_page);
    try {
        if(get_contact_obj.length > 0) {
            await get_contact_obj.map((item) => {
                show_contact_list += `
                  <tr id="rowdata_${item.pk}">
                      <td class="align-middle">${item.hn}</td>
                      <td class="align-middle">${item.f_name_th}</td>
                      <td class="align-middle">${item.l_name_th}</td>
                      <td class="align-middle">${item.f_name_th} ${item.l_name_th}</td>
                      <td class="align-middle">${item.mobile_phone}</td>
                      <td class="align-middle">${item.nationality_title}</td>
                      <td class="align-middle">${item.email}</td>
                      <td class="align-middle">${item.gender_title}</td>
                      <td class="align-middle text-center">
                      <div class="btn-group btn-group-sm" role="group">
                      <a name="update_contact" id="edit_contact_${item.pk}" class="btn btn-sm btn-primary" target="${item.pk}"
                      data-toggle="modal" 
                      data-target="#show_update_view"
                      >
                          <i class="fas fa-edit"></i>
                      </a>
                      <a name="dalete_contact" id="delete_contact_${item.pk}" class="btn btn-sm btn-danger" target="${item.pk}">
                          <i class="fas fa-trash"></i>
                      </a>
                    </div>
                      </td>
                  </tr>
                  `;
            });
        }else {
            show_contact_list=`
            <tr>
                <td scope="row" colspan="9" class="text-center p-2">No Data Validble in Table</td>
            </tr>
            `;
        }

        show_pervious_page=`
        <li class="page-item" id="page_previous">
            <a type="button" class="page-link run_count_all_page" target_page="previous">Previous</a>
        </li>
        `;

        for (var i=get_min_page; i<= get_max_page; i++) {
            show_page_run +=`
            ${base_page === i ?     
                `
                <li class="page-item active"><a type="button" class="page-link run_count_all_page" id="run_page_${i}" target_page="${i}">${i}</a></li>
                ` 
                : 
                `
                <li class="page-item"><a type="button" class="page-link run_count_all_page" id="run_page_${i}" target_page="${i}">${i}</a></li>
                `
            }
            `;
        }

        show_nextpage=`
        <li class="page-item" id="page_next">
            <a type="button" class="page-link run_count_all_page" target_page="next">Next</a>
        </li>
        `;

        contact_for_set_html = {
            show_contact_list: show_contact_list,
            show_pervious_page: show_pervious_page,
            show_page_run: show_page_run,
            show_nextpage: show_nextpage
        };

        return contact_for_set_html;
    } catch (err) {
        console.log(err);
    }

};

const RenderPushDataToFormUpdateContact = async (obj_data) => {
    let obj_data_push_form = obj_data;
    try {
        await obj_data_push_form.map((item) => {
            for (const [key, value] of Object.entries(item)) {
                if (value || "") {
                    if (key === "nationality" || key === "gender") {
                        $(`select#${key}_update option[value=${value}]`).attr(
                            "selected",
                            "selected"
                        );
                    }else {
                        $(`form#frm_update_contact input#${key}_update`).val(value);
                        // $(`form#frm_update_contact input#${key}_update`).attr("value", value);
                    }
                } else {
                    console.log(`${key} = null`);
                }
            }
        });
        return obj_data_push_form;
    } catch (err) {
        console.log(err);
    }

};

// set Render Alternate_email
const RenderHTML_Alternate_email_list = async (obj_data) => {
    let alternate_email_html = "";
    let get_alternate_email_obj = obj_data;
    var get_contact_by = null;
    var new_obj = [];
    try {
        if (get_alternate_email_obj.length > 0) {
            $('#btn_save_alternate_email_change_status').removeClass('disabled');
            await get_alternate_email_obj.map((item, key) => {
                get_contact_by = item.contact_by;

                alternate_email_html += `
                    <tr id="rowdata_${key}">
                    ${(item.primary_status === true ?
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_a-e"  target="${item.primary_status}" value="${item.id}" checked="checked" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-check-circle set_base_icon text-success" value="${item.primary_status}"></i></td>
                        `
                        :
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_a-e" value="${item.id}" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-times-circle set_base_icon text-danger" value="${item.primary_status}"></i></td>
                        `
                    )}
                        <td class="align-middle">${item.alternate_email}</td>
                        <td class="align-middle">${item.email_type_title}</td>
                        <td class="align-middle">${item.description}</td>
                        <td class="align-middle text-center">
                            <div class="btn-group btn-group-sm" role="group">
                                <a name="update_alternate_email" id="update_alternate_email_${item.id}" class="btn btn-sm btn-primary" target="${item.id}"
                                data-toggle="modal" 
                                data-target="#show_create_alternate_email_view"
                                >
                                <i class="fas fa-edit"></i>
                                </a>
                                <a name="delete_alternate_email" id="delete_alternate_email_${item.id}" class="btn btn-sm btn-danger" target="${item.id}">
                                <i class="fas fa-trash"></i>
                                </a>
                            </div>
                        </td>
                    </tr>
                    `;
            });
        } else {
            $('#btn_save_alternate_email_change_status').addClass('disabled');
            alternate_email_html += `
                <tr>
                    <td scope="row" colspan="6" class="text-center p-2">No Data Validble in Table</td>
                </tr>
                `;
        }
        new_obj = [...obj_data];
        return { alternate_email_html, new_obj, get_contact_by };
    } catch (err) {
        console.log(err)
    }

};

const RenderPushDataToFormUpdateAlternate_Email = async (obj_data, id) => {
    $("form#frm_create_alternate_email").attr("update_to", `${id}`);
    let obj_data_push_form = obj_data;
    try {
        await obj_data_push_form.map((item) => {
            for (const [key, value] of Object.entries(item)) {
                if (key === "email_type") {
                    $(`form#frm_create_alternate_email select#${key}_mo_a-e option[value=${value}]`).attr("selected", "selected");
                    $(`form#frm_create_alternate_email select#${key}_mo_a-e option`)
                        .not(":selected")
                        .removeAttr("selected");
                } else if (key === "description") {
                    $(`form#frm_create_alternate_email textarea#${key}_mo_a-e`).val(value);
                } else if (key === "primary_status") {
                    if (value === true) {
                        $(`form#frm_create_alternate_email input:checkbox#${key}_mo_a-e`).attr(
                            "checked",
                            "checked"
                        );
                    } else {
                        $(`form#frm_create_alternate_email input:checkbox#${key}_mo_a-e`).removeAttr(
                            "checked"
                        );
                    }
                } else {
                    $(`form#frm_create_alternate_email input#${key}_mo_a-e`).val(value);
                }
            }
        });
        return { obj_data, id };
    } catch (err) {
        console.log(err);
    }

};



// set Render Alternate_phone
const RenderHTML_Alternate_phone_list = async (obj_data) => {
    let alternate_phone_html = "";
    let get_alternate_phone_obj = obj_data;
    var get_contact_by = null;
    var new_obj = [];
    try {
        if (get_alternate_phone_obj.length > 0) {
            $('#btn_save_alternate_phone_change_status').removeClass('disabled');
            await get_alternate_phone_obj.map((item, key) => {
                get_contact_by = item.contact_by;

                alternate_phone_html += `
                    <tr id="rowdata_${key}">
                    ${(item.primary_status === true ?
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_a-p"  target="${item.primary_status}" value="${item.id}" checked="checked" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-check-circle set_base_icon text-success" value="${item.primary_status}"></i></td>
                        `
                        :
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_a-p" value="${item.id}" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-times-circle set_base_icon text-danger" value="${item.primary_status}"></i></td>
                        `
                    )}
                        <td class="align-middle">${item.alternate_phone}</td>
                        <td class="align-middle">${item.phone_type_title}</td>
                        <td class="align-middle">${item.description}</td>
                        <td class="align-middle text-center">
                            <div class="btn-group btn-group-sm" role="group">
                                <a name="update_alternate_phone" id="update_alternate_phone_${item.id}" class="btn btn-sm btn-primary" target="${item.id}"
                                data-toggle="modal" 
                                data-target="#show_create_alternate_phone_view"
                                >
                                <i class="fas fa-edit"></i>
                                </a>
                                <a name="delete_alternate_phone" id="delete_alternate_phone_${item.id}" class="btn btn-sm btn-danger" target="${item.id}">
                                <i class="fas fa-trash"></i>
                                </a>
                            </div>
                        </td>
                    </tr>
                    `;
            });
        } else {
            $('#btn_save_alternate_phone_change_status').addClass('disabled');
            alternate_phone_html += `
                <tr>
                    <td scope="row" colspan="6" class="text-center p-2">No Data Validble in Table</td>
                </tr>
                `;
        }
        new_obj = [...obj_data];
        return { alternate_phone_html, new_obj, get_contact_by };
    } catch (err) {
        console.log(err)
    }

};

const RenderPushDataToFormUpdateAlternate_Phone = async (obj_data, id) => {
    $("form#frm_create_alternate_phone").attr("update_to", `${id}`);
    let obj_data_push_form = obj_data;
    try {
        await obj_data_push_form.map((item) => {
            for (const [key, value] of Object.entries(item)) {
                if (key === "phone_type") {
                    $(`form#frm_create_alternate_phone select#${key}_mo_a-p option[value=${value}]`).attr("selected", "selected");
                    $(`form#frm_create_alternate_phone select#${key}_mo_a-p option`)
                        .not(":selected")
                        .removeAttr("selected");
                } else if (key === "description") {
                    $(`form#frm_create_alternate_phone textarea#${key}_mo_a-p`).val(value);
                } else if (key === "primary_status") {
                    if (value === true) {
                        $(`form#frm_create_alternate_phone input:checkbox#${key}_mo_a-p`).attr(
                            "checked",
                            "checked"
                        );
                    } else {
                        $(`form#frm_create_alternate_phone input:checkbox#${key}_mo_a-p`).removeAttr(
                            "checked"
                        );
                    }
                } else {
                    $(`form#frm_create_alternate_phone input#${key}_mo_a-p`).val(value);
                }
            }
        });
        return { obj_data, id };
    } catch (err) {
        console.log(err);
    }

};



// set Render Personal_Address
const RenderHTML_Personal_address_list = async (obj_data) => {
    let personal_address_html = "";
    let get_personal_address_obj = obj_data;
    var get_contact_by = null;
    var new_obj = [];
    try {
        if (get_personal_address_obj.length > 0) {
            $('#btn_save_personal_address_change_status').removeClass('disabled');
            await get_personal_address_obj.map((item, key) => {
                get_contact_by = item.contact_by;

                personal_address_html += `
                    <tr id="rowdata_${key}">
                    ${(item.primary_status === true ?
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_p-a"  target="${item.primary_status}" value="${item.id}" checked="checked" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-check-circle set_base_icon text-success" value="${item.primary_status}"></i></td>
                        `
                        :
                        `
                        <td class="align-middle text-center">
                            <div class="form-check">
                                <input class="form-check-input position-static" type="radio" name="select_primary_p-a" value="${item.id}" >
                            </div>
                        </td>
                        <td class="align-middle text-center"><i class="fas fa-times-circle set_base_icon text-danger" value="${item.primary_status}"></i></td>
                        `
                    )}
                        <td class="align-middle">${item.address_1}</td>
                        <td class="align-middle">${item.address_2}</td>
                        <td class="align-middle">${item.building}</td>
                        <td class="align-middle">${item.district}</td>
                        <td class="align-middle">${item.city}</td>
                        <td class="align-middle">${item.province}</td>
                        <td class="align-middle">${item.zipcode}</td>
                        <td class="align-middle text-center">
                        ${(item.alignment_status === true ? 
                            `
                            <i class="fas fa-check-circle set_base_icon text-success" value="${item.alignment_status}"></i>
                            `
                            :
                            `
                            <i class="fas fa-times-circle set_base_icon text-danger" value="${item.alignment_status}"></i>
                            `
                        )}
                        </td>
                        <td class="align-middle text-center">
                            <div class="btn-group btn-group-sm" role="group">
                                <a name="update_personal_address" id="update_personal_address_${item.id}" class="btn btn-sm btn-primary" target="${item.id}"
                                data-toggle="modal" 
                                data-target="#show_create_personal_address_view"
                                >
                                <i class="fas fa-edit"></i>
                                </a>
                                <a name="delete_personal_address" id="delete_personal_address_${item.id}" class="btn btn-sm btn-danger" target="${item.id}">
                                <i class="fas fa-trash"></i>
                                </a>
                            </div>
                        </td>
                    </tr>
                    `;
            });
        } else {
            $('#btn_save_personal_address_change_status').addClass('disabled');
            personal_address_html += `
                <tr>
                    <td scope="row" colspan="11" class="text-center p-2">No Data Validble in Table</td>
                </tr>
                `;
        }
        new_obj = [...obj_data];
        return { personal_address_html, new_obj, get_contact_by };
    } catch (err) {
        console.log(err)
    }

};

const RenderPushDataToFormUpdatePersonal_Address = async (obj_data, id) => {
    $("form#frm_create_personal_address").attr("update_to", `${id}`);
    let obj_data_push_form = obj_data;
    try {
        await obj_data_push_form.map((item) => {
            for (const [key, value] of Object.entries(item)) {
                if (key === "primary_status" || key === "alignment_status") {
                    if (value === true) {
                        $(`form#frm_create_personal_address input:checkbox#${key}_mo_p-a`).attr(
                            "checked",
                            "checked"
                        );
                    } else {
                        $(`form#frm_create_personal_address input:checkbox#${key}_mo_p-a`).removeAttr(
                            "checked"
                        );
                    }
                } else {
                    $(`form#frm_create_personal_address input#${key}_mo_p-a`).val(value);
                }
            }
        });
        return { obj_data, id };
    } catch (err) {
        console.log(err);
    }

};