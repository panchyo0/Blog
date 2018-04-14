$(document).ready(function () {
// show side bar
$('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
});

// change image of side bar
$('#sidebarCollapse').bind('click',function(){
    var className=$('#sidebar').attr('class');
    var navSideBtnImg=$('.nav-side-btn-img');
    if (className=='active') {
      navSideBtnImg.attr('src','/static/image/chevron-left-d.png');
    } else {
      navSideBtnImg.attr('src','/static/image/chevron-right-d.png');
    }
});

});
