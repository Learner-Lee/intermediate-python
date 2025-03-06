__version__ = "1.0.0"
__author__ = "ALen"

from .moduleA import x,y
from . import moduleA

__all__ = ['x','y','moduleA']

print("this __init__")