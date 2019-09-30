# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
customer = pd.read_csv("CUSTOMER.CSV") 
# Preview the first 5 lines of the loaded data 
customer_sample = pd.read_csv("CUSTOMER_SAMPLE.CSV")

c = customer[customer["CUSTOMER_CODE"].isin(customer_sample["CUSTOMER_CODE"])]
c.to_csv("customer_out.csv", index = None)

invoice = pd.read_csv("INVOICE.CSV") 
c = invoice[invoice["CUSTOMER_CODE"].isin(customer_sample["CUSTOMER_CODE"])]
c.to_csv("invoice_out.csv", index = None)

invoice_item = pd.read_csv("INVOICE_ITEM.CSV")
d = invoice_item[invoice_item["INVOICE_CODE"].isin(c["INVOICE_CODE"])]
d.to_csv("invoice_item_out.csv", index = None)