import pandas as pd
from ydata_profiling import ProfileReport
from dataprep.eda import create_report
from dataprep.datasets import load_dataset, get_dataset_names
df = pd.read_csv('../data/products.csv')
df.describe()
profile = ProfileReport(df, title="Profiling Report")
"""report = create_report(df)
report.show_browser()"""
profile.to_widgets()
