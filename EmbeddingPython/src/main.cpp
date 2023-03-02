#include <iostream>
#include "PyEmbeddedApp.hpp"

int main(int argc, char *argv[])
{
    std::cout << "Starting application !" << std::endl;
    pybind11::scoped_interpreter guard{};
    PyEmbeddedApp application{};
    application.setup();
    return application.run();
}