// getDayOfWeekNumber7JS.js

function getDayOfWeekNumber7JS()
{
    let currentDate = new Date();

    let dayOfWeekNumber = currentDate.getDay();

    // make sunday be 6, monday 0
    dayOfWeekNumber = (dayOfWeekNumber + 6) % 7;

    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted;
}

// console.log(getDayOfWeekNumber7JS());

//--------------------//
// If today is Wednesday, it returns:
// 3
//--------------------//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
// getDayOfWeekNumber7JS.js
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian

//********************//

