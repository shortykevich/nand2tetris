import os
import pytest

from hack_assembler.assembler import HackAssembler

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "binFiles")


@pytest.fixture
def max_res():
    file = FIXTURES_DIR + "/" + "MaxRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def add_res():
    file = FIXTURES_DIR + "/" + "AddRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def max_l_res():
    file = FIXTURES_DIR + "/" + "MaxLRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def pong_res():
    file = FIXTURES_DIR + "/" + "PongRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def pong_l_res():
    file = FIXTURES_DIR + "/" + "PongLRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def rect_res():
    file = FIXTURES_DIR + "/" + "RectRes"
    with open(file, "r") as f:
        return f.read().splitlines()


@pytest.fixture
def rect_l_res():
    file = FIXTURES_DIR + "/" + "RectLRes"
    with open(file, "r") as f:
        return f.read().splitlines()


def test_add(add_res):
    add_hack = HackAssembler("Add.asm")
    assert add_hack.generate_bin_code() == add_res


def test_max(max_res):
    max_hack = HackAssembler("Max.asm")
    assert max_hack.generate_bin_code() == max_res


def test_max_l(max_l_res):
    max_l_hack = HackAssembler("MaxL.asm")
    assert max_l_hack.generate_bin_code() == max_l_res


def test_pong(pong_res):
    pong_hack = HackAssembler("Pong.asm")
    assert pong_hack.generate_bin_code() == pong_res


def test_pong_l(pong_l_res):
    pong_l_hack = HackAssembler("PongL.asm")
    assert pong_l_hack.generate_bin_code() == pong_l_res


def test_rect(rect_res):
    rect_hack = HackAssembler("Rect.asm")
    assert rect_hack.generate_bin_code() == rect_res


def test_rect_l(rect_l_res):
    rect_l_hack = HackAssembler("RectL.asm")
    assert rect_l_hack.generate_bin_code() == rect_l_res
