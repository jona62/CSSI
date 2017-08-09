function DisplayPoem(Noun,Pronoun,Adjective,Verb,Place) {
    var poem = "My student " + Noun + Pronoun + Adjective + Place + ", standing proud <br/> is a fine example for the crowd.";
    $('#output').html(poem);
}

$('.submitName').click(function(){
    var passThis = $('input[name="Noun","Pronoun","Adjective","Verb","Place"]').val();
    DisplayPoem(passThis);
