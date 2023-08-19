from simulator.models import Box, Move, Stack
from simulator.move import process_one_move
from tests.move.test_move_all_steps import assert_stack_letters


def test_moving_step_by_step():
    stacks = [
        Stack('1', [Box('P'), Box('A'), Box('K')]),
        Stack('2', [Box('U'), Box('Q')]),
        Stack('3', [Box('B')]),
        Stack('4', [Box('T'), Box('F')]),
    ]

    assert_stack_letters(
        stacks,
        [
            ['P', 'A', 'K'],
            ['U', 'Q'],
            ['B'],
            ['T', 'F'],
        ],
    )

    process_one_move(stacks, Move(1, 3, 4))

    assert_stack_letters(
        stacks,
        [
            ['P', 'A', 'K'],
            ['U', 'Q'],
            [],
            ['T', 'F', 'B'],
        ],
    )

    process_one_move(stacks, Move(2, 1, 3))

    assert_stack_letters(
        stacks,
        [
            ['P'],
            ['U', 'Q'],
            ['K', 'A'],
            ['T', 'F', 'B'],
        ],
    )

    process_one_move(stacks, Move(1, 1, 2))

    assert_stack_letters(
        stacks,
        [
            [],
            ['U', 'Q', 'P'],
            ['K', 'A'],
            ['T', 'F', 'B'],
        ],
    )

    process_one_move(stacks, Move(2, 4, 1))

    assert_stack_letters(
        stacks,
        [
            ['B', 'F'],
            ['U', 'Q', 'P'],
            ['K', 'A'],
            ['T'],
        ],
    )
