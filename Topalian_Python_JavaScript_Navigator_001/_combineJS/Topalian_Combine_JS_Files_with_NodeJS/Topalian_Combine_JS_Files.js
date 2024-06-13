// Dedicated to God the Father

// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024

// https://github.com/ChristopherTopalian

// https://github.com/ChristopherAndrewTopalian

// Topalian_Combine_JS_Files.js

let fs = require('fs');
let path = require('path');

function combineJSFiles(directory, scriptFilename)
{
    let outputFilePath = path.join(directory, 'main.js');

    let fileContents = [];

    function traverseFolder(folder)
    {
        let files = fs.readdirSync(folder);

        for (let i = 0; i < files.length; i++)
        {
            let file = files[i];

            let filePath = path.join(folder, file);

            let stats = fs.statSync(filePath);

            if (stats.isDirectory())
            {
                traverseFolder(filePath);
            }
            else if (path.extname(filePath) === '.js')
            {
                let content = fs.readFileSync(filePath, 'utf8');
                // check if file is not the script file itself
                if (filePath !== scriptFilename)
                {
                    fileContents.push(content);
                }
            }
        }
    }

    traverseFolder(directory);

    fs.writeFileSync(outputFilePath, fileContents.join('\n'), 'utf8');

    console.log(`Combined ${fileContents.length} .js files into ${outputFilePath}`);
}

// get current directory of script
let currentDirectory = process.cwd();

// get filename of script
let scriptFilename = __filename;

combineJSFiles(currentDirectory, scriptFilename);
