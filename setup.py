from setuptools import setup

import vs_locus

def readme():
    with open('README') as f:
        return f.read()


setup(name='vs_locus',
      version=vs_locus.__version__,
      description=vs_locus.__description__,
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Intended Audience :: Science/Research',
      ],
      keywords='population genomics RAD vsearch',
      url=vs_locus.__url__,
      author=vs_locus.__author__,
      author_email=vs_locus.__author_email__,
      license=vs_locus.__license__,
      packages=['vs_locus'],
      install_requires=[
          'click',
          'pandas',
      ],
      test_suite='nose.collector',
      tests_require=[],
      entry_points={
          'console_scripts': ['vs_locus=vs_locus.vs_locus:vs_locus'],
      },
      include_package_data=True,
      zip_safe=False)
