#include "DataClassExample.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/embed.h>

DataClassExample::DataClassExample(int id, std::string name)
    : m_id(id), m_name(name)
{
}

DataClassExample::~DataClassExample()
{
}

int DataClassExample::getId()
{
    return this->m_id;
}

std::string DataClassExample::getName()
{
    return this->m_name;
}

void DataClassExample::setName(std::string name)
{
    this->m_name = name;
}

bool DataClassExample::isSameName(std::string name)
{
    return this->m_name.compare(name);
}

PYBIND11_EMBEDDED_MODULE(MyPyApp, m)
{
    m.doc() = "A Python API to access to cpp function";
    pybind11::class_<DataClassExample>(m, "DataClassExample")
        .def(pybind11::init<int, std::string>())
        .def("getId", &DataClassExample::getId)
        .def("getName", &DataClassExample::getName)
        .def("setName", &DataClassExample::setName)
        .def("isSameName", &DataClassExample::isSameName);
}