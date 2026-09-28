import json, os, sys, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validator import validate_domain_annotation

def test_sme_gold_dataset():
    path = os.path.join(os.path.dirname(__file__), '../data/sme_gold_dataset.json')
    with open(path) as f:
        data = json.load(f)
    assert len(data) >= 2
    for item in data:
        errs = validate_domain_annotation(item)
        assert len(errs) == 0

def test_invalid_domain_item():
    bad = {"prompt_id": "ERR-1", "domain": "Finance", "rationale": "Short"}
    errs = validate_domain_annotation(bad)
    assert len(errs) > 0
