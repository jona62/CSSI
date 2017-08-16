/*var filter = ["ass", "piss"];
var comment = document.getElementById("#comment-post-text").innerHTML;

  for (var i=0; i<filter.length; i++){
    var filter_word = filter[i];
    var replace = '*'.repeat (filter_word.length);
  }
*/
$(document).ready(function(){
    $("button").click(function(){
        var div = $("div");
        div.animate({height: '300px', opacity: '0.4'}, "slow");
        div.animate({width: '300px', opacity: '0.8'}, "slow");
        div.animate({height: '100px', opacity: '0.4'}, "slow");
        div.animate({width: '100px', opacity: '0.8'}, "slow");
    });
});
