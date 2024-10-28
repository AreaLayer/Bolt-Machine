import json
import requests
import ldk

def get_balance(address):
    """
    Retrieves the balance of a Bitcoin address.
    Args:
        address (str): The Bitcoin address.

    Returns:
        float: The balance of the address.
    """