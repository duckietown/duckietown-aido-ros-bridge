from setuptools import find_packages, setup

# :==> Fill in your project data here
# The package name is the name on PyPI
# it is not the python module names.
line = "daffy"
package_name = f"duckietown-aido-ros-bridge-{line}"
library_webpage = "http://github.com/duckietown/duckietown-aido-ros-bridge"
maintainer = "Mack"
maintainer_email = "admin@duckietown.org"
short_description = "A short description"
full_description = """
A longer description.
"""


# Read version from the __init__ file
def get_version_from_source(filename):
    import ast

    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith("__version__"):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError("No version found in %r." % filename)
    if version is None:
        raise ValueError(filename)
    return version


version = get_version_from_source("src/duckietown_aido_ros_bridge/__init__.py")

# read project dependencies
# NO - dependencies.txt is for testing dependiences - EVERYTHING PINNED
# The requirements here must be broad.
# dependencies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dependencies.txt')
# with open(dependencies_file, 'rt') as fin:
#     dependencies = list(filter(lambda line: not line.startswith('#'), fin.read().splitlines()))
line = "daffy"

install_requires = [
    f"aido-protocols-{line}",
    "numpy",
    "Pillow",
    "opencv-python",
]
tests_require = []

# compile description
underline = "=" * (len(package_name) + len(short_description) + 2)
description = """
{name}: {short}
{underline}

{long}
""".format(
    name=package_name,
    short=short_description,
    long=full_description,
    underline=underline,
)

console_scripts = [
    "aido-ros-bridge-launch=duckietown_aido_ros_bridge:run_ros_bridge_main",
]
# setup package
setup(
    name=package_name,
    author=maintainer,
    author_email=maintainer_email,
    url=library_webpage,
    tests_require=tests_require,
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages("./src"),
    long_description=description,
    version=version,
    entry_points={"console_scripts": console_scripts},
)
