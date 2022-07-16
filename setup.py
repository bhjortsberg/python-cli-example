from setuptools import setup, find_packages


setup(
    name='py-cli-example',
    version='0.1',
    description='Command line example tool',
    author='Björn Hjortsberg',
    author_email='bjorn.hjortsberg@gmail.com',
    # Will find cli_example and cli_example.commands packages
    packages=find_packages('src'),
    # The 'root' package is in src/
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'py-cli-example=cli_example.main:main',
        ]
    }
)