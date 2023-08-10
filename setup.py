from setuptools import setup

setup(
    name = 'montecarlo',
    version = '0.1.0',
    author = 'Quinn Glovier',
    author_email = 'qdg9xwb@virginia.edu',
    packages = ['montecarlo', 'unit_tests'],
    url = 'https://github.com/quinngl/quinngl_ds5100_montecarlo',
    license = 'LICENSE.txt',
    description = 'A monte carlo game simulation for DS 5100',
    long_description = open('README.md').read(),
    install_requires = [
        "Django >= 1.1.1",
        "pytest",
        "numpy",
        "pandas"
    ],
)
