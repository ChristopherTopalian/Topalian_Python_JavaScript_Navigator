# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

# Topalian_Python_JavaScript_Navigator.pyw
# Version 001 - (2024-06-13)

# pip install pywebview

import webview
import base64

from py.date.getDate import getDate
from py.date.getDateTime12 import getDateTime12
from py.date.getDayOfMonth import getDayOfMonth
from py.date.getDayOfWeekName import getDayOfWeekName
from py.date.getDayOfWeekNumber import getDayOfWeekNumber
from py.date.getDayOfWeekNumber7 import getDayOfWeekNumber7
from py.date.getMonthNumber import getMonthNumber
from py.date.getYear import getYear

from py.time.getTime12 import getTime12
from py.time.getTime24 import getTime24

##

# Our JS is imported below

with open("js/date/getDateJS.js", "r") as file:
    getDateJS = file.read()

with open("js/date/getDateTimeJS.js", "r") as file:
    getDateTimeJS = file.read()

with open("js/date/getDayOfMonthJS.js", "r") as file:
    getDayOfMonthJS = file.read()

with open("js/date/getDayOfWeekNameJS.js", "r") as file:
    getDayOfWeekNameJS = file.read()

with open("js/date/getDayOfWeekNumber7JS.js", "r") as file:
    getDayOfWeekNumber7JS = file.read()

with open("js/date/getDayOfWeekNumberJS.js", "r") as file:
    getDayOfWeekNumberJS = file.read()

with open("js/date/getMonthNumberJS.js", "r") as file:
    getMonthNumberJS = file.read()

with open("js/date/getYearJS.js", "r") as file:
    getYearJS = file.read()

with open("js/time/getTime12JS.js", "r") as file:
    getTime12JS = file.read()

with open("js/time/getTime24JS.js", "r") as file:
    getTime24JS = file.read()

##

def getFileContent(filePath):
    try:
        with open(filePath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

##

# reads texture file and encodes it as base64
def readImageAsBase64(filePath):
    with open(filePath, "rb") as file:
        imageData = file.read()
        encodedImage = base64.b64encode(imageData).decode("utf-8")
    return encodedImage

bgTexturePath = "media/textures/bg001.jpg"
bgImage = readImageAsBase64(bgTexturePath)

##

htmlContent = f"""
<html>
<head>
<title> Topalian Python JavaScript Navigator </title>

<style>

body
{{
    background-color: rgb(0, 0, 0);
    font-family: Arial;
    color: rgb(255, 255, 255);
}}

#bg
{{
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1; 
}}

.textStyle001
{{
    width: 300px;
    margin: 2px;
    border: solid 1px rgb(100, 100, 100);
    border-radius: 8px;
    padding-left: 10px;
    padding-right: 10px;
    background-color: rgb(0, 0, 0);
    font-family: Arial;
    font-size: 16px;
    font-weight: bold;
    color: rgb(150, 150, 150);
    overflow: hidden;
    cursor: pointer;
}}

.textStyle001:hover
{{
    border-color: rgb(0, 255, 255);
}}

#code
{{
    width: 99%;
    height: 130vh;
    margin: 2px;
    border: solid 1px rgb(100, 100, 100);
    border-radius: 8px;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: rgb(0, 0, 0);
    font-family: Arial;
    font-size: 24px;
    font-weight: bold;
    color: rgb(220, 220, 220);
    overflow-y: scroll;
    cursor: pointer;
}}

* {{
    scrollbar-width: thin;
    scrollbar-color: rgb(100, 100, 100) rgb(0, 0, 0);
}}

</style>

<script>

function ge(whichId)
{{
    let result = document.getElementById(whichId);

    return result;
}}

function ce(whichType)
{{
    let result = document.createElement(whichType);

    return result;
}}

function ba(whichElement)
{{
    let result = document.body.append(whichElement);

    return result;
}}

//-//

// since we don't use two {{
// when we defined our functions
// we have to include these brackets
// as shown below:
{ getDateJS }
{ getDateTimeJS }
{ getDayOfMonthJS }
{ getDayOfWeekNameJS }
{ getDayOfWeekNumberJS }
{ getDayOfWeekNumber7JS }
{ getMonthNumberJS }
{ getYearJS }

{ getTime12JS }
{ getTime24JS }

//-//

function makeInterface()
{{
    let mainDiv = ce('div');
    mainDiv.id = 'mainDiv';
    ba(mainDiv);

    //-//

    let divContainer = ce('div');
    divContainer.id = 'divContainer';
    divContainer.style.display = 'grid';
    divContainer.style.gridTemplateColumns = 'repeat(2, 1fr)';
    divContainer.style.gap = '2.5px';
    mainDiv.append(divContainer);

    //-//

    // leftContainer
    let leftContainer = ce('div');
    leftContainer.id = 'leftContainer';
    leftContainer.style.overflowY = 'scroll';
    leftContainer.style.height = '200px';
    divContainer.append(leftContainer);

    //-//

    let pyLabel = ce('div');
    pyLabel.id = 'pyLabel';
    pyLabel.textContent = 'PY';
    pyLabel.style.fontWeight = 'bold';
    leftContainer.append(pyLabel);

    //-//

    let datePY = ce('input');
    datePY.id = 'datePY';
    datePY.className = 'textStyle001';
    datePY.value = 'Date: ' + '{getDate()}';
    datePY.title = 'getDate()';
    datePY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDate.py')}`;
    }};
    leftContainer.append(datePY);

    //-//

    let time12PY = ce('input');
    time12PY.id = 'time12PY';
    time12PY.className = 'textStyle001';
    time12PY.value = 'Time: ' + '{getTime12()}';
    time12PY.title = 'getTime12()';
    time12PY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/time/getTime12.py')}`;
    }};
    leftContainer.append(time12PY);

    //-//

    let time24PY = ce('input');
    time24PY.id = 'time24PY';
    time24PY.className = 'textStyle001';
    time24PY.value = 'Military Time: ' + '{getTime24()}';
    time24PY.title = 'getTime24()';
    time24PY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/time/getTime24.py')}`;
    }};
    leftContainer.append(time24PY);

    //-//

    let dateTime12PY = ce('input');
    dateTime12PY.id = 'dateTime12PY';
    dateTime12PY.className = 'textStyle001';
    dateTime12PY.value = 'Date Time: ' + '{getDateTime12()}';
    dateTime12PY.title = 'getDateTime12()';
    dateTime12PY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDateTime12.py')}`;
    }};
    leftContainer.append(dateTime12PY);

    //-//

    let yearPY = ce('input');
    yearPY.id = 'yearPY';
    yearPY.className = 'textStyle001';
    yearPY.value = 'Year: ' + '{getYear()}';
    yearPY.title = 'getYear()';
    yearPY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getYear.py')}`;
    }};
    leftContainer.append(yearPY);

    //-//

    let monthNumberPY = ce('input');
    monthNumberPY.id = 'monthNumberPY';
    monthNumberPY.className = 'textStyle001';
    monthNumberPY.value = 'Month Number: ' + '{getMonthNumber()}';
    monthNumberPY.title = 'getMonthNumber()';
    monthNumberPY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getMonthNumber.py')}`;
    }};
    leftContainer.append(monthNumberPY);

    //-//

    let dayOfMonthPY = ce('input');
    dayOfMonthPY.id = 'dayOfMonthPY';
    dayOfMonthPY.className = 'textStyle001';
    dayOfMonthPY.value = 'Day of Month: ' + '{getDayOfMonth()}';
    dayOfMonthPY.title = 'getDayOfMonth()';
    dayOfMonthPY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDayOfMonth.py')}`;
    }};
    leftContainer.append(dayOfMonthPY);

    //-//

    let dayOfWeekNamePY = ce('input');
    dayOfWeekNamePY.id = 'dayOfWeekNamePY';
    dayOfWeekNamePY.className = 'textStyle001';
    dayOfWeekNamePY.value = 'Day of Week Name: ' + '{getDayOfWeekName()}';
    dayOfWeekNamePY.title = 'getDayOfWeekName()';
    dayOfWeekNamePY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDayOfWeekName.py')}`;
    }};
    leftContainer.append(dayOfWeekNamePY);

    //-//

    let dayOfWeekNumberPY = ce('input');
    dayOfWeekNumberPY.id = 'dayOfWeekNumberPY';
    dayOfWeekNumberPY.className = 'textStyle001';
    dayOfWeekNumberPY.value = 'Day of Week Number: ' + '{getDayOfWeekNumber()}';
    dayOfWeekNumberPY.title = 'getDayOfWeekNumber()';
    dayOfWeekNumberPY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDayOfWeekNumber.py')}`;
    }};
    leftContainer.append(dayOfWeekNumberPY);

    //-//

    let dayOfWeekNumber7PY = ce('input');
    dayOfWeekNumber7PY.id = 'dayOfWeekNumber7PY';
    dayOfWeekNumber7PY.className = 'textStyle001';
    dayOfWeekNumber7PY.value = 'Day of Week Number 7th: ' + '{getDayOfWeekNumber7()}';
    dayOfWeekNumber7PY.title = 'getDayOfWeekNumber7()';
    dayOfWeekNumber7PY.onclick = function()
    {{
        ge('code').value = `{getFileContent('py/date/getDayOfWeekNumber7.py')}`;
    }};
    leftContainer.append(dayOfWeekNumber7PY);

    //----//

    // rightContainer
    let rightContainer = ce('div');
    rightContainer.id = 'rightContainer';
    rightContainer.style.overflowY = 'scroll';
    rightContainer.style.height = '200px';
    divContainer.append(rightContainer);

    //-//

    let jsLabel = ce('div');
    jsLabel.id = 'jsLabel';
    jsLabel.textContent = 'JS';
    jsLabel.style.fontWeight = 'bold';
    rightContainer.append(jsLabel);

    //-//

    let dateJS = ce('input');
    dateJS.id = 'dateJS';
    dateJS.className = 'textStyle001';
    dateJS.value = 'Date: ' + getDateJS();
    dateJS.title = 'getDateJS()';
    dateJS.onclick = function()
    {{
        ge('code').value = getDateJS;
    }};
    rightContainer.append(dateJS);

    //-//

    let time12JS = ce('input');
    time12JS.id = 'time12JS';
    time12JS.className = 'textStyle001';
    time12JS.value = 'Time: ' + getTime12JS();
    time12JS.title = 'getTime12JS()';
    time12JS.onclick = function()
    {{
        ge('code').value = getTime12JS;
    }};
    rightContainer.append(time12JS);

    //-//

    let time24JS = ce('input');
    time24JS.id = 'time24JS';
    time24JS.className = 'textStyle001';
    time24JS.value = 'Military Time: ' + getTime24JS();
    time24JS.title = 'getTime24JS()';
    time24JS.onclick = function()
    {{
        ge('code').value = getTime24JS;
    }};
    rightContainer.append(time24JS);

    //-//

    let dateTimeJS = ce('input');
    dateTimeJS.id = 'dateTimeJS';
    dateTimeJS.className = 'textStyle001';
    dateTimeJS.value = 'Date Time: ' + getDateTimeJS();
    dateTimeJS.title = 'getDateTimeJS()';
    dateTimeJS.onclick = function()
    {{
        ge('code').value = getDateTimeJS;
    }};
    rightContainer.append(dateTimeJS);

    //-//

    let yearJS = ce('input');
    yearJS.id = 'yearJS';
    yearJS.className = 'textStyle001';
    yearJS.value = 'Year: ' + getYearJS();
    yearJS.title = 'getYearJS()';
    yearJS.onclick = function()
    {{
        ge('code').value = getYearJS;
    }};
    rightContainer.append(yearJS);

    //-//

    let monthNumberJS = ce('input');
    monthNumberJS.id = 'monthNumberJS';
    monthNumberJS.className = 'textStyle001';
    monthNumberJS.value = 'Month Number: ' + getMonthNumberJS();
    monthNumberJS.title = ' getMonthNumberJS()';
    monthNumberJS.onclick = function()
    {{
        ge('code').value = getMonthNumberJS;
    }};
    rightContainer.append(monthNumberJS);

    //-//

    let dayOfMonthNumberJS = ce('input');
    dayOfMonthNumberJS.id = 'dayOfMonthNumberJS';
    dayOfMonthNumberJS.className = 'textStyle001';
    dayOfMonthNumberJS.value = 'Day of Month: ' + getDayOfMonthJS();
    dayOfMonthNumberJS.title = 'getDayOfMonthJS()';
    dayOfMonthNumberJS.onclick = function()
    {{
        ge('code').value = getDayOfMonthJS;
    }};
    rightContainer.append(dayOfMonthNumberJS);

    //-//

    let dayOfWeekNameJS = ce('input');
    dayOfWeekNameJS.id = 'dayOfWeekNameJS';
    dayOfWeekNameJS.className = 'textStyle001';
    dayOfWeekNameJS.value = 'Day of Week Name: ' + getDayOfWeekNameJS();
    dayOfWeekNameJS.title = 'getDayOfWeekNameJS()';
    dayOfWeekNameJS.onclick = function()
    {{
        ge('code').value = getDayOfWeekNameJS;
    }};
    rightContainer.append(dayOfWeekNameJS);

    //-//

    let dayOfWeekNumberJS = ce('input');
    dayOfWeekNumberJS.id = 'dayOfWeekNumberJS';
    dayOfWeekNumberJS.className = 'textStyle001';
    dayOfWeekNumberJS.value = 'Day of Week Number: ' + getDayOfWeekNumberJS();
    dayOfWeekNumberJS.title = 'getDayOfWeekNumberJS()';
    dayOfWeekNumberJS.onclick = function()
    {{
        ge('code').value = getDayOfWeekNumberJS;
    }};
    rightContainer.append(dayOfWeekNumberJS);

    //-//

    let dayOfWeekNumber7JS = ce('input');
    dayOfWeekNumber7JS.id = 'dayOfWeekNumber7JS';
    dayOfWeekNumber7JS.className = 'textStyle001';
    dayOfWeekNumber7JS.value = 'Day of Week Number 7th: ' + getDayOfWeekNumber7JS();
    dayOfWeekNumber7JS.title = 'getDayOfWeekNumber7JS()';
    dayOfWeekNumber7JS.onclick = function()
    {{
        ge('code').value = getDayOfWeekNumber7JS;
    }};
    rightContainer.append(dayOfWeekNumber7JS);

    //-//

    let hr001 = ce('hr');
    mainDiv.append(hr001);

    //-//

    // centerContainer
    let centerContainer = ce('div');
    centerContainer.id = 'centerContainer';
    centerContainer.style.overflowY = 'scroll';
    centerContainer.style.height = '270px';
    mainDiv.append(centerContainer);

    //-//

    let codeLabel = ce('div');
    codeLabel.id = 'codeLabel';
    codeLabel.textContent = 'CODE';
    codeLabel.style.fontWeight = 'bold';
    centerContainer.append(codeLabel);

    //-//

    let codeTextarea = ce('textarea');
    codeTextarea.id = 'code';
    centerContainer.append(codeTextarea);
}}

//-//

window.onload = function()
{{
    makeInterface();
}};

</script>

</head>

<body>

<img src = "data:image/jpeg;base64,{bgImage}" alt = "bgTexture" id = 'bg'>

</body>

</html>

"""

if __name__ == "__main__":
    # we can start the window at a small size
    # to avoid flashing white on the screen
    # and then maximize it manually
    widthOfWindow = 1200   #20
    heightOfWindow = 670   # 20

    # create window with HTML content
    webview.create_window("Topalian Python JavaScript Navigator", html=htmlContent, width=widthOfWindow, height=heightOfWindow)

    # start pywebview event loop
    # debug True enables console
    webview.start(debug=True)

