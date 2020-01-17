import pytest
import json
from gen_diff.scripts.gendiff import generate_diff

# did json - file
# file = open('/home/aleksbel/example/python-project-lvl2/tests/fixtures/expectation_step4.json', 'r')
# expectation_step4 = file.read()
# print(type(expectation_step4), expectation_step4)
# expectation_step4 = {'- timeout': 20, '- proxy': '123.234.53.22', '+ verbose': True, '+ timeout': 50, 'host': 'hexlet.io'}
# expectation_step4 = json.load(open('/home/aleksbel/example/python-project-lvl2/tests/fixtures/expectation_step4.json'))
expectation_step4 = json.load(open('tests/fixtures/expectation_step4.json'))


def test_gen_diff_files():
    # gen_diff_result = generate_diff('/home/aleksbel/example/python-project-lvl2/tests/fixtures/step4_before.json', '/home/aleksbel/example/python-project-lvl2/tests/fixtures/step4_after.json')
    gen_diff_result = generate_diff('tests/fixtures/step4_before.json', 'tests/fixtures/step4_after.json')
    assert expectation_step4 == json.loads(gen_diff_result)
