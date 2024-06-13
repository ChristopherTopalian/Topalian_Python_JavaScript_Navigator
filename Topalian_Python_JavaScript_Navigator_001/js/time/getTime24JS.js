// getTime24JS.js

function getTime24JS()
{
    let currentDate = new Date();

    let hours = currentDate.getHours();
    let minutes = currentDate.getMinutes();
    let seconds = currentDate.getSeconds();

    // add a zero at the beginning
    if (hours < 10)
    {
        hours = "0" + hours;
    }

    if (minutes < 10)
    {
        minutes = "0" + minutes;
    }

    if (seconds < 10)
    {
        seconds = "0" + seconds;
    }

    let time = hours + ':' + minutes + ':' + seconds;

    return time;
}

// console.log(getTime24JS());

//--------------------//
// 04:57:08
//--------------------//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
// getTime24JS.js
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian

//********************//

