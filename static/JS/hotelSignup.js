// const ngoFormButtonClick = document.getElementById("hotelFormButton")

// ngoFormButtonClick.addEventListener('click',function (event) {
//     event.preventDefault(); // stops the submitting and prints the alert
//     const alertShow = document.getElementById("alertBox")
//     alertShow.classList.remove("hide")
    
// })




//do a proper from validation and then submit it properly and then make a proper alert , the above one is temporary


const validIcon = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
</svg>
`;

const invalidIcon = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
</svg>`;

const nameErrorMsg = `Name should contain min. 5 characters and max. 30 characters.
`;

const validMsg = `Looks Good!
`;

const contactNumberErrorMsg=`Contact Number should contain 10 digits.
`;


const emailErrorMsg=`Please Enter a valid Email Address.
`;

const passwordErrorMsg = `Please Enter a valid Password.
`;

const uploadErrorMsg = `Please Upload a .png File.
`;


function clearErrors(){
    let errors = document.getElementsByClassName("formError");
    for (let item of errors){
        item.innerHTML = "";
    }
}



function setError(id,error){
    //sets error inside tag of id
    let element = document.getElementById(id)
    element.innerHTML = error;
}

function setValid(id,valid){
    let element = document.getElementById(id)
    element.innerHTML=valid;
}

//do a proper from validation and then submit it properly and then make a proper alert , the above one is temporary



const hotelFormButtonClick = document.getElementById("hotelFormButton")

hotelFormButtonClick.addEventListener('click',function validateForm (event) {
    event.preventDefault();
    clearErrors();
    //perform validation and if validation fails , set the value of defaultReturnValue to false.
})

// name validation
const username = document.forms["myForm"]["requester_name"];
username.addEventListener('input',function (e) {
    console.log(e.target.name)
    let target = e.target.name;
    if (target == "req_name"){
        var name = document.forms["myForm"]["requester_name"].value;
    if((name.length<=4)||(name.length>30)){
        setError("nameMsg",nameErrorMsg);
        setError("nameIcon",invalidIcon)
        document.getElementById("nameIcon").classList.add("invalidIcon")
        document.getElementById("nameIcon").classList.remove("validIcon")
        document.getElementById("nameMsg").classList.add("errorMsg")
        document.getElementById("nameMsg").classList.remove("validMsg")
    }
    else{
        setValid("nameMsg",validMsg)
        setValid("nameIcon",validIcon)
        document.getElementById("nameIcon").classList.add("validIcon")
        document.getElementById("nameIcon").classList.remove("invalidIcon")
        document.getElementById("nameMsg").classList.add("validMsg")
        document.getElementById("nameMsg").classList.remove("errorMsg")
    }
    }
})