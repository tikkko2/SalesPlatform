$(document).ready(function () {

    var menu = $(".menu");
    var hamburger = $(".category-container");
    var menuOpen;

    function openMenu() {
        menu.css("left", "0px");
        menuOpen = true;
    }

    function closeMenu() {
        menu.css("left", "-320px");
        line.css("background", "#BCAD90");
        menuOpen = false;
    }

    function toggleMenu() {
        if (menuOpen) {
            closeMenu();
        } else {
            openMenu();
        }
    }

    hamburger.on({
        mouseenter: function () {
            openMenu();
        }
    });

    menu.on({
        mouseleave: function () {
            closeMenu();
        }

    });

    hamburger.on({
        click: function () {
            toggleMenu();
        }
    })

    function changeRange() {
        let range = document.getElementById("customRange1");
        let max_value = document.getElementById("max_value");
        max_value.innerText = "$" + (parseInt(range.value) + 15).toString();
    }

});