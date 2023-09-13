const start_btn = document.getElementById("start");
start_btn.addEventListener("click", start);
function start(){
    var startTime = new Date().getTime();
    timer = setInterval(() =>{
    var now = new Date().getTime();
    var passed_time = now - startTime;
    var places = 2
    var hours = String(Math.floor((passed_time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))).padStart(places, '0');
    var minutes = String(Math.floor((passed_time % (1000 * 60 * 60)) / (1000 * 60))).padStart(places, '0');
    var seconds = String(Math.floor((passed_time % (1000 * 60)) / 1000)).padStart(places, '0');
    document.querySelector(".text-bg-light").innerHTML = hours+" : "+minutes+" : "+seconds
    },1000);
    if (start_btn.innerHTML==="Start"){
        start_btn.removeEventListener("click", start);
        start_btn.addEventListener("click", reset);
        start_btn.innerHTML = "Reset"
    }
}

function reset(){
    clearInterval(timer);
    start();
}