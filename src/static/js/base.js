$(document).ready(function () {
// show side bar
$('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
});

// make navbar's position fixed when scroll
$(window).bind('scroll',function(){
    var navbar=$('.navbar-default');
    if ($(window).scrollTop()>0.8*$(window).height()) {
      // navbar.css({"position":"fixed"});
      navbar.addClass('navbar-scroll');
    } else {
      // navbar.css({"position":"initial"});
      navbar.removeClass('navbar-scroll');
    }

});
// change image of side bar and add css
$('#sidebarCollapse').bind('click',function(){
    var className=$('#sidebar').attr('class');
    var navSideBtnImg=$('.nav-side-btn-img');
    var bg=$('.bg');
    if (className=='active') {
      navSideBtnImg.attr('src','/static/image/chevron-left-d.png');
      bg.css({"margin-left":"20%"})
    } else {
      navSideBtnImg.attr('src','/static/image/chevron-right-d.png');
      bg.css({"margin-left":"0"})
    }
});

// alert messages show jump to github page
$('#play').bind('click',function(){
  alert('Go to github page');
});

// for each content-markdown insert markdown artical to DOM
$('.content-markdown').each(function(){
  var content=$(this).text();
  var markdownContent=marked(content);
  $(this).html(markdownContent);
});

});

//ajax for search
$(function() {
  $('#search').keyup(function() {

    $.ajax({
        type: "GET",
        url: "ajax",
        data: {
            'search_by' : $('#search').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType: 'html'
    });
});
});

// callback function. insert html to DOM
function searchSuccess(response)
{
  $('#search-result').html(response)
  //append will save old value
  // var parent = $("#p");
  // parent.append($(response));
}
