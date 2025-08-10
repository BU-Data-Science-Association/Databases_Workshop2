import pandas as pd
from sqlalchemy import create_engine

subject = pd.read_csv("/workspace/data/subject.csv")
work = pd.read_csv("/workspace/data/work.csv")

engine = create_engine("postgresql://app_user:app_password@localhost:5432/app")  # adjust accordingly
subject.to_sql("subject", engine, if_exists="replace", index=False)
work.to_sql("work", engine, if_exists="replace", index=False)
print("Data should be loaded into Postgres")