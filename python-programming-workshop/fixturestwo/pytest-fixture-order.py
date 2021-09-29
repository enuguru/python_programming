import pytest
import logging

@pytest.fixture(scope="session")
def session():
    logging.info("scope session")
    
@pytest.fixture(scope="package")
def package():
    logging.info("scope package")

@pytest.fixture(scope="module")
def module():
    logging.info("scope module")

@pytest.fixture(scope="class")
def class_():
    logging.info("scope class")

@pytest.fixture(scope="function")
def function():
    logging.info("scope function")

def test_order(module, class_, session, function, package):
    assert True

# test/test_code1.py::test_order 
# ---------------- live log setup ----------------
# INFO     root:test_code1.py:8 scope session
# INFO     root:test_code1.py:13 scope package
# INFO     root:test_code1.py:18 scope module
# INFO     root:test_code1.py:23 scope class
# INFO     root:test_code1.py:28 scope function
# PASSED
