from setuptools import setup, find_packages

setup(
    name='resourcetrack',  # The name of your package
    version='0.1.1',  # Version number
    packages=find_packages(),  # Automatically find all packages in this directory
    description='A package for tracking and recording system metrics during data science workloads.',  # Short description of the package
    author='Prenil Sewmohan',  # Your name
    author_email='prenil.s@gmail.com',  # Your contact email
    install_requires=[
        'psutil',  # Dependency for system metrics
        'matplotlib',  # Dependency for plotting graphs
        'numpy',  # Dependency for numerical operations
        'gputil',  # Dependency for GPU metrics
        'pandas',  # Dependency for data manipulation
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
