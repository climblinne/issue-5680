from conans import ConanFile, CMake

class Pkg(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    name = "HelloA"
    version = "0.1"
    requires = "HelloB/0.1@user/testing", ("HelloC/0.1@user/testing", "override")
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["helloA"]
