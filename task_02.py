#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK12 synthesizing task 02."""


class CustomError(Exception):
    """Defining a CustomError class."""

    def __init__(self, msg, cause):
        """Defining the CustomError constructor."""
        Exception.__init__(self)
        self.msg = msg
        self.cause = cause
