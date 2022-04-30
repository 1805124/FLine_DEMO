let subHotInf = document.getElementsByClassName("subHotInf");
console.log(subHotInf)



let countBoxMsg=`<div class="container d-flex flex-column justify-content-center align-items-center">
Time Remaining
</div>
<div class="container d-flex justify-content-center align-items-center">
<div class="container Days d-flex flex-column justify-content-center align-items-center">
    <div class="container">
        <span id="daysRemaining"></span>
    </div>
    <div class="container">
        Days
    </div>
</div>
<div class="container Days d-flex flex-column justify-content-center align-items-center">
    <div class="container">
        <span id="hoursRemaining"></span>
    </div>
    <div class="container">
        Hours
    </div>
</div>
<div class="container Days d-flex flex-column justify-content-center align-items-center">
    <div class="container">
        <span id="minutesRemaining"></span>
    </div>
    <div class="container">
        Minutes
    </div>
</div>
<div class="container Days d-flex flex-column justify-content-center align-items-center">
    <div class="container">
        <span id="secondsRemaining"></span>
    </div>
    <div class="container">
        Seconds
    </div>
</div>
</div>`;

function countDown(){
    // const dayCount = document.getElementById("dayCount").value;
    // console.log(dayCount)
    var countBox = document.getElementById("countDwn");
    countBox.classList.add("countBox")
    countBox.innerHTML=countBoxMsg;
    const todaysDate = new Date();
    console.log(todaysDate)
    const todaysDateTime = todaysDate.getTime();
    console.log(todaysDateTime);
    // const noOfDays = parseInt(dayCount);
    // const nextDate = new Date();
    // nextDate.setDate(nextDate.getDate()+noOfDays);
    // console.log(nextDate);
    // fixedDate = nextDate;

    let fixedDate = new Date('Sat May 01 2022 00:00:00');
    const fixedDateTime = fixedDate.getTime();
    console.log(fixedDateTime)
    console.log("fixed date :- ",fixedDate)
    const gap = fixedDateTime - todaysDateTime;
    console.log(gap)

    const seconds = 1000;
    const minutes = seconds*60;
    const hours = minutes*60;
    const days = hours*24;

    const daysRemaining = Math.floor(gap/days)
    const hoursRemaining = Math.floor((gap%days)/(hours))
    const minutesRemaining = Math.floor((gap%hours)/(minutes))
    const secondsRemaining = Math.floor((gap%minutes)/(seconds))

    // console.log(daysRemaining,hoursRemaining,minutesRemaining,secondsRemaining)

    document.getElementById("daysRemaining").innerHTML = daysRemaining;
    document.getElementById("hoursRemaining").innerHTML = hoursRemaining;
    document.getElementById("minutesRemaining").innerHTML = minutesRemaining;
    document.getElementById("secondsRemaining").innerHTML =secondsRemaining;
    console.log("Time")
}





for (var i = 0; i < subHotInf.length; i++) {
    subHotInf[i].addEventListener('mouseenter',function(){
        countDown();
    })
    subHotInf[i].addEventListener('mouseleave',function(){
        let removeCountDown = document.getElementById('countDwn');
        removeCountDown.innerHTML='Count Down Clock';
    })
}