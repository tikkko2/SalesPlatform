let mini2 = false;
toggleSidebar2();
function toggleSidebar2() {
    if (mini2) {
        document.getElementById("mySidebar2").style.width = "350px";
        document.getElementById("before_open").style.display = "none";
        document.getElementById("after_open").style.display = "";
        mini2 = false;
    } else {
        document.getElementById("mySidebar2").style.width = "50px";
        document.getElementById("before_open").style.display = "";
        document.getElementById("after_open").style.display = "none";
        mini2 = true;
    }
}

function change_image(image) {
    var container = document.getElementById("main-image");
    container.src = image.src;
}

document.addEventListener("DOMContentLoaded", function (event) {
});