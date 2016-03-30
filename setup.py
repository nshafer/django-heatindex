import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

long_description = """
This replaces the `runserver` management command with a version that fires up a `brunch watch` process alongside the
Django development server to automatically recompile css and javascript. The brunch process is not interrupted when
the Django server reloads, but it will die when you shut down the Django server.

`Full Documentation on GitHub <https://github.com/nshafer/django-brunch>`_
"""

setup(
    name='django-heatindex',
    version='0.9.0',
    packages=['heatindex'],
    include_package_data=True,
    install_requires=['Django>=1.8.0,<1.10.0'],
    license='BSD License',
    description='A model field that tracks the "heat" of something.',
    long_description=long_description,
    url='https://github.com/nshafer/django-heatindex',
    author='Nathan Shafer',
    author_email='nate-github@lotech.org',
    keywords='django heatindex heat hotness sort',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
