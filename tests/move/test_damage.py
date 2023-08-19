import pytest

from simulator.models import Box, Move, Stack
from simulator.move import EquipmentDamaged, process_one_move


def test_damage():
    stacks = [
        Stack('1', [Box('P'), Box('A'), Box('K')]),
        Stack('2', []),
    ]

    with pytest.raises(EquipmentDamaged) as exc_info:
        process_one_move(stacks, Move(4, 1, 2))

    assert str(exc_info.value) == 'Not enough boxes in stack 1'
