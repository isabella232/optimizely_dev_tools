from setuptools import setup

setup(name='optimizely_dev_tools',
      version='0.0.1',
      description='Optimizely developer tools',
      url='http://developers.optimizely.com/',
      author='Lucas Swartsenburg',
      author_email='lucas@optimizely.com',
      license='MIT',
      packages=['optimizely_dev_tools'],
      scripts=['opti'],
      install_requires=[
        'flask', 'colorama', 'PyYAML'
      ],
      package_data={'optimizely_dev_tools': ['assets/*.png', 'assets/*.csv', 'assets/*.rst/', 'assets/*.txt']},
      zip_safe=False)