from typing import List

from simulator.models import Box, InstructionSet, Move, Stack
from simulator.move import simulate_instruction_set


def test_moving_all_steps():
    instruction_set = InstructionSet(
        stacks=[
            Stack('1', [Box('P'), Box('A'), Box('K')]),
            Stack('2', [Box('U'), Box('Q')]),
            Stack('3', [Box('B')]),
            Stack('4', [Box('T'), Box('F')]),
        ],
        moves=[
            Move(1, 3, 4),
            Move(2, 1, 3),
            Move(1, 1, 2),
            Move(2, 4, 1),
        ],
    )

    top_boxes = simulate_instruction_set(instruction_set)

    assert_stack_letters(
        instruction_set.stacks,
        [
            ['B', 'F'],
            ['U', 'Q', 'P'],
            ['K', 'A'],
            ['T'],
        ],
    )

    assert top_boxes == 'FPAT'


def assert_stack_letters(stacks: List[Stack], expected=List[List[str]]):
    current = [[box.letter for box in stack.boxes] for stack in stacks]
    assert current == expected
