# Dedicated to God the Father

# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024

# https://github.com/ChristopherTopalian

# https://github.com/ChristopherAndrewTopalian

# Topalian_Combine_JS_Files.py

import os

def combineJSFiles(directory, scriptFileName):
    outputFilePath = os.path.join(directory, 'main.js')
    fileContents = []

    def traverseFolder(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath != scriptFileName and filePath.endswith('.js'):
                    with open(filePath, 'r', encoding='utf-8') as f:
                        fileContents.append(f.read())

    traverseFolder(directory)

    with open(outputFilePath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fileContents))
    print(f"Combined {len(fileContents)} .js files into {outputFilePath}")

# get current directory of script
currentDirectory = os.path.dirname(os.path.abspath(__file__))

# get filename of script
scriptFileName = os.path.abspath(__file__)

combineJSFiles(currentDirectory, scriptFileName)
