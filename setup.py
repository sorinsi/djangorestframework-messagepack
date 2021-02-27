from setuptools import setup, find_packages

setup(
    name="djangorestframework-messagepack",
    version="1.0.1",
    url="https://github.com/sorinsi/djangorestframework-messagepack",
    license="MIT",
    description="Parser and renderer for MessagePack in Django Rest Framework",
    author="Sorin Cotoc",
    author_email="sopromo@protonmail.com",
    packages=find_packages(),
    install_requires=("msgpack>=1.0.0", "djangorestframework>=2.1.15", "Django>=1.8"),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
