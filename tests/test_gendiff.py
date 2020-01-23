#!/usr/bin/env python3


import pytest
import json
from gen_diff.scripts.gendiff import generate_diff


expectation_step4 = json.load(open('tests/fixtures/expectation_step4.json'))


def test_gen_yml():
    gen_diff_result = generate_diff('tests/fixtures/step5_before.yml', 'tests/fixtures/step5_after.yml')
    assert expectation_step4 == json.loads(gen_diff_result)


def test_gen_diff_json():
    gen_diff_result = generate_diff('tests/fixtures/step4_before.json', 'tests/fixtures/step4_after.json')
    assert expectation_step4 == json.loads(gen_diff_result)
