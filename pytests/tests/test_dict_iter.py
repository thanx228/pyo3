import pytest
from pyo3_pytests.dict_iter import DictSize


@pytest.mark.parametrize("size", [64, 128, 256])
def test_size(size):
    d = {i: str(i) for i in range(size)}
    assert DictSize(len(d)).iter_dict(d) == size
