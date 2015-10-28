from setuptools import setup, find_packages

setup(
    name="EncryptHashPassword",
    version="1.0.1",
    description="Use your domain, password and extra salt to encrypt password",
    long_description=open('README.rst').read(),
    author="BoscoTsang",
    author_email="boscotsang3@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['genpassword=genpassword.genpassword:main']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
