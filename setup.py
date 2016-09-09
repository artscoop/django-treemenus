from setuptools import setup, find_packages

setup(
    name='django-treemenus',
    version='0.8.8-pre',
    description='Tree-structured menuing application for Django.',
    author='Julien Phalip',
    author_email='julien@julienphalip.com',
    url='http://github.com/jphalip/django-treemenus/',
    packages=find_packages(),
    package_data={
        'treemenus': [
            'static/img/treemenus/*.gif',
            'templates/admin/treemenus/menu/*.html',
            'templates/admin/treemenus/menuitem/*.html',
        ]
    },
    requires=['django'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
