import json
from typing import Sequence, List

from llama_index.llms import OpenAI, ChatMessage
from llama_index.tools import BaseTool, FunctionTool
from lightning import Data, Channel

import nest_asyncio

nest_asyncio.apply()

def data (a:int , b: int) -> int:
    "multiple push data around liquidity"

def inbound (a: int , b: int) -> int:
    "multiple data about inbound liquidity"

def outbound
(a: int , b: int) -> int:
    "multiple data about outbound liquidity"


def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

def data (a:int, b:int ) -> int:
    "multiple push data around APIs"

def api (a:int , b:int ) -> int
    "multiple push apis"

def ligjtningnode (a: int , b:int ) -> int
"multiple push lightning nodes"
