import os


# Generate folder graph from root folder excluding 'venv' folder and hidden folders starting with '.'
def generate_folder_graph(root_folder):
    graph = {}

    for dirpath, dirnames, filenames in os.walk(root_folder):
        current_folder = os.path.basename(dirpath)
        adjacent_items = [file_tree for file_tree in dirnames + filenames if file_tree != "venv" and not file_tree.startswith(".")]

        graph[current_folder] = adjacent_items

    return graph