var get_contact_id;

const CallAlertRequired_ForSub  = async (mes_err, event_name) => {
  try {
      let select_endwith_text = {
        alternate_email: 'mo_a-e',
        alternate_phone: 'mo_a-p',
        personal_address: 'mo_p-a',
      };
      let call_event_name = event_name;
      let call_mes;
      let build_tag;
      let get_field_name;

      let build_chk_form_fields_list = [];
      let build_get_field_name_list = [];
      let build_get_new_obj = {};

      let get_fields = $(`#frm_create_${call_event_name}`).serializeArray();
      get_fields.map((field) => {return build_chk_form_fields_list.push(field.name);});

      await $.each(mes_err, (field_name, obJ_item) => {
        // console.log(`field_name = ${field_name}  obJ_item = ${obJ_item}`);
        build_get_field_name_list.push(field_name);
        get_field_name = field_name; 

         obJ_item.map((item) => {
          build_get_new_obj[get_field_name] = item;
        });

      });
      console.log('build_get_new_obj = ', build_get_new_obj);
      console.log('build_get_field_name_list = ', build_get_field_name_list);

      await build_chk_form_fields_list.map((key) => {
          if(build_get_field_name_list.includes(key)) { 
              call_mes = build_get_new_obj[key].message;
              // console.log(call_mes);
              build_tag = `<div class="invalid-feedback set_err_for_sub d-block">${call_mes}</div>`;
              $(`#${key}_${select_endwith_text[call_event_name]}`).removeClass('is-valid').addClass('is-invalid').focus();
              $(`div[err_for="${key}_${select_endwith_text[call_event_name]}"]`).html(build_tag);
          }else { 
              if ($(`#${key}_${select_endwith_text[call_event_name]}`).hasClass('is-invalid')) {
                  $(`#${key}_${select_endwith_text[call_event_name]}`).removeClass('is-invalid').addClass('is-valid');
                  $(`div[err_for="${key}_${select_endwith_text[call_event_name]}"] > div`).remove();
              }else {
                  $(`#${key}_${select_endwith_text[call_event_name]}`).removeClass([ "is-invalid", "is-valid" ]);
                  $(`div[err_for="${key}_${select_endwith_text[call_event_name]}"] > div`).remove();
              }
          }
      });
      console.log('show alert success');
      return true;
  }catch (err) {
      console.log(err);
  }
};

// click chanage radio checked in table list
const CheckList_View = async function (module_nane) { 
  let chk_list_select = ['alternate_email','alternate_phone','personal_address'];
  try {
    if (chk_list_select.includes(module_nane)) {
      console.log('module_nane = ', module_nane);
      $("tr td.align-middle").not(".text-center").addClass("pl-2");
    
      $("input:radio").change(function () {
        $("input:radio:checked").attr("target", "true");
        $("input:radio").not(":checked").removeAttr("target");
      });
    }
  }catch (err) {
    console.log(err);
  }
};

$(document).ready(() => {

  // show table contact list on Index
  (async = () => {
    const get_load = LoadAllContact();
  })();




});
