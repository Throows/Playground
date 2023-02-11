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

    after_build(function (target) 
        --os.run("python3 setup.py bdist_wheel")
        --for _, filedir in ipairs(os.filedirs("$(projectdir)/dist/**")) do
            --local filename = path.filename(filedir)
            --os.run("python3 -m pip install dist/%s --force-reinstall", filename)
        --end
        os.cp("$(projectdir)/src/scripts/**", "$(projectdir)/bin/$(os)_$(arch)_$(mode)/scripts/")
    end)