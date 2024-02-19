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
    
class MapCols():
    """
    Functions to map column names for test result files

    Args:
        op = OrgPathing object
    """
    def __init__(self, op: object):

        self.op = op

        self.paths = op.grab_paths()
        self.test_results = self.paths[op.tr]
        self.col_mapping = self.paths[op.cm]
        self.student_information = self.paths[op.si]
        
        self.col_map = pd.read_csv(
            self.col_mapping,
            header = 0, 
            index_col = 0
            )
        
    def parse_file_name(self, f: str) -> str:
        name = f.split('\\')[-1]
        name = re.split('-|.csv', name)[1].strip()
        return name
    
    def filter_col_map(self, name: str) -> pd.DataFrame:
        return self.col_map.filter(items = [name], axis = 0)
    
    def swap_key_vals(self, filtered_df: pd.DataFrame, name: str) -> dict:
        col_dict = filtered_df.to_dict('index')[name]
        return {v: k for k, v in col_dict.items()}
    
    def rename_cols(self, df: pd.DataFrame, swapped_kv: dict) -> pd.DataFrame:
        return df.rename(columns = swapped_kv)