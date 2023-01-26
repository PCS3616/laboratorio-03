import pytest
from pathlib import Path

from turingmachine import load, run_test

submission_path = Path("./submission")
autogradle_path = Path("./autogradle")
mt_input_path = Path("./inputs")


def test_1():
    img = submission_path / 'mt_soma.svg'
    # assert img.exists(), f"A submissão não contem o arquivo '{img.name}'"

    mt = submission_path / 'mt_soma.txt'
    mt_in = mt_input_path / 'ex1-soma.in'

    assert mt.exists(), "A submissão não contém o arquivo 'mt_soma.txt'"

    load(mt.as_posix())
    run_test(mt_in.as_posix())

def test_2():
    img = submission_path / 'mt_subtracao.svg'
    # assert img.exists(), f"A submissão não contem o arquivo '{img.name}'"

    mt = submission_path / 'mt_subtracao.txt'
    mt_in = mt_input_path / 'ex2-subtracao.in'

    assert mt.exists(), "A submissão não contém o arquivo 'mt_subtracao.txt'"

    load(mt.as_posix())
    run_test(mt_in.as_posix())

def test_3():
    img = submission_path / 'mt_soma_binaria.svg'
    # assert img.exists(), f"A submissão não contem o arquivo '{img.name}'"

    mt = submission_path / 'mt_soma_binaria.txt'
    mt_in = mt_input_path / 'ex4-soma-binaria.in'

    assert mt.exists(), "A submissão não contém o arquivo 'mt_soma_binaria.txt'"

    load(mt.as_posix())
    run_test(mt_in.as_posix())
