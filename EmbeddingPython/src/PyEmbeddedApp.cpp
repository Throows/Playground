#include "PyEmbeddedApp.hpp"
#include <iostream>

PyEmbeddedApp::PyEmbeddedApp()
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
    pybind11::scoped_interpreter scope{};
    this->myModule = pybind11::module_::import("scripts.script");
    std::cout << "Running application !" << std::endl;
    
    try {
        returnval = this->myModule.attr("addition")(1, 3).cast<int>();
    }
    catch(const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    
    std::cout << "The result is : " << returnval << std::endl;
    return 0;
}

void printText()
{
    std::cout << "Printed a text" << std::endl;
}

PYBIND11_MODULE(MyPyApp, m)
{
    m.doc() = "A Python API to access to cpp function";
    m.def("printText", &printText, "Just print a text");
}