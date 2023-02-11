#pragma once
#include <pybind11/pybind11.h>
#include <pybind11/embed.h>

#include "DataClassExample.hpp"

class PyEmbeddedApp
{
public:
    PyEmbeddedApp();
    ~PyEmbeddedApp();

    void setup();
    int run();

private:
    pybind11::module_ myModule;
    DataClassExample myDataClass;
};
