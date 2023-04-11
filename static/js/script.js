btn=document.querySelector('#submit')
btn.disabled=true;
function validat(){
    div=document.querySelectorAll('.input-validate');
    email=div[0].value;
    password=div[1].value;
    len=email.length
    if((email.slice(-4)==='.com') && (password.length>=8)) {
    btn.disabled=false;
    }
}
validat()