import pytest

# ==== CONFIGURATION AND FIXTURES ====

# Fixture with setup and teardown
@pytest.fixture(scope="module")
def sample_data():
    print("\n[SETUP] Preparing sample data...")
    data = {"key1": "value1", "key2": 42, "key3": [1, 2, 3]}
    yield data
    print("\n[TEARDOWN] Cleaning up sample data...")

# Fixture with a parameterized value
@pytest.fixture(params=[1, 2, 3])
def param_fixture(request):
    return request.param

# ==== TEST FUNCTIONS ====

# Basic test function
def test_basic_assertion():
    assert 1 + 1 == 2, "Basic arithmetic test failed."

# Using a fixture
def test_using_fixture(sample_data):
    assert "key1" in sample_data, "Expected key 'key1' in sample data."

# Parameterized test
@pytest.mark.parametrize("input_value, expected", [(2, 4), (3, 9), (4, 16)])
def test_parametrize(input_value, expected):
    assert input_value**2 == expected, f"Square of {input_value} should be {expected}"

# Using a parameterized fixture
def test_with_param_fixture(param_fixture):
    assert param_fixture in [1, 2, 3], f"Fixture returned unexpected value {param_fixture}"

# Skipping a test conditionally
@pytest.mark.skipif(condition=True, reason="Demonstration of skipping")
def test_skipped():
    assert False, "This test is skipped."

# Custom marker
@pytest.mark.slow
def test_custom_marker():
    import time
    time.sleep(1)
    assert True, "Custom marker test passed."

# Expected exception
def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# ==== GROUPING AND DEPENDENCIES ====

# Grouping related tests with a class
class TestStringMethods:
    def test_upper(self):
        assert "hello".upper() == "HELLO"

    def test_isupper(self):
        assert not "Hello".isupper()

# Dependency injection: Use one test's result in another
@pytest.fixture
def computation_result():
    return 2 * 3

def test_computation(computation_result):
    assert computation_result == 6

def test_dependency_on_computation(computation_result):
    assert computation_result % 2 == 0, "Result should be even."

# ==== DYNAMICALLY GENERATED TEST CASES ====

# Generate test cases dynamically using a factory
@pytest.mark.parametrize("value", range(5))
def test_dynamic_tests(value):
    assert value >= 0, f"Value {value} should be non-negative."

# ==== MAIN DRIVER CODE (OPTIONAL) ====
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
