// -----------------by atul -----------------------------------


let arnav_login = document.querySelector("#main-nav-bar-login");
let login_main_box = document.querySelector(".atul_login_box");
let login_main_box_closeBtn = document.querySelector("#login_close");
let modal_body_container = document.querySelector(".modal-body-container");
let search_search_closeBtn = document.querySelector("#search p");
let search_icon_navbar = document.querySelector(".search-icon-navbar");
let main_page_menu_btn = document.querySelector(".main-nav-menu");
let inside_menu = document.querySelector(".inside_menu");
let inside_menu_navbar_close = document.querySelector(".inside_menu_navbar_close");

main_page_menu_btn.addEventListener("click", () => {
    console.log("clicked");
    inside_menu.classList.add("popUPOfInsideMenu");
})

inside_menu_navbar_close.addEventListener("click", () => {
    console.log("clicked");
    inside_menu.classList.remove("popUPOfInsideMenu");
})

search_icon_navbar.addEventListener("click", () => {
    console.log("clicked");
    modal_body_container.classList.add("popUPOfSearch");
})

search_search_closeBtn.addEventListener("click", () => {
    console.log("clicked");
    modal_body_container.classList.remove("popUPOfSearch");
})


arnav_login.addEventListener("click", () => {
    login_main_box.classList.add("popUPOfLoginBox");

})
login_main_box_closeBtn.addEventListener("click", () => {
    login_main_box.classList.remove("popUPOfLoginBox");
})

