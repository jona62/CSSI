/*function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
}
*/
$("div").click(function(){
   $("#div1").fadeTo("slow", 0.15);
   $("#div2").fadeTo("slow", 0.4);
