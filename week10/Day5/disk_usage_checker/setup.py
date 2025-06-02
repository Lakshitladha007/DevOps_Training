from setuptools import setup, find_packages

setup(
    name='disk_usage_checker',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'disk-usage=disk_usage_checker.disk_usage_cli:main'
        ]
    },
)
