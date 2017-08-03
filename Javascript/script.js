function Taskdone(val)
  {
    var change = document.getElementById(val).style.textDecoration;
    if(change == 'line-through')
    {
      document.getElementById(val).style.textDecoration = 'none';
    }
    else
    {
      document.getElementById(val).style.textDecoration = 'line-through';
    }
 }


function ClearAll()
 {
   names= $(".task");
   names.css("text-decoration", "none");
 }
 /* {
  names=document.getElementsByClassName("task");
  var nm=names.length
 for (i=0; i<nm; i++)
 {

 names[i].style.textDecoration="none";
 }
  }*/
  function addListItem(text){
    list = document.querySelector('ol');
    item = document.createElement('li');
    item.innerText = text;
    list.appendChild(item);
  }


function pop_up(){
var i=prompt("Enter the Item to add to Bucket List");
addListItem(i);
}
