function Navo(){
  document.getElementById('navBar').style.width="200px"
}

function Navc(){
  document.getElementById('navBar').style.width="0px"
}

// AT PAGE 920px needs to refresh
// The below is a temporary fix, quite slow
window.onresize = function(){ location.reload(); }
