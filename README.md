Reproduce recipe:
=================

1. Create C: `conan create . user/testing`
2. Create B: `conan create . user/testing`
3. Create A: `conan create . user/testing`

Output:
```
HelloA/0.1@user/testing: Building your package in C:\Users\jlinnenkoh\.conan\data\HelloA\0.1\user\testing\build\a8c031b0151521648fa249b62f2a654a9211671b
HelloA/0.1@user/testing: ERROR: Generator cmake(file:conanbuildinfo.cmake) failed
'HelloC'
ERROR: 'HelloC'
```

conan --version   == 1.19.2
