from conans import ConanFile, CMake

class Pkg(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    name = "HelloB"
    version = "0.1"
    requires = [("HelloC/0.1@user/testing", "override")]
    generators = "cmake"
    exports_sources = "src/*"

    def requirements(self):
        pass
        self.requires("HelloC/0.1@user/testing", override=True)
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["helloB"]
