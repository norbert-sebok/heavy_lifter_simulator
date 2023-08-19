"""
The internal data structure
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Box:
    letter: str


@dataclass
class Stack:
    title: str
    boxes: List[Box]


@dataclass
class Move:
    count: int
    from_index: int
    to_index: int


@dataclass
class InstructionSet:
    stacks: List[Stack]
    moves: List[Move]
