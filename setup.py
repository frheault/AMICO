from setuptools import setup, find_packages

setup(
    name='amico',
    version='1.2.2',
    description='Accelerated Microstructure Imaging via Convex Optimization (AMICO)',
    author='Alessandro Daducci',
    author_email='alessandro.daducci@univr.it',
    url='https://github.com/daducci/AMICO',
    packages=find_packages(),
    package_data={'': ['*.bin', 'directions/*.bin']},
    install_requires=[
        'dipy', 'cython', 'spams',
    ],
)
