# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
pokemon_PgSQL_Train = dataiku.Dataset("Pokemon_PgSQL_Train")
pokemon_PgSQL_Train_df = pokemon_PgSQL_Train.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pokemon_PgSQL_Train_df.shape

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pokemon_PgSQL_Train_df.head(5)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pokemon_PgSQL_Train_df.tail(5)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Legendary_pokemon_speed = pokemon_PgSQL_Train_df.pivot_table(
    index=["Type 1", 'Type 2'],
    columns=["Name"],
    values=["Speed"],
    aggfunc='max',   # aggregation function
    margins=True     # add subtotals on rows and cols
)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Legendary_pokemon_speed

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pokemon_PgSQL_Python = dataiku.Dataset("Pokemon_PgSQL_Python")
pokemon_PgSQL_Python.write_with_schema(Legendary_pokemon_speed)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Legendary_pokemon_HP = pokemon_PgSQL_Train_df.pivot_table(
    index=["Name"],
    columns=["Legendary"],
    values=["HP"],
    aggfunc='max',   # aggregation function
    margins=True     # add subtotals on rows and cols
)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Legendary_pokemon_HP