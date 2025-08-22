from setuptools import setup, find_packages

setup(
    name="ibukichi",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["Pillow"],
    include_package_data=True,
    package_data={
        "ibukichi": ["images/*"]
    },
    entry_points={
        "console_scripts": [
            "ibukichi=ibukichi.main:main"
        ]
    }
)
