
document.addEventListener('DOMContentLoaded', function() {
    var optionButtons = document.querySelectorAll('.question-box option-new button');
    optionButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        optionButtons.forEach(function(btn) {
          btn.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  });

  