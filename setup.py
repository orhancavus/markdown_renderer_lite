from setuptools import setup, find_packages

setup(
    name="markdown_renderer",
    version="0.1",
    packages=find_packages(),
    install_requires=["markdown"],
    entry_points={
        "console_scripts": [
            "markdown_renderer=markdown_renderer.converter:convert_markdown"
        ],
    },
    include_package_data=True,
    package_data={"markdown_renderer": ["static/*.css"]},
    author="Orhan Cavus",
    author_email="orhancv@example.com",
    description="A simple Markdown to HTML converter with syntax highlighting.",
    url="https://github.com/orhancavus/markdown_renderer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
