# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2016 and onwards Google, Inc.
#
# For general information on the Pynini grammar compilation library, see
# pynini.opengrm.org.


from setuptools import Extension
from setuptools import setup


COMPILE_ARGS = ["-std=c++11",
                "-Wno-unused-function",
                "-Wno-unused-local-typedef",
                "-funsigned-char",
                "-O3",
                "-march=native"]

pywrapfst = Extension(name="pywrapfst", language="c++",
                      extra_compile_args=COMPILE_ARGS,
                      libraries=["fstfarscript", "fstfar", "fstscript",
                                 "fst", "m", "dl"],
                      sources=["src/pywrapfst.cc"])

pynini = Extension(name="pynini", language="c++",
                   extra_compile_args=COMPILE_ARGS,
                   libraries=["re2",
                              "fstfarscript",
                              "fstpdtscript",
                              "fstmpdtscript",
                              "fstscript",
                              "fstfar",
                              "fst",
                              "m",
                              "dl"],
                   sources=["src/wildcardcomposescript.cc",
                            "src/special_arcs.cc",
                            "src/stringtokentype.cc",
                            "src/stringprintscript.cc",
                            "src/stringmapscript.cc",
                            "src/stringfile.cc",
                            "src/stringcompilescript.cc",
                            "src/stringcompile.cc",
                            "src/repeatscript.cc",
                            "src/pynini_replace.cc",
                            "src/pynini_cdrewrite.cc",
                            "src/pynini.cc",
                            "src/pathsscript.cc",
                            "src/optimizescript.cc",
                            "src/mergescript.cc",
                            "src/merge.cc",
                            "src/lenientlycomposescript.cc",
                            "src/gtl.cc",
                            "src/getters.cc",
                            "src/crossproductscript.cc"])

setup(
    name="pynini",
    version="1.9.1",
    description="Finite-state grammar compilation library",
    author="Kyle Gorman",
    author_email="kbg@google.com",
    url="http://pynini.opengrm.org/",
    keywords=[
        "natural language processing", "speech recognition", "machine learning"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment", "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    ext_modules=[pywrapfst, pynini],
    packages=[''],
    package_dir={'': '.'},
    package_data={'': ['lib/libre2.so.0', 'lib/libfstfarscript.so.0', 'lib/libfstpdtscript.so.0', 'lib/libfstmpdtscript.so.0', 'lib/libfstscript.so.0', 'lib/libfstfar.so.0', 'lib/libfst.so.0']},
    test_suite="pynini_test")
