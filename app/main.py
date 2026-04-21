from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(
        self,
        other: Union["Distance", int, float],
    ) -> Union[float, NotImplemented]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(
        self,
        other: Union["Distance", int, float],
    ) -> Union["Distance", NotImplemented]:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(
        self,
        other: Union["Distance", int, float],
    ) -> Union["Distance", NotImplemented]:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(
        self,
        other: Union["Distance", int, float],
    ) -> bool:
        return self.km < self._get_value(other)

    def __gt__(
        self,
        other: Union["Distance", int, float],
    ) -> bool:
        return self.km > self._get_value(other)

    def __eq__(
        self,
        other: Union["Distance", int, float],
    ) -> bool:
        return self.km == self._get_value(other)

    def __le__(
        self,
        other: Union["Distance", int, float],
    ) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(
        self,
        other: Union["Distance", int, float],
    ) -> bool:
        return self.km >= self._get_value(other)
