from setuptools import setup, find_packages
from version import get_git_version

with open('README') as f:
    long_description = ''.join(f.readlines())


setup(
    name='dzisholiday',
    version=get_git_version(),
    description='Finds Czech holiday for given year',
    long_description=long_description,
    author='Jan Novak',
    author_email='novak@novak.com',
    keywords='holiday,dates',
    license='Public Domain',
    url='https://github.com/zichd/dzisholiday',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        ],
    zip_safe=False,
)
