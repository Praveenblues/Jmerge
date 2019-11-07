# Jmerge

JSON-Merge is a Python utility for merging multiple .json files

## Installation

Download the script and run it on the computer.

## OS supported

Works on Most OS, Tested on Windows, Linux

## Usage

Provide the following parameters as input upon running the script:
* Path of the Folder containing the .json files
* The Base name of all the input files
* The desired base name of output files to be created
* The maximum output file size

The output JSON file will be saved in the same directory as the input JSON files, that is inside the specified input folder.

## Additional Features

* Files that do not have .json extension are ignored.
* Files that do not have the specified prefix are ignored.
* JSON files can be in any order inside the folder
* Missing JSON files are handled.
* The root key of all the files can be anything.


## License
[MIT](https://choosealicense.com/licenses/mit/)
