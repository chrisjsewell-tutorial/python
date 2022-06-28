from math import sqrt

import matplotlib.pyplot as plt

from .lib import eigenvalue, linspace, potential_energy, psi_squared


def plt_oscillator(vmax: int = 8) -> plt.Axes:
    """Plot up to level vmax."""

    # Range of x determine by classical turning points:
    xmin, xmax = -sqrt(2 * eigenvalue(vmax)), sqrt(2 * eigenvalue(vmax))

    xs = linspace(xmin, xmax, 1000)

    fig, ax = plt.subplots(figsize=(8, 8))

    # plot potential V(x)
    ax.plot(xs, potential_energy(xs), color="black")

    for v in range(vmax):

        # plot psi squared which we shift up by values of energy
        ax.plot(xs, psi_squared(v, xs, eigenvalue(v)), lw=2)

        # add lines and labels
        ax.axhline(eigenvalue(v), color="gray", linestyle="--")
        ax.text(xmax, eigenvalue(v), f"v={v}")

    ax.set_xlabel("x")
    ax.set_ylabel(r"$\psi^2_n(x)$")

    return fig, ax
