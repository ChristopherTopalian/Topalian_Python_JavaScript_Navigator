// getDateJS.js

function getDateJS()
{
    let currentDate = new Date();

    let year = currentDate.getFullYear();

    let month = (currentDate.getMonth() + 1).toString();

    // add a zero
    if (month.length < 2)
    {
        month = '0' + month;
    }

    let day = currentDate.getDate().toString();

    // add a zero
    if (day.length < 2)
    {
        day = '0' + day;
    }

    let date = year + '-' + month + '-' + day;

    return date;
}

// console.log(getDateJS());

//--------------------//
// 2024/06/07
//--------------------//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
// getDateJS.js
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian

//********************//

