import pytest
from durationutil import parser


class TestDurationutil():
    
    def test_noValueSpecified(self):
        with pytest.raises(ValueError):
            parser.parse("")

    def test_onlyDaysSpecified(self):
        res = parser.parse("2d")
        assert res == 172800

    def test_onlyHoursSpecified(self):
        res = parser.parse("3h")
        assert res == 10800

    def test_onlyMinutesSpecified(self):
        res = parser.parse("9m")
        assert res == 540

    def test_onlySecondsSpecified(self):
        res = parser.parse("13s")
        assert res == 13

    def test_upperCase(self):
        res = parser.parse("1D1H1M1S")
        assert res == 90061

    def test_lowerCase(self):
        res = parser.parse("1d1h1m1s")
        assert res == 90061

    def test_exceedingNaturalLimits(self):
        # we can have >23 hours, >59 minutes, >59 seconds
        res = parser.parse("1d30h90m100s")
        assert res == 199900

    def test_zero(self):
        res = parser.parse("0d0h0m0s")
        assert res == 0