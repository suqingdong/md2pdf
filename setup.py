import json
from pathlib import Path
from setuptools import setup, find_packages


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('md2pdf', 'version.json').open())

setup(
    name=version_info['name'],
    version=version_info['version'],
    author=version_info['author'],
    author_email=version_info['author_email'],
    description=version_info['desc'],
    long_description=BASE_DIR.joinpath('README.md').read_text(),
    long_description_content_type='text/markdown',
    url=version_info['url'],
    license='MIT License',
    install_requires=BASE_DIR.joinpath('requirements.txt').read_text().strip().split(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'md2pdf = md2pdf.bin.main:main',
    ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries'
    ]
)
