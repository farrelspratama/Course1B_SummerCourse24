import pandas as pd
import numpy as np
import statistics

ListCovid = pd.Series ([174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,
                        1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342])

df = pd.DataFrame ({'List':ListCovid})
range_value = max(ListCovid) - min(ListCovid)
median = statistics.median(ListCovid)
variance = statistics.variance(ListCovid)

print(f"Range of infection rates: {range_value}")
print(f"Median infection rate: {median}")
print(f"Variance of infection rates: {variance:.2f}")
df.describe()