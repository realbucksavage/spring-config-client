import os
from collections import OrderedDict

import setuptools

release_tag = os.getenv("RELEASE")
if not release_tag:
    print("RELEASE environment must be set")
    exit(2)

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="spring-config-client",
    version=release_tag,
    author="realbucksavage",
    description="A client for Spring Config Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://realbucksavage.github.io/spring-config-client",
    packages=setuptools.find_packages(),
    python_requires=">=3.6.0",
    project_urls=OrderedDict(
        (
            ("Documentation", "https://github.com/realbucksavage/spring-config-client"),
            ("Code", "https://github.com/realbucksavage/spring-config-client"),
            (
                "Issue tracker",
                "https://github.com/realbucksavage/spring-config-client/issues",
            ),
        )
    ),
    install_requires=["requests>=2.28.2"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Java Libraries",
    ],
)
