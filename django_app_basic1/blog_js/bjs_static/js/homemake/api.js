
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

function updateToken(){
    $("[name='csrfmiddlewaretoken']").val(getCookie("csrftoken"));
}

const fetchData = (inURL, inMethod, inDataForm) => {
    return new Promise((resolve, reject) => {
        try 
        {   
            let token = getCookie("csrftoken");
            if (token != null){
                if(inMethod.toUpperCase() !== "GET"){
                    let formData = new FormData();
                    for ( var key in inDataForm ) {
                        formData.append(key, inDataForm[key]);
                    }
                    fetch(`${inURL}`,{
                        body: formData,
                        method: inMethod,
                        headers: {
                        //   'Content-Type': "application/json",
                          'X-CSRFToken': `${token}`
                        },
                        credentials: 'include', // This is set on request
                      }
                    )
                    .then(response => {
                        if (response.status > 400) {
                            return null;
                            // return { success: false, message: "Fetch Error!"};
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log("data =", data)
                        // console.log("data.data.length = ", data.data.length)
                        if(data) {
                            if((data["status"] && data["status"] === "success") || !data["status"]){
                                return resolve({ success: true, message: "Fetch Success!", data_json:data });
                            }
                            else {
                                return resolve({ success: false, message: "Fetch Error!", data_json:data });
                            }
                        }
                        else {
                            return resolve({ success: false, message: "Fetch Error!", data_json:{} });
                        }
                    });
                }
                else{
                    fetch(`${inURL}`,{
                        method: inMethod,
                        headers: {
                            'Content-Type': "application/json",
                            'X-CSRFToken': `${token}`
                          },
                        credentials: 'include', // This is set on request
                      }
                    )
                    .then(response => {
                        if (response.status > 400) {
                            // return { success: false, message: "Fetch Error!" };
                            return null;
                        }
                        return response.json();
                    })
                    .then(data => {
                        // return resolve({ success: true, message: "Fetch Success!", data_json:data });
                        if(data){
                            if((data["status"] && data["status"] === "success") || !data["status"]){
                                return resolve({ success: true, message: "Fetch Success!", data_json:data });
                            }
                            else {
                                return resolve({ success: false, message: "Fetch Error!", data_json:{} });
                            }
                        }
                        else {
                            return resolve({ success: false, message: "Fetch Error!", data_json:{} });
                        }
                    });
                }
            }
            else{
                return resolve( { success: false, message: "Token Not Found!" });
            }
        } catch (error) {
            return resolve({ success: false, message: error.toString(), data_json: {} })
        }
    })
}