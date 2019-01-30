from setuptools import find_packages, setup

setup(
    name='testwebapp',
    version='1.0.0',
    description='a description',
    author='author',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-login',
        'flask_sqlalchemy',
        'flask-wtf',
        'werkzeug',
    ],
)