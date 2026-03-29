import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Skill gained: Data loading & inspection
data = pd.read_csv("sales_data.csv", encoding="latin1")
print(data)
print(data.head())
print(data.tail())
print(data.info())


