let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let subItem = document.querySelector(".sub-item");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

var subBtns = document.querySelectorAll(".sub-btn");
for (var i = 0; i < subBtns.length; i++) {
    subBtns[i].addEventListener("click", function () {
        var subMenu = this.parentNode.querySelector(".sub-menu");
        subMenu.classList.toggle("sub-menu-open");
        var dropdownrotate = this.querySelector(".dropdown-open");
        dropdownrotate.classList.toggle("rotate");
    });
}

let dropdowns = document.querySelectorAll(".dropdown-open");
function dropdownClose() {
    dropdowns.forEach((dropdown) => {
        dropdown.style.backgroundColor = "transparent";
        dropdown.style.color = "transparent";
    });
}
dropdownClose();
function dropdownOpen() {
    dropdowns.forEach((dropdown) => {
        dropdown.style.backgroundColor = "";
        dropdown.style.color = "";
    });
}

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("fa-bars", "fa-bars-staggered");//replacing the icons class
        dropdownOpen();
    } else {
        closeBtn.classList.replace("fa-bars-staggered", "fa-bars");//replacing the icons class
        dropdownClose();
    }
}

$(document).ready(function () {
    $('.custom-tooltip').tooltip({
        template: '<div class="tooltip custom-tooltip-style" role="tooltip"><div class="tooltip-inner"></div></div>'
    });
});