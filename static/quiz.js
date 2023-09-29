
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

  function adjustContentMainHeight() {
    var contentMain = document.querySelector('.content-main');
    var elements = contentMain.children;
  
    var totalHeight = 0;
    for (var i = 0; i < elements.length; i++) {
      totalHeight += elements[i].offsetHeight;
    }
  
    contentMain.style.height = totalHeight + 'px';
  }

  // Example: Adding a new element dynamically
var newElement = document.createElement('div');
document.querySelector('.content-main')

adjustContentMainHeight(); // Call the function to adjust the height



// this helps dynamically adjust the position of the stopwatch






  
