from simulator.loader import load_instruction_set
from simulator.models import Move

set_1 = """\
|K|
|A| |Q|     |F|
|P| |U| |B| |T|
 1   2   3   4
     bottom

move 1 from 3 to 4
move 2 from 1 to 3
move 1 from 1 to 2
move 2 from 4 to 1
"""


def test_loading_set_1():
    instruction_set = load_instruction_set(set_1)

    assert len(instruction_set.stacks) == 4

    assert instruction_set.stacks[0].title == '1'
    assert instruction_set.stacks[1].title == '2'
    assert instruction_set.stacks[2].title == '3'
    assert instruction_set.stacks[3].title == '4'

    assert [box.letter for box in instruction_set.stacks[0].boxes] == ['P', 'A', 'K']
    assert [box.letter for box in instruction_set.stacks[1].boxes] == ['U', 'Q']
    assert [box.letter for box in instruction_set.stacks[2].boxes] == ['B']
    assert [box.letter for box in instruction_set.stacks[3].boxes] == ['T', 'F']

    assert len(instruction_set.moves) == 4

    assert instruction_set.moves[0] == Move(count=1, from_index=3, to_index=4)
    assert instruction_set.moves[1] == Move(count=2, from_index=1, to_index=3)
    assert instruction_set.moves[2] == Move(count=1, from_index=1, to_index=2)
    assert instruction_set.moves[3] == Move(count=2, from_index=4, to_index=1)
