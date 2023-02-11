#pragma once
#include <string>

class DataClassExample
{
public:
    DataClassExample(int id, std::string name);
    ~DataClassExample();

    int getId();
    std::string getName();
    void setName(std::string name);
    bool isSameName(std::string name);

private:
    int m_id;
    std::string m_name;
};
