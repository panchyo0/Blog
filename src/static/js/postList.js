//add for current image shadow when hover
$(document).ready(function(){
  $( ".thumbnail" ).hover(
  function() {
    var content=$( this ).find('#post-content');
    var shadow=$( this ).find('.no-shadow');
    content.css({"display":"block"});
    shadow.addClass("with-shadow");
  }, function() {
    var content=$( this ).find('#post-content');
    var shadow=$( this ).find('.no-shadow');
    content.css({"display":"none"});
    shadow.removeClass("with-shadow");
  }
  );
});
