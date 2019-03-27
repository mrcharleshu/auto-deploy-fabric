import setuptools

from fabfile import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-deploy-fabric",
    version=__version__,
    author="Charles",
    author_email="mrcharleshu@gmail.com",
    description="A small example package",
    long_description='Nothing Special, Just Deploy Our Application',
    long_description_content_type="text/markdown",
    url="https://github.com/mrcharleshu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['git-fabfile'],
    py_modules=['fabfile'],
    entry_points={
        'console_scripts': [
            'deploy_test_engine=fabfile:local_deploy_test_engine',
            'deploy_test_stats_api=fabfile:local_deploy_test_stats_api',
            'deploy_staging_engine=fabfile:local_deploy_staging_engine',
            'deploy_staging_stats_api=fabfile:local_deploy_staging_stats_api',
        ],
    },
)
