function openApp() {
  window.open("app.html", "_blank");
}

const waterSound = new Audio('thailand-eas-alarm-2006-266492.mp3');


function playMusic() {
    waterSound.play();
}


window.onload = function() {
    waterSound.play();
}