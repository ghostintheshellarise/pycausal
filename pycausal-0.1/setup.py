from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pycausal',
      version='0.1',
      description='Causal discovery and inference library',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Sociology',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      url='http://github.com/triptoes1/pycausal/',
      author='Tanmayee Narendra',	
      license='BSD',
      packages=['pycausal'],
      install_requires= [
      'numpy',
      'networkx'],
      include_package_data = True,
      test_suite='nose.collector',
	  tests_require=['nose'],
      zip_safe=False)
