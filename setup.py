from setuptools import setup

setup(
    name='AIBS',
    version='0.0.1',
    packages=['APP'],
    url='https://github.com/taux1c/AIBS',
    license='MIT',
    author='Taux1c',
    author_email='taux1c.software@protonmail.com',
    description='A simple, database centered scraper for anonib.',
    install_requires=[
        'aiofiles~=23.2.1',
        'SQLAlchemy~=2.0.23',
        'httpx~=0.25.1',
        'tqdm~=4.66.1',
        'beautifulsoup4~=4.12.2',
        'lxml~=4.6.1',
        ],
    long_description=open('README.md').read(),

)
