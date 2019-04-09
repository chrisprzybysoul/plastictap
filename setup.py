from setuptools import setup

VERSION = '0.1.0'

REQUIRES = [
        'rq==0.13.0',
]

setup(
    name='plastictap',
    version=VERSION,
    description="lightweight distributed Gatling load test tool",
    url='https://github.com/soulcycle/plastictap',
    download_url='https://github.com/soulcycle/plastictap/archive/{}.zip'.format(VERSION),
    author='Chris Przybycien',
    author_email='chris.przybycien@soul-cycle.com',
    license='MIT',
    packages=['plastictap'],
    zip_safe=False,
    install_requires=REQUIRES,
    test_suite='tests',
        'console_scripts': [
            'plastictap = plastictap.cli:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
    ],
)

