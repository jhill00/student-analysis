import pandas as pd
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    DATA_FILE = os.environ.get('DATA_FILE')
    TWO_PATH = os.environ.get('TWO_PATH')
    write_to = '\\'.join([TWO_PATH, 'filtered_df.csv'])

    # filter data set
    df = pd.read_csv(DATA_FILE)
    grade_1_df = df.query("grade == 'Grade 1'")
    
    grade_1_df.to_csv(write_to,
                      mode = 'w',
                      index = False,
                      header = True)