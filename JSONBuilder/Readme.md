# JSON Builder tool

This is a simple tool which allows you to generate your own JSON file. It generate it entry by entry and it is recursive (Array of object in a object is allowed).

## Description

The simple way to use it is to follow the indications. This tool uses a command prompt. This system is based on Question answers. There is a translation file ... up to you to add your own.

Example of basic Json : \
![alt text](https://github.com/Throows/Playground/blob/main/JSONBuilder/resources/example.jpg?raw=true)

Gives the result :\
![alt text](https://github.com/Throows/Playground/blob/main/JSONBuilder/resources/result.jpg?raw=true)

## Getting Started

### Dependencies

This Project is made with Python (3.11), Toml (0.10), VirtualEnv

### Installing

How to install this project ?\
* Clone the repository
```
git clone --recurse-submodules git@github.com:Throows/Playground
```
* Open a command prompt and create a venv (with python) inside JSONBuilder folder
```
python3 -m venv <path-to-project>
```
* Add Dependencies to the venv (after entrering in it)
```
pip install toml 
```

### Executing program

How to run the program:
* Open the Venv with the command
```
source env/bin/activate
```
* Run the python script 
```
python3 main.py
```
* Enjoy

## Help

Any advise for common problems or issues. Please create a issue or even a pull request.\
Feel Free to Contribute !

## Authors

Project made by Romain Berthoule (Throows)
Contributors names and contact info : \
(empty)

## Version History
* 0.0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Todo's

* Better file handling
* Faster navigation through the program
* ADD TUI ? maybe later (https://github.com/bczsalba/pytermgui)