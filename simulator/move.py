"""
The move simulator
"""

from typing import List

from simulator.models import InstructionSet, Move, Stack


class EquipmentDamaged(Exception):
    pass


def simulate_instruction_set(instruction_set: InstructionSet) -> str:
    print('Initial state:')
    print_stack(instruction_set.stacks)

    for move in instruction_set.moves:
        process_one_move(instruction_set.stacks, move)
        print_move(move)
        print_stack(instruction_set.stacks)

    top_boxes = get_top_boxes(instruction_set.stacks)
    print('\nTop boxes:')
    print(top_boxes)

    return top_boxes


def process_one_move(stacks: List[Stack], move: Move):
    for _ in range(move.count):
        boxes = stacks[move.from_index - 1].boxes

        if boxes:
            box = boxes.pop(-1)
            stacks[move.to_index - 1].boxes.append(box)
        else:
            raise EquipmentDamaged(f'Not enough boxes in stack {move.from_index}')


def get_top_boxes(stacks: List[Stack]) -> str:
    return ''.join(stack.boxes[-1].letter if stack.boxes else '' for stack in stacks)


def print_move(move: Move):
    box_title = 'box' if move.count == 1 else 'boxes'
    print(
        f'\nMoved {move.count} {box_title} '
        f'from {move.from_index} '
        f'to {move.to_index}:'
    )


def print_stack(stacks: List[Stack]):
    for stack in stacks:
        box_letters = ''.join(box.letter for box in stack.boxes)
        print(f' {stack.title}: {box_letters}')
