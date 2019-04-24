var likes = 1;
  var dislikes = 1;
  function like() {
    document.getElementById("show_like").innerHTML=likes;
    likes=likes+1;
  }
  function dislike() {
    document.getElementById("show_dislike").innerHTML=dislikes;
    dislikes=dislikes+1;
  }