import enum
from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Protocol,
    Tuple,
    TypeVar,
    Union,
    runtime_checkable,
)

if TYPE_CHECKING:
    from builtins import ellipsis


VendoredDtype = Any
VendoredDevice = Any
VendoredArrayNamespace = Any
VendoredPyCapsule = Any
VendoredShape = Tuple[int, ...]


A = TypeVar("A")


@runtime_checkable
class VendoredArrayProtocol(Protocol[A]):
    @property
    def dtype(self) -> VendoredDtype:
        ...

    # @property
    # def device(self) -> VendoredDevice:
    #     ...

    @property
    def ndim(self) -> int:
        ...

    @property
    def shape(self) -> VendoredShape:
        ...

    @property
    def size(self) -> int:
        ...

    @property
    def T(self) -> A:
        ...

    def __abs__(self) -> A:
        ...

    def __add__(self, other: Union[int, float, A], /) -> A:
        ...

    def __and__(self, other: Union[bool, int, A], /) -> A:
        ...

    # def __array_namespace__(
    #     self, /, *, api_version: Optional[str] = None
    # ) -> VendoredArrayNamespace:
    #     ...

    def __bool__(self) -> bool:
        ...

    # def __dlpack__(
    #     self, /, *, stream: Optional[Union[int, Any]] = None
    # ) -> VendoredPyCapsule:
    #     ...

    # def __dlpack_device__(self) -> Tuple[enum.IntEnum, int]:
    #     ...

    # This overrides the input type, since object.__eq__ handles any input
    # This overrides the return type, since object.__eq__ returns a bool
    def __eq__(  # type: ignore[override]
        self,
        other: Union[bool, int, float, A],
        /,
    ) -> A:  # type: ignore[override]
        ...

    def __float__(self) -> float:
        ...

    def __floordiv__(self, other: Union[int, float, A], /) -> A:
        ...

    def __ge__(self, other: Union[int, float, A], /) -> A:
        ...

    def __getitem__(
        self,
        key: Union[
            int,
            slice,
            "ellipsis",
            Tuple[Union[int, slice, "ellipsis"], ...],
            A,
        ],
        /,
    ) -> A:
        ...

    def __gt__(self, other: Union[int, float, A], /) -> A:
        ...

    def __int__(self) -> int:
        ...

    def __invert__(self) -> A:
        ...

    def __le__(self, other: Union[int, float, A], /) -> A:
        ...

    def __len__(self) -> int:
        ...

    def __lshift__(self, other: Union[int, A], /) -> A:
        ...

    def __lt__(self, other: Union[int, float, A], /) -> A:
        ...

    def __matmul__(self, other: A) -> A:
        ...

    def __mod__(self, other: Union[int, float, A], /) -> A:
        ...

    def __mul__(self, other: Union[int, float, A], /) -> A:
        ...

    # This overrides the input type, since object.__ne__ handles any input
    # This overrides the return type, since object.__ne__ returns a bool
    def __ne__(  # type: ignore[override]
        self, other: Union[bool, int, float, A], /
    ) -> A:  # type: ignore[override]
        ...

    def __neg__(self) -> A:
        ...

    def __or__(self, other: Union[bool, int, A], /) -> A:
        ...

    def __pos__(self) -> A:
        ...

    def __pow__(self, other: Union[int, float, A], /) -> A:
        ...

    def __rshift__(self, other: Union[int, A], /) -> A:
        ...

    def __setitem__(
        self,
        key: Union[
            int,
            slice,
            "ellipsis",
            Tuple[Union[int, slice, "ellipsis"], ...],
            A,
        ],
        value: Union[bool, int, float, A],
        /,
    ) -> None:
        ...

    def __sub__(self, other: Union[int, float, A], /) -> A:
        ...

    def __truediv__(self, other: Union[int, float, A], /) -> A:
        ...

    def __xor__(self, other: Union[bool, int, A], /) -> A:
        ...
