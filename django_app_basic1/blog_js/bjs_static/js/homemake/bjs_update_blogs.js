const UpdateBy_ID = async (form_data, id) => {
  console.log("Come to function Update");
  let data = form_data;
  console.log(data);

  res = await fetchData(`/blog_js/update_blog/${id}/`, "POST", { data: data });
  console.log(res);
  if (res.success) {
    if (res.data_json.data === null) {
      link = res.data_json.url;
      console.log("go to URL =" + link);
      window.location.href = res.data_json.url;
    }
  } else {
    console.log("Update blog error: " + res.success);
  }
};

$(document).ready(() => {
  $("#submit_frm_update_blogs").click(() => {
    // alert('click get form')
    let get_id = $("#frm_update_blogs").attr("blog_id");
    console.log("get_id =" + get_id);
    var obj = $("#frm_update_blogs").serializeJSON();
    var form_jsonstring = JSON.stringify(obj);
    console.log("Get Form obj=" + obj);
    console.log("Get Form jsonstring=" + form_jsonstring);

    UpdateBy_ID(obj, get_id);
  });
});
