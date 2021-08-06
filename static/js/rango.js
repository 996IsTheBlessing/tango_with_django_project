var $$ = function (id) {
    return document.getElementById(id);
}

var follow = function () {
    if ($$("like-icon").style.color == "black") {
        $$("like-icon").style.color = "#3a62d7"
        $$("like-icon").style.fill = "#3a62d7"
        $$("like_count").innerHTML = parseInt($$("like_count").innerHTML) + 1
    } else {
        $$("like-icon").style.fill = ""
        $$("like-icon").style.color = "black"
        $$("like_count").innerHTML = parseInt($$("like_count").innerHTML) - 1
    }
    
}

var goToLogin = function () {
    location.href="http://127.0.0.1:8000/rango/login";
}

var goToRegister = function () {
    location.href="http://127.0.0.1:8000/rango/register";
}