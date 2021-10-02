from setuptools import setup

with open("README.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

REQUIREMENTS = ["numpy", "pandas"]

setup(
    name="GARPAR",
    version="0.1.1",
    description="Generación y análisis de retornos de portafolios artificiales y reales ",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Nadia Luczywo",
    author_email="nluczywo@gmail.com",
    url="https://github.com/nluczywo/GARPAR",

    py_modules=["garpar"],    #    <------- aca van los modulos
    #packages=[],    #    <------- aca van los paquetes completar luego
    include_package_data=False,    #    <------- solo si hay datos

    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["market simulation", "informacional eficiency",
              "portfolio optimization"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
    ],
)
