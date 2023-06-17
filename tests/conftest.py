import pathlib
import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def data():
    return pathlib.Path(__file__).parent / "data"
