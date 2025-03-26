from setuptools import setup, find_packages

setup(
    name="wallhaven_crawler",
    version="0.1.0",
    author="kyriechen",
    author_email="your.email@example.com",
    description="A powerful crawler for Wallhaven website",
    # 修改这一行，指定编码为UTF-8
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KyrieMU/wallhaven-crawler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
)