from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pycausal',
      version='0.1',
      description='Causal discovery and inference library',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Topic :: Statistics :: Causal Inference',
      ],
      url='http://github.com/triptoes/pycausal',
      author='Tanmayee Narendra',
      author_email='tanmayee.narendra@iiitb.org',
      license='BSD',
      packages=['pycausal'],
      install_requires= [
      'numpy',
      'networkx'],
      include_package_data = True,
      test_suite='nose.collector',
	  tests_require=['nose'],
      zip_safe=False)
