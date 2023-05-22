from setuptools import setup, find_packages

setup(
    name='phalanx-customizer',
    version='0.1.0',
    author='Stelios Voutsinas',
    author_email='stv@roe.ac.uk',
    description='Phalanx Customizer Package',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
