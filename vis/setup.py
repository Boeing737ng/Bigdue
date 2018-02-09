from setuptools import setup, find_packages

setup(name='packetvisulizaion',
      version='1.2.0',
      description='Packet Visualization',
      url='https://github.com/Boeing737ng/Bigdue',
      license='GNU',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: OSI Approved :: GNU License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      packages=find_packages(exclude=['docs', 'tests']),
      )