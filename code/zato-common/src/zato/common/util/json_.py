# -*- coding: utf-8 -*-

"""
Copyright (C) 2019, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from datetime import datetime
from json import dumps as json_dumps

# bson
from bson.objectid import ObjectId

# Python 2/3 compatibility
from builtins import bytes

# ################################################################################################################################

def default_json_handler(value):

    # Useful in various contexts
    if isinstance(value, datetime):
        return value.isoformat()

    # Always use Unicode
    elif isinstance(value, bytes):
        return value.decode('utf8')

    # For MongoDB queries
    elif isinstance(value, ObjectId):
        return 'ObjectId({})'.format(value)

    # We do not know how to serialize it
    raise TypeError('Cannot serialize `{}`'.format(value))

# ################################################################################################################################

def dumps(value, indent=4):
    return json_dumps(value, default=default_json_handler, indent=indent)

# ################################################################################################################################
