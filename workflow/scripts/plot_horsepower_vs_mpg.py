import altair as alt
import polars as pl
alt.data_transformers.enable("vegafusion")

data = pl.read_csv(snakemake.input[0], separator="\t")

chart = alt.Chart(data).mark_point(tooltip=True).encode(
    alt.X("miles per gallon"),
    alt.Y("horsepower"),
    alt.Color("origin").scale(scheme="accent"),
).interactive()

chart.save(snakemake.output[0])
