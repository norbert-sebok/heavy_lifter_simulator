"""HeavyLifter Simulator

Usage:
  heavy_lifter_simulator.py <path>
  heavy_lifter_simulator.py -h | --help
  heavy_lifter_simulator.py --version

Options:
  -h --help     Show this screen
  --version     Show version
"""
from docopt import docopt

from simulator.loader import load_instruction_set
from simulator.move import simulate_instruction_set


if __name__ == '__main__':
    arguments = docopt(__doc__, version='HeavyLifter Simulator 0.1')

    with open(arguments['<path>']) as f:
        text = f.read()

    instruction_set = load_instruction_set(text)
    simulate_instruction_set(instruction_set)
