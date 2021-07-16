import enum
from typing import TYPE_CHECKING, Any, Optional, Tuple, Union

if TYPE_CHECKING:
    from builtins import ellipsis


class ArrayImplementation:
    @property
    def dtype(self) -> object:
        return object()

    @property
    def device(self) -> object:
        return object()

    @property
    def ndim(self) -> int:
        return 0

    @property
    def shape(self) -> Tuple[int, ...]:
        return (0,)

    @property
    def size(self) -> int:
        return 0

    @property
    def T(self) -> "ArrayImplementation":
        return self

    def __abs__(self) -> "ArrayImplementation":
        return self

    def __add__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __and__(
        self, other: Union[bool, int, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __array_namespace__(self, /, *, api_version: Optional[str] = None) -> object:
        return object()

    def __bool__(self) -> bool:
        return False

    def __dlpack__(self, /, *, stream: Optional[Union[int, Any]] = None) -> object:
        return object()

    def __dlpack_device__(self) -> Tuple[enum.IntEnum, int]:
        class Foo(enum.IntEnum):
            bar = 0

        return Foo.bar, 0

    # This overrides the input type, since object.__eq__ handles any input
    # This overrides the return type, since object.__eq__ returns a bool
    def __eq__(  # type: ignore[override]
        self: "ArrayImplementation",
        other: Union[bool, int, float, "ArrayImplementation"],
        /,
    ) -> "ArrayImplementation":  # type: ignore[override]
        return self

    def __float__(self) -> float:
        return 0.0

    def __floordiv__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __ge__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __getitem__(
        self,
        key: Union[
            int,
            slice,
            "ellipsis",
            Tuple[Union[int, slice, "ellipsis"], ...],
            "ArrayImplementation",
        ],
        /,
    ) -> "ArrayImplementation":
        return self

    def __gt__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __int__(self) -> int:
        return 0

    def __invert__(self) -> "ArrayImplementation":
        return self

    def __le__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __len__(self) -> int:
        return 0

    def __lshift__(
        self, other: Union[int, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __lt__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __matmul__(self, other: "ArrayImplementation") -> "ArrayImplementation":
        return self

    def __mod__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __mul__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    # This overrides the input type, since object.__ne__ handles any input
    # This overrides the return type, since object.__ne__ returns a bool
    def __ne__(  # type: ignore[override]
        self: "ArrayImplementation",
        other: Union[bool, int, float, "ArrayImplementation"],
        /,
    ) -> "ArrayImplementation":  # type: ignore[override]
        return self

    def __neg__(self) -> "ArrayImplementation":
        return self

    def __or__(
        self, other: Union[bool, int, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __pos__(self) -> "ArrayImplementation":
        return self

    def __pow__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __rshift__(
        self, other: Union[int, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __setitem__(
        self,
        key: Union[
            int,
            slice,
            "ellipsis",
            Tuple[Union[int, slice, "ellipsis"], ...],
            "ArrayImplementation",
        ],
        value: Union[bool, int, float, "ArrayImplementation"],
        /,
    ) -> None:
        return None

    def __sub__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __truediv__(
        self, other: Union[int, float, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self

    def __xor__(
        self, other: Union[bool, int, "ArrayImplementation"], /
    ) -> "ArrayImplementation":
        return self
