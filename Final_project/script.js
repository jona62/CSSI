function greeting()
{
  var userName= $ ('#username').val();
  $("#comments").append(userName + " <br>");
}

function setup(){
  $("#comment_button").click(greeting);
}

$(document).ready(setup)
