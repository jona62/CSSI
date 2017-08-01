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
