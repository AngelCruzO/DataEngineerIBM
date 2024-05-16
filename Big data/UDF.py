from pyspark.sql.functions import udf
import time

@udf("string")
def engine(cylinders):
    time.sleep(0.2)  # Intentionally delay task
    eng = {4: "inline-four", 6: "V6", 8: "V8"}
    return eng.get(cylinders, "other")

df = df.withColumn("engine", engine("cylinders"))

dfg = df.groupby("cylinders")

dfa = dfg.agg({"mpg": "avg", "engine": "first"})

dfa.show()