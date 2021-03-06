import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-multi-email-field',
    version='0.1',
    author='Florent Lebreton',
    author_email='florent.lebreton@makina-corpus.com',
    url='https://github.com/makinacorpus/django-multi-email-field',
    download_url="https://github.com/makinacorpus/django-multi-email-field/archive/master.zip",
    description="Provides a model field and a form field to manage list of e-mails",
    #long_description=open(os.path.join(here, 'README.rst')).read(),
    license='LPGL, see LICENSE file.',
    install_requires=['Django'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Intended Audience :: Developers',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Development Status :: 4 - Beta',
                'Programming Language :: Python :: 2.7'],
)
