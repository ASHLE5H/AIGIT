from setuptools import setup, find_packages

setup(
    name="aigit",
    version="1.0.0",
    author="Your Team Name",
    author_email="your_email@example.com",
    description="AI-powered Git command execution using natural language.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/aigit",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "aigit=src.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
