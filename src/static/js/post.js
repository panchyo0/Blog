// show message when update or edit success
window.onload=function(){
  var btn=document.getElementById('sub_form');
  var flag=document.getElementById('flag');
  console.log(flag);
  btn.addEventListener('click',function showMessage(event){
        if (flag.textContent=='Create') {
          alert("Save Succee.");
        }else if (flag.textContent=='Edit') {
          alert("Edit Success");
        }else{
          alert("Somthing Wrong. Please try again.")
        }
      }
  ,false);
}
