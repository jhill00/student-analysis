import os
import glob
from dotenv import load_dotenv
import yaml
from pathlib import Path
import re
import pandas as pd

class OrgPathing:
    """
    Organize file paths

    Args:
        DATA_FILES_PATH: directory of relevant files
        tr: string to filter for test results files
        cm: string to filter for column mapping file
        si: string to filter for student information file
    """

    def __init__(self,
                 DATA_FILES_PATH: str,
                 tr: str,
                 cm: str,
                 si: str
                 ):
        
        self.DATA_FILES_PATH = Path(DATA_FILES_PATH)
        self.tr = tr
        self.cm = cm
        self.si = si

        if self.DATA_FILES_PATH.exists():
            self.paths = self.DATA_FILES_PATH.glob('**\*.csv')
        else:
            raise Exception(f'Directory {self.DATA_FILES_PATH} does not exist. Please check your environment variables.')

    def grab_paths(self) -> dict:
        file_paths = {
        self.tr:[],
        self.cm:None,
        self.si:None
        }

        for f in self.paths:
            f = str(f)
            s = f.lower()
            if self.tr in s:
                file_paths[self.tr].append(f)
            if self.cm in s:
                file_paths[self.cm] = f
            if self.si in s:
                file_paths[self.si] = f
        
        return file_paths