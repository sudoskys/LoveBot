# -*- coding: utf-8 -*-
# @Time    : 9/22/22 10:07 PM
# @FileName: main.py
# @Software: PyCharm
# @Github    ：sudoskys
from pathlib import Path
from utils.DataParse import ReadConfig
config = ReadConfig().parseFile(str(Path.cwd()) + "/Config/app.toml")
print(config)