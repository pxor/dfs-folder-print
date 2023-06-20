import os
from pathlib import Path
from algo import dfs as d
from generate import generate_folder_graph as g

root_folder = Path(__file__).parent
graph = g.generate_folder_graph(root_folder)

start = os.path.basename(root_folder)
visited_set = set()
path_list = []

d.dfs(graph, start, visited_set, 0, path_list)
