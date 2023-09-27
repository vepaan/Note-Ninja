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
}

document.addEventListener('DOMContentLoaded', function() {
    var optionButtons = document.querySelectorAll('.question-box option-new button');
    start();
    optionButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        optionButtons.forEach(function(btn) {
          btn.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  });

  