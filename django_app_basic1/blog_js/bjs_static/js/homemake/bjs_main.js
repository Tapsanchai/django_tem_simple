$(document).ready(() => {

  Get_Search_tag = (key_tag) => {
    // alert('value = '+ key_txt);
    let get_tag_value = key_tag;
    GetTagSearch(get_tag_value);
  };

  $("#btn_search").click(() => {
    // let get_textbox_value = document.getElementById("search_txt").value;
    // alert('text = '+ get_textbox_value);
    let get_textbox_value_obj = $("#search_txt").serializeJSON();
    console.log("obj = " + get_textbox_value_obj);
    let textbox_value_jsonstring = JSON.stringify(get_textbox_value_obj);
    console.log("stringify = " + textbox_value_jsonstring);
    GetTextBoxSearch(get_textbox_value_obj);
  });

  $("#user_login").click(() => {
    let get_login_obj = $("input.validate_login").serializeJSON();
    // console.log("obj = " ,get_login_obj);
    let convert_obj = JSON.parse(get_login_obj);
    console.log("convert_obj = " ,convert_obj);
    GetLoginForm(get_login_obj);
    $.each(convert_obj, (key, mes) => {
        // console.log("key = " ,key);
        // console.log("mes = " ,mes);
        if(mes || ''){ 
            $(`input[name="${key}"]`)
            .removeClass("is-invalid")
            .addClass("is-valid");
        }
    });
  });

  $("#user_logout").click(() => {
    GetLogout();
  });
});
