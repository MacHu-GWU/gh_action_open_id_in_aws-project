# -*- coding: utf-8 -*-

import os
import subprocess
from pathlib import Path

dir_here = Path(__file__).absolute().parent

os.chdir(str(dir_here))
args = [
    "cdk",
    "synth",
    "--path-metadata",
    "false",
    "--version-reporting",
    "false",
]
subprocess.run(args)
