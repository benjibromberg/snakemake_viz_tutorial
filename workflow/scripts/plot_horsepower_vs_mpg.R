library(readr)
library(ggplot2)

cars <- read_tsv(snakemake@input[[1]], show_col_types = FALSE)
svg(snakemake@output[[1]])
ggplot(cars, aes(`miles per gallon`, horsepower)) +
  geom_point() +
  theme_classic(16)
dev.off()
