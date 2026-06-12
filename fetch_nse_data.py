import subprocess
import sys

subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "nsepython"]
)

from nsepython import *

print(nse_get_index_quote("NIFTY 50"))