// show message when update or edit success
window.onload=function(){
  var btn=document.getElementById('sub_form');
  var flag=document.getElementById('flag');
  var image=document.getElementById('id_Image');
  console.log(flag);
  btn.addEventListener('click',function showMessage(event){
        if (flag.textContent=='Create' &&image.files.length!=0 ) {
          alert("Save Succee.");
        }else if (flag.textContent=='Edit'&& image.files.length!=0) {
          alert("Edit Success");
        }else{
          alert("Please fill the high light part and try again.")
        }
      }
  ,false);
}
