from setuptools import setup

setup(
    name='my_py_cli',
    version='0.1.0',
    py_modules=['my_py_cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'my_py_cli = my_py_cli:cli',
        ],
    },
)