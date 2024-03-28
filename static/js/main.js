const menu = document.querySelector("#menu");
const dropDown = document.querySelector('#dropdown')
const sidebar = document.querySelector(".sidebar");
const dropDownBg=document.querySelector(".dropdown-bg")

// console.log(menu,dropDown,sidebar)

menu.addEventListener('click', function () {
    sidebar.classList.toggle("show-sidebar");
});

dropDown.addEventListener('click',function(){
    dropDownBg.classList.toggle("show-dropdown")
})