"""Logger fixtures."""

import logging

import pytest

from taralog import setup_logger
from taralog.testing.logger import LoggerHandler


@pytest.fixture(autouse=True)
def logger_handler():
    """Logger handler fixture."""
    handler = LoggerHandler()
    setup_logger(logging.DEBUG, handler)
    try:
        yield handler
    finally:
        setup_logger()
