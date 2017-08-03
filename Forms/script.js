var user_text = $('input').val();
$('#results').text(pigLatin(user_text));

 function greeting() {
    var userName = $('#username').val();
    alert("Hi "  + userName + ", welcome to my page!");
    $("#top_greeting").text("Welcome " + userName +"!");
 }

 function setup() {
    $("#ok_button").click(greeting);
 }

 $(document).ready(setup)
