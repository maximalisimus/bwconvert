from setuptools import setup, find_packages
from os.path import join, dirname

# python setup.py sdist bdist_wheel
# python setup.py install
# pip install .

setup(
    name='blacklist-scripts',
    version='1.0.0',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Mikhail Artamonov',
    author_email='maximalis171091@yandex.ru',
    url='https://github.com/maximalisimus/bwconvert.git',
    packages=find_packages(include=['bwconvert', '*.py']),
    include_package_data=True,
    entry_points={
        'console_scripts': ['bwconvert=bwconvert.bwconvert:main']
    },
    keywords = ["Bitwarden", "KeepassXC", "Converter"],
	classifiers = [
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Development Status :: 3 public release",
		"License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 3 (GPL3)",
		"Operating System :: Linux",
		"Topic :: Utilities",
		],
	python_requires='>=3.0',
)
