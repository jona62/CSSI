function DisplayStory(noun, noun2, noun3, noun_plural, adjective) {
    var madlib1 = "Be kind to your " + noun + "-footed " + noun_plural +
    "<br/> For a duck may be somebody`s " + noun2 + ", Be kind to your " + noun_plural +
    "<br/> in a place Where the weather is always " + adjective + " You may think that this is the <br/>" +
    noun3 + ", Well it is. ";
    $('#output').html(madlib1);
}

$('#submit').click(function(){
    var passThis = $('input[name="noun"]').val();
      var passThis1 = $('input[name="noun2"]').val();
        var passThis2 = $('input[name="noun3"]').val();
          var passThis3 = $('input[name="noun_plural"]').val();
            var passThis4 = $('input[name="adjective"]').val();
    DisplayStory(passThis, passThis1, passThis2, passThis3, passThis4);
});
