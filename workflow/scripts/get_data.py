# workflow/scripts/get_data.py

import polars as pl
from vega_datasets import data

cars = pl.from_pandas(data.cars()).with_columns(
    pl.col("Year").dt.year()
).select(
    pl.col("*").name.map(lambda name: name.lower().replace("_", " "))
)

cars.write_csv(snakemake.output[0], separator="\t")
