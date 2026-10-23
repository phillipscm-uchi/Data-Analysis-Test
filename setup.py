import setuptools

setuptools.setup(
    name="textkit", 
    version="0.0.1",
    author="Connor Phillips",  
    author_email="phillipscm@uchicago.edu",
    description="A simple pytest setup",
    packages=setuptools.find_packages(),
    install_requires=[
        'textkit',
        'sys', 
        '.text_utils',
        're',
        'unicodedata'
        'helpers',
    ],
)