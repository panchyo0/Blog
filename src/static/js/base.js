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

//ajax for search 
$(function() {
  $('#search').keyup(function() {

    $.ajax({
        type: "GET",
        url: "index/ajax/",
        data: {
            'search_by' : $('#search').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType: 'html'
    });
});
});
function searchSuccess(response)
{
  $('#t').html(response)
  //append will save old value
  // var parent = $("#p");
  // parent.append($(i));
}
