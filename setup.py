from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="warnme",
    version="0.1",
    packages=find_packages(),
    py_modules=["cli"],
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "warnme=cli:send_message"
        ]
    },
)
