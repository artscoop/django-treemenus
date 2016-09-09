from setuptools import setup, find_packages

setup(
    name='django-treemenus-plus',
    version='0.8.8-pre',
    description='Tree-structured menuing application for Django.',
    author='Steve Kossouho/Julien Phalip',
    author_email='julien@julienphalip.com',
    url='http://github.com/artscoop/django-treemenus-plus/',
    packages=find_packages(),
    package_data={
        'treemenusplus': [
            'static/img/treemenusplus/*.gif',
            'templates/admin/treemenusplus/menu/*.html',
            'templates/admin/treemenusplus/menuitem/*.html',
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
