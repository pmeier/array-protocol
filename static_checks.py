import enum
from typing import Any, Optional, Tuple, TypeVar, Union

from consumer import (
    VendoredArrayNamespace,
    VendoredArrayProtocol,
    VendoredDevice,
    VendoredDtype,
    VendoredPyCapsule,
    VendoredShape,
)

import numpy

AIT = numpy.ndarray
AI = numpy.array(1.0)
VAP = TypeVar("VAP", bound=VendoredArrayProtocol)


# dtype
def test_dtype(self: VAP) -> VendoredDtype:
    return self.dtype


DTYPE: VendoredDtype = test_dtype(AI)

# # device
# def test_device(self: VAP) -> VendoredDevice:
#     return self.dtype
#
#
# DEVICE: VendoredDevice = test_device(AI)

# ndim
def test_ndim(self: VAP) -> int:
    return self.ndim


NDIM: int = test_ndim(AI)

# shape
def test_shape(self: VAP) -> VendoredShape:
    return self.shape


SHAPE: VendoredShape = test_shape(AI)

# size
def test_size(self: VAP) -> int:
    return self.size


SIZE: int = test_size(AI)

# T
def test_T(self: VAP) -> VAP:
    return self.T


T: AIT = test_T(AI)


# __abs__
def test_abs(self: VAP) -> VAP:
    return abs(self)


ABS: AIT = test_abs(AI)


# __add__
def test_add(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self + other


ADD_INT: AIT = test_add(AI, 0)
ADD_FLOAT: AIT = test_add(AI, 0.0)
ADD_ARRAY: AIT = test_add(AI, AI)

# __and__
def test_and(self: VAP, other: Union[bool, int, VAP]) -> VAP:
    return self & other


AND_BOOL = test_and(AI, False)
AND_INT = test_and(AI, 0)
AND_ARRAY = test_and(AI, AI)

# # __array_namespace__
# def test_array_namespace(
#     self: VAP, api_version: Optional[str] = None
# ) -> VendoredArrayNamespace:
#     return self.__array_namespace__(api_version=api_version)
#
#
# ARRAY_NAMESPACE_NONE: Any = test_array_namespace(AI, api_version=None)
# ARRAY_NAMESPACE_STR: Any = test_array_namespace(AI, api_version="api_version")
#
# __bool__
def test_bool(self: VAP) -> bool:
    return bool(self)


BOOL: bool = test_bool(AI)

# # __dlpack__
# def test_dlpack(self: VAP, stream: Any = None) -> VendoredPyCapsule:
#     return self.__dlpack__(stream=stream)
#
#
# DLPACK_NONE: VendoredPyCapsule = test_dlpack(AI, stream=None)
# DLPACK_INT: VendoredPyCapsule = test_dlpack(AI, stream=0)
# DLPACK_OBJECT: VendoredPyCapsule = test_dlpack(AI, stream=object())
#
# # __dlpack_device__
# def test_dlpack_device(self: VAP) -> Tuple[enum.IntEnum, int]:
#     return self.__dlpack_device__()
#
#
# DLPACK_DEVICE: Tuple[enum.IntEnum, int] = test_dlpack_device(AI)
#
# __eq__
def test_eq(self: VAP, other: Any) -> VAP:
    return self == other


EQ_BOOL: AIT = test_eq(AI, False)
EQ_INT: AIT = test_eq(AI, 0)
EQ_FLOAT: AIT = test_eq(AI, 0.0)
EQ_ARRAY: AIT = test_eq(AI, AI)

# __float__
def test_float(self: VAP) -> float:
    return float(self)


FLOAT: float = test_float(AI)

# __floordiv__
def test_floordiv(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self + other


FLOORDIV_INT: AIT = test_floordiv(AI, 0)
FLOORDIV_FLOAT: AIT = test_floordiv(AI, 0.0)
FLOORDIV_ARRAY: AIT = test_floordiv(AI, AI)

# __ge__
def test_ge(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self >= other


GE_INT: AIT = test_ge(AI, 0)
GE_FLOAT: AIT = test_ge(AI, 0.0)
GE_ARRAY: AIT = test_ge(AI, AI)


# __getitem__
GETITEM_INT: AIT = AI[0]
GETITEM_SLICE1: AIT = AI[:]
GETITEM_SLICE2: AIT = AI[0:]
GETITEM_SLICE3: AIT = AI[:-1]
GETITEM_SLICE4: AIT = AI[0:-1]
GETITEM_INT_SLICE: AIT = AI[0, :]
GETITEM_SLICE_INT: AIT = AI[:, 0]
GETITEM_ELLIPSIS_INT: AIT = AI[..., 0]
GETITEM_SLICE_ELLIPSIS: AIT = AI[:, ...]
GETITEM_SLICE_ELLIPSIS_INT: AIT = AI[:, ..., 0]
GETITEM_ARRAY: AIT = AI[AI]


# __gt__
def test_gt(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self > other


GT_INT: AIT = test_gt(AI, 0)
GT_FLOAT: AIT = test_gt(AI, 0.0)
GT_ARRAY: AIT = test_gt(AI, AI)

# __int__
def test_int(self: VAP) -> int:
    return int(self)


INT: int = test_int(AI)

# __invert__
def test_invert(self: VAP) -> VAP:
    return ~self


INVERT: AIT = test_invert(AI)

# __le__
def test_le(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self <= other


LE_INT: AIT = test_le(AI, 0)
LE_FLOAT: AIT = test_le(AI, 0.0)
LE_ARRAY: AIT = test_le(AI, AI)

# __len__
def test_len(self: VAP) -> int:
    return len(self)


LEN: int = test_len(AI)

# __lshift__
def test_lshift(self: VAP, other: Union[int, VAP]) -> VAP:
    return self << other


LSHIFT_INT: AIT = test_lshift(AI, 0)
LSHIFT_ARRAY: AIT = test_lshift(AI, AI)


# __le__
def test_lt(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self < other


LT_INT: AIT = test_lt(AI, 0)
LT_FLOAT: AIT = test_lt(AI, 0.0)
LT_ARRAY: AIT = test_lt(AI, AI)

# __matmul__
def test_matmul(self: VAP, other: VAP) -> VAP:
    return self @ other


MATMUL: AIT = test_matmul(AI, AI)

# __mod__
def test_mod(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self % other


MOD_INT: AIT = test_mod(AI, 0)
MOD_FLOAT: AIT = test_mod(AI, 0.0)
MOD_ARRAY: AIT = test_mod(AI, AI)


# __mul__
def test_mul(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self * other


MUL_INT: AIT = test_mul(AI, 0)
MUL_FLOAT: AIT = test_mul(AI, 0.0)
MUL_ARRAY: AIT = test_mul(AI, AI)

# __ne__
def test_ne(self: VAP, other: Any) -> VAP:
    return self != other


NE_BOOL: AIT = test_eq(AI, False)
NE_INT: AIT = test_eq(AI, 0)
NE_FLOAT: AIT = test_eq(AI, 0.0)
NE_ARRAY: AIT = test_eq(AI, AI)


# __neg__
def test_neg(self: VAP) -> VAP:
    return -self


NEG: AIT = test_neg(AI)


# __or__
def test_or(self: VAP, other: Union[bool, int, VAP]) -> VAP:
    return self | other


OR_BOOL = test_or(AI, False)
OR_INT = test_or(AI, 0)
OR_ARRAY = test_or(AI, AI)

# __pos__
def test_pos(self: VAP) -> VAP:
    return +self


POS: AIT = test_pos(AI)

# __pow__
def test_pow(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self ** other


POW_INT: AIT = test_pow(AI, 0)
POW_FLOAT: AIT = test_pow(AI, 0.0)
POW_ARRAY: AIT = test_pow(AI, AI)


# __rshift__
def test_rshift(self: VAP, other: Union[int, VAP]) -> VAP:
    return self << other


RSHIFT_INT: AIT = test_rshift(AI, 0)
RSHIFT_ARRAY: AIT = test_rshift(AI, AI)

# __setitem__
AI[0] = False
AI[:] = False
AI[0:] = False
AI[:-1] = False
AI[0:-1] = False
AI[0, :] = False
AI[:, 0] = False
AI[..., 0] = False
AI[:, ...] = False
AI[:, ..., 0] = False
AI[AI] = False

AI[0] = 0
AI[:] = 0
AI[0:] = 0
AI[:-1] = 0
AI[0:-1] = 0
AI[0, :] = 0
AI[:, 0] = 0
AI[..., 0] = 0
AI[:, ...] = 0
AI[:, ..., 0] = 0
AI[AI] = 0

AI[0] = 0.0
AI[:] = 0.0
AI[0:] = 0.0
AI[:-1] = 0.0
AI[0:-1] = 0.0
AI[0, :] = 0.0
AI[:, 0] = 0.0
AI[..., 0] = 0.0
AI[:, ...] = 0.0
AI[:, ..., 0] = 0.0
AI[AI] = 0.0

AI[0] = AI
AI[:] = AI
AI[0:] = AI
AI[:-1] = AI
AI[0:-1] = AI
AI[0, :] = AI
AI[:, 0] = AI
AI[..., 0] = AI
AI[:, ...] = AI
AI[:, ..., 0] = AI
AI[AI] = AI

# __sub__
def test_sub(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self - other


SUB_INT: AIT = test_sub(AI, 0)
SUB_FLOAT: AIT = test_sub(AI, 0.0)
SUB_ARRAY: AIT = test_sub(AI, AI)

# __truediv__
def test_truediv(self: VAP, other: Union[int, float, VAP]) -> VAP:
    return self / other


TRUEDIV_INT: AIT = test_truediv(AI, 0)
TRUEDIV_FLOAT: AIT = test_truediv(AI, 0.0)
TRUEDIV_ARRAY: AIT = test_truediv(AI, AI)

# __xor__
def test_xor(self: VAP, other: Union[bool, int, VAP]) -> VAP:
    return self ^ other


XOR_BOOL = test_or(AI, False)
XOR_INT = test_or(AI, 0)
XOR_ARRAY = test_or(AI, AI)
