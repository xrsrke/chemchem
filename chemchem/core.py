# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['ureg', 'Q', 'Unit', 'DimensionalAnalysis', 'Symbol']

# %% ../nbs/00_core.ipynb 4
from dataclasses import dataclass

from fastcore.test import test_eq
import pint
import sympy as smp

# %% ../nbs/00_core.ipynb 6
@dataclass
class Unit:
    """
    Default Units
    """
    
    # SI Unit
    LENGTH = 'meter'
    MASS = 'kilogram'
    TIME = 'second'
    TEMPERATURE = 'kelvin'
    
    # Derived from SI Unit
    MOLE = 'moles'
    SPECIFIC_HEAT = 'joule / (kilogram kelvin)'
    PRESSURE = 'pascal'

# %% ../nbs/00_core.ipynb 8
ureg = pint.UnitRegistry(system='SI')
Q = ureg.Quantity # quantity

# %% ../nbs/00_core.ipynb 22
class DimensionalAnalysis:
    
    # TODO: Add
    pass

# %% ../nbs/00_core.ipynb 24
class Symbol:
    def __init__(
        self,
        symbol: str, # the symbol
        name: str # the name of the symbol
    ):
        self.name = smp.symbols(f'{symbol}_{name}', real=True)
        self.value = None
    
    @property
    def is_empty(self):
        return False if self.value else True
    
    def setValue(
        self,
        value: Q # the value of the symbol
    ):
        self.value = value
        return self
    
    # def __repr__(self):
    #     return self.name
