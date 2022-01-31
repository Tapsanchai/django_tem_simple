// import {GetPromise} from './bjs_call_queryset.js'

// const GetPromise = () => {
//     fetchData("render_all/?id=1", "POST", {}).then(res => {
//         console.log(res)
//         // return res
//     });
// }
const Render_Blogs = async (query_obj) => {
    let repon_res = query_obj;
    let set_hashtags = "";
    let set_blogs = "";

    repon_res.map((item) => {
        set_hashtags = item.blog_hashtags;

        // console.log(set_hashtags);
        // Set Text HTML
        
        set_blogs += `
        <div class="col-sm-12 col-md-6" >
            <div class="card shadow-sm mb-3" >
                <div class="card-header fs-5 font-weight-bolder bg-dark text-white">
                    <span class="" id="show_title_${item.id}">${item.title
            }</span> <span class="text-info fs-6 ms-1" id="show_type_${item.id}">(${item.blog_type
            })</span>
                </div>
                <div class="card-body" >
                    <div class="card-title fs-6 text-muted font-italic">
                        <span class="show_datetime" id="show_datetime_${item.id}">${item.time_updated}
            }</span> | <span class="" id="show_create_by_${item.id}">${item.create_by
            }</span>
                    </div>
                    <p class="card-text fs-6 text-truncate" id="show_content_${item.id}">${item.content
            }</p>
                    <hr>
        
                    <p class="" id="show_hashtags_${item.id}">
                    ${set_hashtags
                .map(
                    (tag, index) =>
                        `<a id="search_tag_${index}" class="text-decoration-none text-primary mr-2" onclick="Get_Search_tag('${tag}')">    
                            #${tag}
                        </a>`
                )
                .join("")}
                    </p>
                    
                    <div class="test_authen" >
                        <div class="btn-group" role="group" >
                            <a name="edit_blog_${item.id}" id="edit_blog_${item.id
            }" class="btn btn-sm btn-secondary text-uppercase edit_blog" value="${item.id
            }">
                                edit
                            </a>
                            <a name="delete_blog_${item.id}" id="delete_blog_${item.id
            }" class="btn btn-sm btn-danger text-uppercase delete_blog" value="${item.id
            }">
                                delete
                            </a> 
                        </div>
                    </div>

                </div>
            </div>
        </div>
        `;
    });
    $("#TestRender").html(set_blogs);
    console.log("Render Table Successs!!");

    $("a.edit_blog").click(function () {
        var get_id = $(this).attr("value");
        console.log(get_id);
        link = `update_blog/${get_id}/`;
        window.location.href = link;
    });

    $("a.delete_blog").click(function () {
        var get_id = $(this).attr("value");
        console.log(get_id);
        let confirm_todo = confirm("Do you want to delete this BLOG?");
        let message;
        if (confirm_todo) {
            message = "BLOG is Deleted :(";
            // GET ID too Delete Blog
            DeleteBy_ID(get_id).then(() => {
                alert(message);
            });
        } else {
            message = "OK, You don't want to delete this BLOG ;)";
            alert(message);
        }
    });

    var get_datetime = $('span.show_datetime').text();
    GetDetetimeBlogs(get_datetime);
    // console.log(`datetime = ${get_datetime}`);

    return "Render Blog Success!!";
};

const GetAllQuerySet_Async = async () => {
    res = await fetchData("render_blogs/?query=all", "GET", {});
    console.log(res);
    if (res.success) {
        let push_to_render = JSON.parse(res.data_json.data);
        console.log(push_to_render);
        await Render_Blogs(push_to_render).then(() => {
            NewShowStatus().then((response) => {
                let chk_to_remove = response ? $(".test_authen").remove() : null;
                console.log("remove --> ", chk_to_remove);
            });
        });
    } else {        
        console.log("Render Error!!");
    }
};

const DeleteBy_ID = async (id) => {
    console.log("Come to function delete");
    res = await fetchData(`delete_blog/?id=${id}`, "GET", {});
    console.log(res);
    if (res.success) {
        GetAllQuerySet_Async();
    } else {
        console.log("Refetch Render Error!!");
    }
};

const GetTextBoxSearch = async (txt_obj) => {
    console.log("come to function search by textbox");
    let get_value_obj = JSON.parse(txt_obj);
    if (get_value_obj.search_txt.trim().length > 0) {
        console.log("text =" + get_value_obj.search_txt.trim());
        let awrsome_value = get_value_obj.search_txt.trim();
        if (!isNaN(awrsome_value)) {
            res = await fetchData(`render_blogs/?id=${awrsome_value}`, "GET", {});
        } else {
            res = await fetchData(`render_blogs/?txt=${awrsome_value}`, "GET", {});
        }
        console.log(res);
        if (res.success) {
            if (res.data_json.data.length == 0) {
                alert("Not Found Blog..");
            } else {
                let push_to_render = res.data_json.data;
                await Render_Blogs(push_to_render).then(() => {
                    NewShowStatus().then((response) => {
                        let chk_to_remove = response ? $(".test_authen").remove() : null;
                        console.log("remove --> ", chk_to_remove);
                    });
                });
            }
        } else {
            console.log("Render Error!! <search_txt>");
        }
    } else {
        GetAllQuerySet_Async();
    }
};

const GetTagSearch = async (tag) => {
    console.log("come to function search by tag");
    let get_value_tag = tag;
    console.log("tag search =" + get_value_tag);
    res = await fetchData(`render_blogs/?tag=${get_value_tag}`, "GET", {});
    console.log(res);
    if (res.success) {
        if (res.data_json.data.length == 0) {
            alert("Not Found Blog..");
        } else {
            let push_to_render = res.data_json.data;
            await Render_Blogs(push_to_render).then(() => {
                NewShowStatus().then((response) => {
                    let chk_to_remove = response ? $(".test_authen").remove() : null;
                    console.log("remove --> ", chk_to_remove);
                });
            });
        }
    } else {
        console.log("Render Error!! <search_tag>");
    }
};

const GetLoginForm = async (user_object) => {
    console.log("come to function login");
    let get_value_login = user_object;
    console.log("login data =" + get_value_login);


    res = await fetchData("login/", "POST", { data: get_value_login });
    console.log(res);
    if (res.success) {
        if (res.data_json.data !== null) {
            link = res.data_json.url;
            console.log("go to URL =" + link);
            window.location.href = res.data_json.url;
            alert("Login Success!!");
        } else {
            if (res.data_json.messages_error) {
                console.log("have some error");
                let get_all_messages = res.data_json.messages_error;

                $.each(get_all_messages, (field_name, mes) => {
                        $(`input[name="${field_name}"]`)
                        .removeClass("is-valid").addClass("is-invalid").focus();
                        mes.map((item) => {
                            if (field_name === "__all__") {
                                $(`input.validate_login`)
                                .removeClass("is-valid").addClass("is-invalid").focus();
                                $('div.make_validate').text("");
                                alert(item.message);
                            }else{
                                $(`.make_validate[validate="${field_name}_error"]`).text(item.message)
                            }
                        });
                    });
                }   
            else {
                console.log("Login error: " + res.success);
            }
        }
    }
};

    const GetLogout = async () => {
        console.log("come to function logout");
        res = await fetchData("logout/", "POST", {});
        console.log(res);
        if (res.success) {
            if (res.data_json.data === null) {
                link = res.data_json.url;
                console.log("go to URL =" + link);
                window.location.href = res.data_json.url;
                alert("Logout Success!!");
            }
        } else {
            console.log("Logout error: " + res.success);
        }
    };

    // Call Function Get Queryset JSON.type | When Click Button
    $(document).ready(() => {
        // GET Queryset
        GetAllQuerySet_Async();
        // NewShowStatus();
    });
