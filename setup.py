from setuptools import setup

setup(
    name='Quantitative Biochemistry Undergraduate Course',
    version='0.2.0',
    author='Philip W Fowler',
    author_email="philip.fowler@ndm.ox.ac.uk",
    description="Twelve lecture course on mathematics for first-year undergraduates studying Biochemistry at the University of Oxford",
    url="https://github.com/oxfordmmm/quantitative_biochemistry",
    packages=['quantitative_biochemistry'],
    package_data={'': ['../config/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
    python_requires='>=3.5',
    install_requires=[
        "numpy >= 1.18",
        "matplotlib >= 3.2"
    ],
    license="TBD",
    scripts=['bin/qb-modify-latex.py'],\
    zip_safe=False
)
