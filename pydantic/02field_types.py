from pydantic import BaseModel
from typing import Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union, Any, Iterable, Callable, Pattern
from enum import Enum
from decimal import Decimal
from pathlib import Path
from uuid import UUID
import datetime
import ipaddress


class Mymodel(BaseModel):
    none_val: None
    bool_val: bool
    int_val: int
    float_val: float
    str_val: str
    bytes_val: bytes
    list_val: List
    tuple_val: Tuple
    dict_val: Dict
    set_val: Set
    frozenset_val: FrozenSet
    deque_val: Deque
    any_val: Any
    date_val: datetime.date
    time_val: datetime.time
    datetime_val: datetime.datetime
    timedelta_val: datetime.timedelta
    union_val: Union[int, None] = None # 可以是整数或者None，默认值为None
    optional_val: Optional[int] # Union[int, None]的另一种写法
    iteralbe_val: Iterable
    callable_val: Callable
    pattern_val: Pattern
    ipv4_address_val: ipaddress.IPv4Address
    ipv4_interface_val: ipaddress.IPv4Interface
    ipv4_network_val: ipaddress.IPv4Network
    ipv6_address_val: ipaddress.IPv6Address
    ipv6_interface_val: ipaddress.IPv6Interface
    ipv6_network_val: ipaddress.IPv6Network
    enum_val: Enum
    decimal_val: Decimal
    path_val: Path
    uuid_val: UUID
