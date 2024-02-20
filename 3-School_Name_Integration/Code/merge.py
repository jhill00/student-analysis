import pandas as pd
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    STEP_TWO_FILE = os.environ.get('STEP_TWO_FILE')
    STUDENT_INFO = os.environ.get('STUDENT_INFO')
    THREE_PATH = os.environ.get('THREE_PATH')
    write_to = '\\'.join([THREE_PATH, 'merged_school_name.csv'])

    # filter data set
    df = pd.read_csv(STEP_TWO_FILE)
    si = pd.read_csv(STUDENT_INFO)
    
    rename_dict = {'sis_id':'student_id'}
    si = si.rename(columns = rename_dict)
    si = si[['student_id', 'school_name']]

    merged_df = pd.merge(df,
                         si,
                         on = 'student_id',
                         how = 'left')
    
    merged_df.to_csv(write_to,
                      mode = 'w',
                      index = False,
                      header = True)