//add for current image shadow when hover
$(document).ready(function(){
  $( ".thumbnail" ).hover(
  function() {
    var content=$( this ).find('#article-content');
    var title=$( this ).find('#article-title');
    var date=$( this ).find('#article-date');
    var shadow=$( this ).find('.no-shadow');

    content.css({"display":"block"});
    title.css({"display":"none"});
    date.css({"display":"none"});
    shadow.addClass("with-shadow");
  }, function() {
    var content=$( this ).find('#article-content');
    var title=$( this ).find('#article-title');
    var date=$( this ).find('#article-date');
    var shadow=$( this ).find('.no-shadow');

    content.css({"display":"none"});
    title.css({"display":"block"});
    date.css({"display":"block"});
    shadow.removeClass("with-shadow");
  }
  );
});
