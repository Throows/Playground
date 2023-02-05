add_rules("mode.debug", "mode.release")

add_requires("spdlog", "pybind11", "python")

set_runtimes("MD")
set_languages("cxx20")
set_rundir("./bin/$(os)_$(arch)_$(mode)")
set_targetdir("./bin/$(os)_$(arch)_$(mode)")

set_project("EmbeddingPython")

target("EmbeddingPython")
    set_version("0.0.1")

    set_kind("binary")

    add_files("src/*.cpp")
    add_headerfiles("src/*.h")
    --add_includedirs("include/")

    add_packages("spdlog", "pybind11", "python")
    set_symbols("debug")
    if is_mode("debug") then
        add_defines("DEBUG")
    end