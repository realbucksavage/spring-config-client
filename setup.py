from collections import OrderedDict

import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="spring-config-client",
    version="0.1",
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
    install_requires=["requests>=2.22.0"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Java Libraries",
    ],
)
