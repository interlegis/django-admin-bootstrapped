from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Leandro Roberto Silva",
    author_email="leandroroberto.br@gmail.com",
    maintainer="Leandro Roberto",
    maintainer_email="leandroroberto.br@gmail.com",
    name='django-admin-bootstrapped',
    version='4.0.0',
    description='A Bootstrap theme for Django Admin',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/interlegis/django-admin-bootstrapped/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'setuptools',
        'django-bootstrap4',
        'Django>=1.11.11',
    ],
    test_suite='django_admin_bootstrapped.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
