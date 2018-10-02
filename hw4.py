import pandas as pd

terrorism= pd.read_csv("gtd.csv")
terrorism.head().to_html("terrorism_head.html")
