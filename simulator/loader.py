"""
Instruction set loader

Converts the instruction set file content to the internal Python dataclass objects
"""

import re
from typing import List, Tuple

from simulator.models import Box, InstructionSet, Move, Stack


def load_instruction_set(text: str) -> InstructionSet:
    stack_lines, move_lines = get_stack_and_move_lines(text)

    stacks = get_stacks(stack_lines)
    moves = get_moves(move_lines)

    return InstructionSet(stacks, moves)


def get_stack_and_move_lines(text: str) -> Tuple[List[str], List[str]]:
    lines = text.split('\n')

    bottom_line = [line for line in lines if line.strip() == 'bottom'][0]
    bottom_index = lines.index(bottom_line)

    stack_lines = lines[:bottom_index]
    move_lines = lines[bottom_index + 1 :]

    return stack_lines, move_lines


def get_stacks(stack_lines: List[str]) -> List[Stack]:
    titles_line = stack_lines[-1]
    box_lines_reversed = reversed(stack_lines[:-1])

    value_indexes = [index for index, value in enumerate(titles_line) if value.strip()]
    titles = [titles_line[index] for index in value_indexes]
    stacks = [Stack(title, []) for title in titles]

    for line in box_lines_reversed:
        for stack, index in zip(stacks, value_indexes):
            try:
                value = line[index].strip()
            except IndexError:
                value = ''

            if value:
                stack.boxes.append(Box(value))

    return stacks


def get_moves(move_lines: List[str]) -> List[Move]:
    moves = []

    for line in move_lines:
        values = re.findall(r'move (\d+) from (\d+) to (\d+)', line)

        for count, from_index, to_index in values:
            moves.append(Move(int(count), int(from_index), int(to_index)))

    return moves
