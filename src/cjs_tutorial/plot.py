from math import sqrt

import matplotlib.pyplot as plt

from .lib import eigenvalue, linspace, potential_energy, psi_squared


def plt_oscillator(vmax: int = 8) -> plt.Axes:
    """Plot up to level vmax."""

    # Range of x determine by classical turning points:
    xmin, xmax = -sqrt(2 * eigenvalue(vmax)), sqrt(2 * eigenvalue(vmax))

    x = linspace(xmin, xmax, 1000)

    fig, ax = plt.subplots(figsize=(8, 8))

    for v in range(8):

        # plot potential V(x)
        ax.plot(x, potential_energy(x), color="black")

        # plot psi squared which we shift up by values of energy
        ax.plot(x, psi_squared(v, x, eigenvalue(v)), lw=2)

        # add lines and labels
        ax.axhline(eigenvalue(v), color="gray", linestyle="--")
        ax.text(xmax, eigenvalue(v), f"v={v}")


    ax.set_xlabel("x")
    ax.set_ylabel("$\psi^2_n(x)$")

    return fig, ax
