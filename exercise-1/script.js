/* You will save your code during today's demos and exercises here. */
function hide(){
$('.frame').hide();
hide();
}

function show(){
$('.frame').show();
show();
}

$('.frame').fadeOut(4000,'swing');
function fadeImage() {
  $('.frame').fadeToggle();
}

function setupHandlers() {
  $('#android').on('click', fadeImage);
}

$(document).ready(setupHandlers);
