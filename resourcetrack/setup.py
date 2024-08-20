from setuptools import setup, find_packages

setup(
    name='workload_tracker',  # The name of your package
    version='0.1.0',  # Version number
    packages=find_packages(),  # Automatically find all packages in this directory
    description='A package for tracking and recording system metrics during data science workloads.',  # Short description of the package
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your contact email
    install_requires=[
        'psutil',  # List all dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
