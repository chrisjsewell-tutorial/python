import argparse

import matplotlib.pyplot as plt

from .plot import plt_oscillator


def main():
    """Create CLI for plotting"""
    parser = argparse.ArgumentParser(description="Plot the harmonic oscillator")
    parser.add_argument("-n", "--number", action="store", type=int, default=8)
    args = parser.parse_args()
    plt_oscillator(args.number)
    plt.show()
