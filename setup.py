from setuptools import setup

setup(
  name='wikiBot',
  version='0.7',
  description='A random wikipedia page generator.',
  long_description='A bot that uses the Wikipedia API to enumerate ' +
  'subcategories and subpages to generate a random page that is a member of ' +
  'a given supercategory.',
  author='Garrett Credi',
  author_email='gcc@ameritech.net',
  url='https://github.com/ddxtanx/wikiBot',
  license='MIT',
  download_url='https://github.com/ddxtanx/wikiBot/archive/0.2.tar.gz',
  py_modules=["wikiBot"],
  keywords=['wikipedia', 'random', 'generator', 'command_line', 'api'],
  classifiers=[],
  install_requires=['requests']
)
