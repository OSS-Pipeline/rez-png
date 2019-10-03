name = "png"

version = "1.6.37"

authors = [
    "JCosmin Truta",
    "Glenn Randers-Pehrson",
    "Andreas Eric Dilger",
    "Guy Eric Schalnat"
]

description = \
    """
    libpng is the official Portable Network Graphics reference library. It is a platform-independent library that
    contains C functions for handling PNG images.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "pngfix",
    "png-fix-itxt"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "png-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    # Helper environment variables.
    env.PNG_BINARY_PATH.set("{root}/bin")
    env.PNG_INCLUDE_PATH.set("{root}/include")
    env.PNG_LIBRARY_PATH.set("{root}/lib64")
