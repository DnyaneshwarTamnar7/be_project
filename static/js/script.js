function passwordValidate() {
    let password = document.getElementById("password")
    let msg=document.getElementById("pass-msg")
    if(password.value.length>8) {
        
        msg.innerText=" "
    }else {
        msg.innerText="Password should be greate than 8"
    }
}
