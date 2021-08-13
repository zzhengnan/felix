from setuptools import find_packages, setup

import felix


EXTRA_REQUIRES = {
    'build': ['setuptools', 'twine', 'wheel'],
    'qa': ['flake8'],
    'test': ['mypy', 'pytest'],
}

EXTRA_REQUIRES['dev'] = (
    EXTRA_REQUIRES['build'] +
    EXTRA_REQUIRES['qa'] +
    EXTRA_REQUIRES['test']
)


setup(
    name='felix-decorator',
    version=felix.__version__,
    url='https://github.com/zzhengnan/felix',
    author='Zhengnan Zhao',
    description="A collection of handy decorators for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.7',
    extra_requires=EXTRA_REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
