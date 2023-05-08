import re

_SECOND_MULT = 1
_MINUTE_MULT = _SECOND_MULT * 60
_HOUR_MULT = _MINUTE_MULT * 60
_DAY_MULT = _HOUR_MULT * 24

_MULTS = [
    _DAY_MULT,
    _HOUR_MULT,
    _MINUTE_MULT,
    _SECOND_MULT
]

_PATTERN = re.compile(r"(?:(\d+)[dD])?(?:(\d+)[hH])?(?:(\d+)[mM])?(?:(\d+)[sS])?")



class parser:
    """
    Converts a string in the form of [n]D[n]H[n]M[n]S to an integer representing seconds.
    D, H, M, and S may be capital or lowercase. Only one of the four is required. Values
    must be non-negative integers.

    Examples:
    1D -> 86400
    5H -> 18000
    34M -> 2040
    5S -> 5
    2h100m6s -> 13206
    """
    @staticmethod
    def parse(dur_str: str) -> int:
        if not (match := _PATTERN.match(dur_str)):
            raise ValueError("dur_str did not match expected format.")
        value_present = False
        value = 0
        for (mult, val) in zip(_MULTS, match.groups()):
            if not val:
                continue
            value_present = True
            value += mult * int(val)
        if not value_present:
            raise ValueError("dur_str did not specify a value.")
        return value

parse = parser().parse