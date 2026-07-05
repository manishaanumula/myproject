import pandas as pd
 GITHUB_CSV_URL="https://raw.githubusercontent.com/kothapallyharini19december-glitch/myproject/refs/heads/main/datasets/SampleSuperstore.csv"

def extract_data():
  """
  extract data from github repository.
  """
  df=pd.read_csv(GITHUB_CSV_URL)
  print("Data extracted successfully")
  print("Rows:",df.shape[0])
  print("columns:",df.shape[1])
  return df
if __name__=="__main__":
  extract_data()
