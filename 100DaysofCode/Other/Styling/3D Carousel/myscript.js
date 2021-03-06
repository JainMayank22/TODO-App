// // If we decide on changing the width of the panel or the number of panels, 
// // plug in those two variables into our equation 
// var tz = Math.round( ( cellSize / 2 ) /
//   Math.tan( ( ( Math.PI * 2 ) / numberOfCells ) / 2 ) );
// // or simplified to
// var tz = Math.round( ( cellSize / 2 ) /  Math.tan( Math.PI / numberOfCells ) );



var carousel = document.querySelector('.carousel');
var cellCount = 9;
var selectedIndex = 0;

function rotateCarousel() {
  var angle = selectedIndex / cellCount * -360;
  carousel.style.transform = 'translateZ(-288px) rotateY(' + angle + 'deg)';
}

var prevButton = document.querySelector('.previous-button');
prevButton.addEventListener( 'click', function() {
  selectedIndex--;
  rotateCarousel();
});

var nextButton = document.querySelector('.next-button');
nextButton.addEventListener( 'click', function() {
  selectedIndex++;
  rotateCarousel();
});