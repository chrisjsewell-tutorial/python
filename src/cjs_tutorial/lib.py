from __future__ import annotations

from math import exp, factorial, pi, sqrt
from typing import Callable


def norm(v: int) -> float:
    """Normalization constant"""
    return 1.0 / sqrt(sqrt(pi) * 2**v * factorial(v))


# note could also use from scipy.special.hermite
_HERMITES: dict[int, Callable[[float], float]] = {
    0: lambda x: 1,
    1: lambda x: 2 * x,
    2: lambda x: 4 * x**2 - 2,
    3: lambda x: 8 * x**3 - 12 * x,
    4: lambda x: 16 * x**4 - 48 * x**2 + 12,
    5: lambda x: 32 * x**5 - 160 * x**3 + 120 * x,
    6: lambda x: 64 * x**6 - 480 * x**4 + 720 * x**2 - 120,
    7: lambda x: 128 * x**7 - 1344 * x**5 + 3360 * x**3 - 1680 * x,
    8: lambda x: 256 * x**8 - 3584 * x**6 + 13440 * x**4 - 13440 * x**2 + 1680,
    9: lambda x: 512 * x**9
    - 9216 * x**7
    + 48384 * x**5
    - 80640 * x**3
    + 30240 * x,
    10: lambda x: 1024 * x**10
    - 30720 * x**8
    + 180224 * x**6
    - 300720 * x**4
    + 158720 * x**2
    - 30240,
}


def get_hermite_poly(v: int) -> Callable[[float], float]:
    """Return the hermite polynomial for the given level"""
    return _HERMITES[v]


def psi(v: int, xs: list[float]) -> list[float]:
    """Harmonic oscillator wavefunction for level v computed on grid of points x"""
    hermite_poly = get_hermite_poly(v)
    psi_x = []
    for x_i in xs:
        psi_x.append(norm(v) * hermite_poly(x_i) * exp(-0.5 * x_i**2))
    return psi_x


def psi_squared(v: int, xs: list[float], shift: float = 0) -> list[float]:
    """Harmonic oscillator wavefunction for level v computed on grid of points x"""
    return [x**2 + shift for x in psi(v, xs)]


def eigenvalue(v: int) -> float:
    """Eigenvalues in units of h"""
    return v + 0.5


def potential_energy(xs: list[float]) -> list[float]:
    """Potential energy function"""
    return [0.5 * xi**2 for xi in xs]


def linspace(start: float, stop: float, num: int) -> list[float]:
    """Linearly spaced list of numbers"""
    return [start + (stop - start) * i / (num - 1) for i in range(num)]
