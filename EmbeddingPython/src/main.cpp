#include <iostream>
#include "PyEmbeddedApp.hpp"

int main(int argc, char *argv[])
{
    std::cout << "Starting application !" << std::endl;
    PyEmbeddedApp application;
    application.setup();
    return application.run();
}