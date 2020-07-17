# Project
[![Build Status](https://travis-ci.org/sorinsi/djangorestframework-messagepack.svg?branch=master)](https://travis-ci.org/sorinsi/djangorestframework-messagepack)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/sorinsi/djangorestframework-messagepack/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/djangorestframework-messagepack/)


# Overview
MessagePack renderer and parser for Django Rest Framework to easily implement it in your application.

This package uses the new `msgpack` instead of the old one `msgpack-python` and uses the same
technique for encoding data as the `JSONRenderer` in order to reduce friction and
to be able to easily use the same code.

# Install
`pip install djangorestframework-messagepack`

# Getting started
You need to setup the renderer and parser according to the Django Rest Framework documentation.

You can read [about custom renderers on this link](https://www.django-rest-framework.org/api-guide/renderers/#custom-renderers) 
or [about custom parsers here](https://www.django-rest-framework.org/api-guide/parsers/#custom-parsers)

Your end result might be something similar to this:

```
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework_messagepack.renderers.MessagePackRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework_messagepack.parsers.MessagePackParser",
    ]
}
```

# Changelog

### 1.0.0

Initial release
