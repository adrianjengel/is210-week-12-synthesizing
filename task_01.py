#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK12 synthesizing task 01."""


class BaseError(Exception):
    """Defining a BaseError class."""
    pass


class StringError(BaseError, TypeError):
    """Defining a StringError class."""
    pass


class NumberError(BaseError, TypeError):
    """Defining a NumerError class."""
    pass


class NonZeroError(NumberError):
    """Defining a NonZeroError class."""
    pass
