
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
function adjustElementsPosition() {
  var questionBox = document.querySelector('.question-box');
  var stopwatch = document.querySelector('.stopwatch');

  var baseFontSizePx = 16; // 1 rem = 16 px

  var questionBoxRect = questionBox.getBoundingClientRect();
  var questionBoxTop = questionBoxRect.top / baseFontSizePx; // Convert to rem
  var questionBoxHeight = questionBox.offsetHeight / baseFontSizePx; // Convert to rem

  // Set the top position of stopwatch to maintain a 10px gap below question-box
  stopwatch.style.top = (questionBoxTop + questionBoxHeight + 0.625) + 'rem'; // 10px in rem
}

// Call the function initially
adjustElementsPosition();

// Add an event listener for changes in question-box content
document.querySelector('.question-box').addEventListener('input', adjustElementsPosition);

// Add an event listener for window resize
window.addEventListener('resize', function() {
  setTimeout(adjustElementsPosition, 50); // Recalculate position with slight delay
});

// Add an event listener for window focus
window.addEventListener('focus', function() {
  setTimeout(adjustElementsPosition, 50); // Recalculate position with slight delay
});





  
