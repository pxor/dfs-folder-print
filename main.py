import os
from pathlib import Path
from algo import dfs as d
from generate import generate_folder_graph as g

root_folder = Path(__file__).parent
start = os.path.basename(root_folder)

graph = g.generate_folder_graph(root_folder)

d.dfs(graph, start)
