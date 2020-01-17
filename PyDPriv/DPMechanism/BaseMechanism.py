from abc import ABC, abstractmethod


class BaseMechanism(ABC):
    """
    Base class for all DP mechanisms, abstracted.
    """
    def __init__(self):
        self._eps = None
        self._delta = None
        self._type = None

    @abstractmethod
    def noisy(self, val):
        return NotImplemented

    @abstractmethod
    def var(self, val):
        return NotImplemented

    @abstractmethod
    def mse(self, val):
        return NotImplemented

    def set_eps_delta(self, eps, delta=0.0):
        if not 0 <= delta <= 1:
            raise ValueError("Delta must be in range [0, 1].")
        if eps < 0:
            raise ValueError("Epsilon must be non-negative.")
        if eps == 0 and delta == 0:
            raise ValueError("There must be at least one parameter being non-zero.")

        self._eps = float(eps)
        self._delta = float(delta)

        return self

