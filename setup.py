# coding=utf-8
from setuptools import setup

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
      long_description = ""

setup(name='heatmiser_wifi',
      version='1.1.1',
      description='Library for communication with Heatmiser Wifi thermostats',
      long_description=long_description,
       long_description_content_type="text/markdown",
      url='http://github.com/midstar/heatmiser_wifi',
      project_urls={
            'Bug Tracker': 'https://github.com/midstar/heatmiser_wifi/issues',
            'Source Code': 'https://github.com/midstar/heatmiser_wifi',
      },
      author='Joel Midstjärna',
      author_email='joel.midstjarna@gmail.com',
      keywords = ['heatmiser', 'climate', 'temperature', 'thermostat'], 
      license='MIT',
      packages=['heatmiser_wifi'],
      entry_points = {
            'console_scripts': ['heatmiser_wifi=heatmiser_wifi.heatmiser_wifi:main'],
      },
      zip_safe=False,
      classifiers=[
      'Development Status :: 3 - Alpha',  
      'Intended Audience :: Developers', 
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3'
      ])
