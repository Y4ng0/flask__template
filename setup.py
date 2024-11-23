from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='py_template_by_Yango',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,  # Specifies the requirements
    author='Yango',
    author_email='',
    description='My basic template for all python related projects',
    url='https://github.com/Y4ng0/custom_py_template',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)