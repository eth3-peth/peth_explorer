#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ.setdefault("COINGECKO_PRICE_USD", "1")
    os.environ.setdefault("COINGECKO_PRICE_BTC", "1")
    os.environ.setdefault("COINGECKO_MKT_USD", "1")
    os.environ.setdefault("MIN_PEER_VERSION", "3.2.0")
    os.environ.setdefault("BRS_P2P_VERSION", "1")
    os.environ.setdefault("COIN_SYMBOL", "PETH")
    # os.environ.setdefault("SIGNUM_NODE", "127.0.0.1")
    os.environ.setdefault("ADDRESS_PREFIX", "TS-")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
