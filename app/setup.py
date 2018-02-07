from setuptools import setup, find_packages

setup(
    name             = 'bigdue',
    version          = '1.0.0',
    description      = 'add project description',
    author           = 'add project author',
    author_email     = 'add project author_email',
    url              = 'https://github.com/Boeing737ng/Bigdue',
    download_url     = 'https://github.com/Boeing737ng/Bigdue.git',
    install_requires = ['pypcap', 'geoip2'],
    packages         = ['bigdue_app'],
    python_requires  = '>=3.6'
)