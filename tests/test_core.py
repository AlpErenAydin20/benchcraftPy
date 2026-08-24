import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
import time
from benchcraft.core import BenchCraft
from benchcraft.utils import format_bytes

# format_bytes fonksiyonu doğru dönüşümleri yapıyor mu?
def test_format_bytes():
    assert format_bytes(500) == "500 B"
    assert format_bytes(2048) == "2.00 KB"
    assert format_bytes(1048576 * 5) == "5.00 MB"

# Decorator orijinal fonksiyonun döndürdüğü değeri bozuyor mu?
def test_benchcraft_return_value():
    @BenchCraft(unit="ms")
    def topla(a, b):
        return a + b
    
    assert topla(3, 5) == 8

# Decorator fonksiyonun adını (metadata) koruyor mu? (@wraps testi)
def test_benchcraft_metadata():
    @BenchCraft()
    def ornek_fonksiyon():
        pass
    
    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"