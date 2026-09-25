import pytest
from dummy_backend.app import process_items, items, db

def test_process_items():
    results = process_items(items[:5], db)
    assert len(results) == 5
    assert results[0].item_id == 1
    assert "Detail for item 1" in results[0].data
