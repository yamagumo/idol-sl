from setuptools import setup, find_packages

setup(
    name="ibukichi",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "ibukichi=ibukichi.run:main"
        ]
    },
)
