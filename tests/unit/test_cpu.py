"""
Tests for CPU class
Command line: python3 -m pytest tests/unit/test_cpu.py
"""

import pytest
import sys
sys.path.append('/home/vin/OOP_object_oriented_programming/3_computer_builds/app/models')
from inventory import CPU

@pytest.fixture
def cpu_values():
    return {
        "name": "Ryzen Threadripper 2990WX",
        "manufacturer": "AMD",
        "total": 10,
        "allocated": 3,
        "cores": 32,
        "socket": "sTR4",
        "power_watts": 250
    }

@pytest.fixture
def cpu(cpu_values):
    return CPU(**cpu_values)

def test_create_cpu(cpu, cpu_values):
    for attr_name in cpu_values:
        assert getattr(cpu, attr_name) == cpu_values.get(attr_name)

@pytest.mark.parametrize(
    "cores, exception", [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
)
def test_create_invalid_cores(cores, exception, cpu_values):
    cpu_values["cores"] = cores
    with pytest.raises(exception):
        CPU(**cpu_values)

@pytest.mark.parametrize(
    "watts, exception", [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
)
def test_create_invalid_power(watts, exception, cpu_values):
    cpu_values["power_watts"] = watts
    with pytest.raises(exception):
        CPU(**cpu_values)
    
def test_repr(cpu):
    assert cpu.category in repr(cpu)
    assert cpu.name in repr(cpu)
    assert cpu.socket in repr(cpu)
    assert str(cpu.cores) in repr(cpu)
    