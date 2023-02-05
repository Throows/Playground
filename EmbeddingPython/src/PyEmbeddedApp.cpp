#include "PyEmbeddedApp.hpp"
#include <iostream>

PyEmbeddedApp::PyEmbeddedApp()
{
}

PyEmbeddedApp::~PyEmbeddedApp()
{
}

void PyEmbeddedApp::setup()
{
    std::cout << "Setting up application !" << std::endl;
    Py_Initialize();
    pybind11::scoped_interpreter scope;
    this->myModule = pybind11::module_::import("script");
}

int PyEmbeddedApp::run()
{
    std::cout << "Running application !" << std::endl;
    int returnval = this->myModule.attr("addition")(1, 3).cast<int>(); 
    return 0;
}
