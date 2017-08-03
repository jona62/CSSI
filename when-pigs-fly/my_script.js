function showWhenClicked(){
  $("#pig").show();
}
function hideWhenClicked(){
  $("#pig2").hide();
}


function fly2 (){
  $("#pig2").animate ({left: '1750px'}, 1500);
}
function flyWhenClicked(){
  $('#pig').animate ({left:'1750px'}, "slow", fly2);
}

function setup(){
  $('#showPig').click(showWhenClicked);
  $('#hidePig').click(hideWhenClicked);
  $('#flyPig').click(flyWhenClicked);
}
$(document).ready(setup);
