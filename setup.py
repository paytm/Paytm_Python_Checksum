import setuptools

long_description = "https://developer.paytm.com/docs/checksum/#python"
    
setuptools.setup(
    name="paytmchecksum",
    version="1.7.0",
    description="This is for paytm checksum creation and verification in python",
    url="https://github.com/paytm/Paytm_Python_Checksum",
    author="Soumya Vats",
    license="MIT",
    packages=setuptools.find_packages(),
    keywords='Paytm Checksum Python Signature Payment',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",

        # List of supported Python versions
        # Make sure that this is reflected in .travis.yml as well
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
 )