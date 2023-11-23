from setuptools import setup

setup(
    name='AIBS',
    version='0.0.49',
    packages=['APP','APP.utils', 'APP.scrapers', 'APP.models'],
    url='https://github.com/taux1c/AIBS',
    license='MIT',
    author='Taux1c',
    author_email='taux1c.software@protonmail.com',
    description='A simple, database-centered scraper for anonib.',
    install_requires=[
        'aiofiles~=23.2.1',
        'SQLAlchemy~=2.0.23',
        'httpx~=0.25.1',
        'tqdm~=4.66.1',
        'beautifulsoup4~=4.12.2',
    ],
    long_description="""AnonIB Web Scraper This is a database-centric web scraper designed for extracting information from AnonIB forums. The scraper is freely available for use, and contributions from the community are welcomed and appreciated.

Usage Users are free to utilize this tool for their needs without any mandatory requirement for donations. However, if you find the tool helpful, you can make voluntary contributions through the link provided when the browser opens.

Contributing Feel free to contribute to this project by submitting pull requests. Your contributions can help enhance the functionality and efficiency of the web scraper for the benefit of the community.

Disclaimer This tool is intended for educational purposes only. It is not affiliated with AnonIB in any way, and any trademarks or intellectual property rights associated with AnonIB belong to their rightful owners. Any laws or terms of service violated by the use of this tool are solely the responsibility of the user, as this tool is meant strictly for educational purposes and not intended for actual use.

The tool is provided as-is without any warranty. I, as the creator, accept no liability for the usage of this tool.

Feel free to further modify this disclaimer to ensure it aligns with your intentions and the legal requirements of your project.""",
    entry_points={
        'console_scripts': [
            'anonib=APP.main'
        ]
    }
)
