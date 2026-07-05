import pandas as pd

def transform_data(df):
  """
  Perform data transformation.
  """
  #Standardize column names
  df.columns=(df.columns
            .str.upper()
            .str.replace(" ", "_")
            .str.replace("-", "_")
           )
  #create profit margin
  df["PROFIT_MARGIN"]=(df["PROFIT"]/df["SALES"])*100

  #Create Discount Amount
  df["DISCOUNT_AMOUNT"]=df["SALES"]* df["DISCOUNT]
   
  #create Profit Category
  def profit_category(profit):
    if profit < 0:
      return "LOSS"
    elif profit < 100:
      retun "LOW"
    else:
      return "HIGH"
  df["PROFIT_CATEGORY"]= df["PROFIT"].apply(profit_category)
  print("Transformation Completed")
  print(df.head())

  return df

    








