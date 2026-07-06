"""
Base Judge Interface

All judge models must inherit from this class.
"""

from abc import ABC, abstractmethod


class BaseJudge(ABC):
    """
    Abstract base class for all judge models.
    """

    @abstractmethod
    def evaluate(self, question, answer_a, answer_b):
        """
        Compare two responses.

        Parameters
        ----------
        question : str | list
        answer_a : str
        answer_b : str

        Returns
        -------
        dict
        """
        pass