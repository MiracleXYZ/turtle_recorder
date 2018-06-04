from setuptools import setup, find_packages

setup(
    name = 'turtle_recorder',
    version = '0.2.0',
    keywords='turtle record gif mp4',
    description = 'A recorder of Python turtle animations written in Python 3.',
    license = 'MIT License',
    url = 'https://github.com/MiracleXYZ/turtle_recorder',
    author = 'Yuzhang Xie',
    author_email = 'xieyuzhang_xyz@foxmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)

