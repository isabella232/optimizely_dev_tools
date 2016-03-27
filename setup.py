from setuptools import setup

setup(name='optimizely_dev_tools',
      version='0.0.1',
      description='Optimizely developer tools',
      url='http://developers.optimizely.com/',
      author='Jon Gaulding, Tyler Jones, Peng-Wen Chen, Ali Rizvi, Lucas Swartsenburg',
      author_email='lucas@optimizely.com',
      license='MIT',
      packages=['optimizely_dev_tools'],
      scripts=['opti'],
      install_requires=[
        'flask', 'colorama', 'PyYAML', 'pykwalify', 'pylint', 'requests', 'NoseJS', 'optimizely-platform'
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
      ],
      package_data={
        'optimizely_dev_tools': [
          'assets/*.png',
          'assets/*.csv',
          'assets/*.html',
          'schema_files/*.yaml',
          'static/*.png',
          'static/*.svg',
          'static/*.css',
          'static/*.js',
          'template_files/*',
          'templates/*.html',
          'validate_functions.js'
        ],
      },
      zip_safe=False)
