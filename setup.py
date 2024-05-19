from setuptools import setup, find_packages

setup(
    name='phalanx_customizer',
    version='0.1.0',
    author='Stelios Voutsinas',
    author_email='sv@sv.com',
    description='Phalanx Customizer Package',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'phalanx_customizer = phalanx_customizer.main:main',
        ],
    },
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
