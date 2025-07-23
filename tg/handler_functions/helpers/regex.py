"""
Regex utilities for extracting structured data from trading signal text.
"""

import re
from abc import ABC, abstractmethod
from typing import List, Optional, Any


class SignalExtractor(ABC):
    """
    Abstract base class for extracting data from signal text.
    """

    @abstractmethod
    def extract(self, signal_text: str) -> Any:
        pass


class NumberedListExtractor(SignalExtractor):
    """
    Extracts a list of numbers from a section of text matching a regex pattern.
    """

    def __init__(self, section_pattern: str):
        self.section_pattern = section_pattern

    def extract(self, signal_text: str) -> Optional[List[str]]:
        match = re.search(self.section_pattern, signal_text)
        if not match:
            return None
        numbered_list = re.findall(r"\d\)\s*\d+.?\d*", match.group())
        result = []
        for item in numbered_list:
            number_match = re.search(r"\)\s*\d+.?\d*", item)
            if number_match:
                result.append(number_match.group().replace(")", "").replace(" ", ""))
        return result if result else None


class SymbolExtractor(SignalExtractor):
    """
    Extracts the trading symbol from the signal text.
    """

    SYMBOL_PATTERN = r"#\w+\/\w+"

    def extract(self, signal_text: str) -> Optional[str]:
        match = re.search(self.SYMBOL_PATTERN, signal_text)
        if match:
            return (
                match.group().replace("#", "").replace("/", "").upper() + " Perpetual"
            )
        return None


class SignalTypeExtractor(SignalExtractor):
    """
    Extracts the signal type from the signal text.
    """

    TYPE_PATTERN = r"signal\stype:\s*\w*\s*\(\w+\)"

    def extract(self, signal_text: str) -> Optional[str]:
        match = re.search(self.TYPE_PATTERN, signal_text)
        if match:
            type_match = re.search(r"\(\w+\)", match.group())
            if type_match:
                return type_match.group().replace("(", "").replace(")", "")
        return None


class LeverageExtractor(SignalExtractor):
    """
    Extracts the leverage value from the signal text.
    """

    LEVERAGE_PATTERN = r"leverage:\s*\w*\s*\(\d*\.?\d*"

    def extract(self, signal_text: str) -> Optional[str]:
        match = re.search(self.LEVERAGE_PATTERN, signal_text)
        if match:
            lev_match = re.search(r"\(\d*\.?", match.group())
            if lev_match:
                return lev_match.group().replace(".", "").replace("(", "")
        return None


# Facade functions for external use, for backward compatibility and simplicity
def symbol(signal_text: str) -> Optional[str]:
    """Extracts the trading symbol from the signal text."""
    return SymbolExtractor().extract(signal_text)


def signal_type(signal_text: str) -> Optional[str]:
    """Extracts the signal type from the signal text."""
    return SignalTypeExtractor().extract(signal_text)


def leverage(signal_text: str) -> Optional[str]:
    """Extracts the leverage value from the signal text."""
    return LeverageExtractor().extract(signal_text)


# Concrete extractors for entry, targets, and stop sections
def EntryExtractor() -> NumberedListExtractor:
    """Factory for entry targets extractor."""
    return NumberedListExtractor(r"entry\stargets:\n(\d*\s*\)\s\d+.*\d*\n)*\n*take")


def TargetsExtractor() -> NumberedListExtractor:
    """Factory for take-profit targets extractor."""
    return NumberedListExtractor(
        r"take-profit\stargets:\n(\d*\s*\)\s*\d+.*\d*\n)*\n*stop"
    )


def StopExtractor() -> NumberedListExtractor:
    """Factory for stop targets extractor."""
    return NumberedListExtractor(r"stop\stargets:\n(\d*\s*\)\s*\d+.*\d*\n)*\n*")


def entry(signal_text: str) -> Optional[List[str]]:
    """Extracts entry targets as a list from the signal text."""
    return EntryExtractor().extract(signal_text)


def targets(signal_text: str) -> Optional[List[str]]:
    """Extracts take-profit targets as a list from the signal text."""
    return TargetsExtractor().extract(signal_text)


def stop(signal_text: str) -> Optional[List[str]]:
    """Extracts stop targets as a list from the signal text."""
    return StopExtractor().extract(signal_text)
