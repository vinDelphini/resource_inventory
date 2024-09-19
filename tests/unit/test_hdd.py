"""
Tests for HDD class
Command line: python3 -m pytest tests/unit/test_hdd.py
"""
import pytest
import sys
sys.path.append('/home/vin/OOP_object_oriented_programming/3_computer_builds/app/models')
from inventory import HDD

@pytest.fixture
def hdd_values():
    return {
        "name": "1TB SATA HDD",
        "manufacturer": "Seagate",
        "total": 10,
        "allocated": 3,
        "capacity_gb": 1_000,
        "size": '3.5"',
        "rpm": 10_000
    }

@pytest.fixture
def hdd(hdd_values):
    return HDD(**hdd_values)

def test_create(hdd, hdd_values):
    for attr_name in hdd_values:
        assert getattr(hdd, attr_name) == hdd_values.get(attr_name)
    
@pytest.mark.parametrize("size", ["2.5", '5.25"'])
def test_create_invalid_size(size, hdd_values):
    hdd_values["size"] = size
    with pytest.raises(ValueError):
        HDD(**hdd_values)

@pytest.mark.parametrize(
    "rpm, exception",
    [
        ("100", TypeError),
        (100, ValueError),
        (100_100, ValueError)
    ]
)
def test_create_invalid_rpm(rpm, exception, hdd_values):
    hdd_values["rpm"] = rpm
    with pytest.raises(exception):
        HDD(**hdd_values)

def test_repr(hdd):
    assert hdd.category in repr(hdd)
    assert str(hdd.capacity_gb) in repr(hdd)
    assert hdd.size in repr(hdd)
    assert str(hdd.rpm) in repr(hdd)
    