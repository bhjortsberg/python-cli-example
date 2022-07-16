from setuptools import setup, find_packages

# python3 -m venv env
# env/bin/pip3 install .
with open('test.bhj', 'w') as f:
    f.write(' '.join(find_packages('src')))

setup(
    name='py-cli-example',
    version='0.1',
    description='Command line example tool',
    author='Björn Hjortsberg',
    author_email='bjorn.hjortsberg@gmail.com',
    # Will find cli_example and cli_example.commands packages
    packages=find_packages('src'),
    # The 'root' package is in src/
    package_dir={'': 'src', 'cli_example': 'src/cli_example'},
    entry_points={
        'console_scripts': [
            'py-cli-example=cli_example.main:main',
        ]
    }
)