#include "PyEmbeddedApp.hpp"
#include <iostream>

PyEmbeddedApp::PyEmbeddedApp() : myDataClass(1, "MyDataClass")
{
}

PyEmbeddedApp::~PyEmbeddedApp()
{
    Py_Exit(0);
}

void PyEmbeddedApp::setup()
{
    std::cout << "Setting up application !" << std::endl;
}

int PyEmbeddedApp::run()
{
    int returnval = -1;
   
    this->myModule = pybind11::module_::import("scripts.script");
    std::cout << "Running application !" << std::endl;
    
    try {
        returnval = this->myModule.attr("runScript")(this->myDataClass).cast<int>();
    }
    catch(const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    
    std::cout << "The Data Name is : " << this->myDataClass.getName() << std::endl;
    std::cout << "The result is : " << returnval << std::endl;
    return 0;
}