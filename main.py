import dowhy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygraphviz as pgv
import networkx as nx


import logging.config
DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'INFO',
        },
    }
}

logging.config.dictConfig(DEFAULT_LOGGING)
# Disabling warnings output
import warnings
from sklearn.exceptions import DataConversionWarning, ConvergenceWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
warnings.filterwarnings(action='ignore', category=UserWarning)

df = pd.read_csv('loans_causal_schema.csv')
file = open("causal_graph.dot")
causal_graph = file.read().replace("\n", " ")
file.close()
model= dowhy.CausalModel(
        data = df,
        graph=causal_graph,
        treatment='emp_length',
        outcome='is_bad_loan')

model_view = model.view_model(layout='dot')

#agraph = nx.drawing.nx_agraph.to_agraph(model._graph._graph)
#agraph.draw("lending_club_graph.png", format="png", prog='dot')
