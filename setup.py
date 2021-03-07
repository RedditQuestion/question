from setuptools import setup,find_packages

setup(
name="package",
version="0.0.1",
packages=find_packages(),

entry_points={
"console_scripts":["package=package.module2:main"]
},

package_data={"package":"cpp_files/*"}
)
