import queue
import networkx as nx
import matplotlib.pyplot as plt
import time
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
G = nx.Graph()
entry = ttk.Entry(root, font=('Arial', 12))
start_node = ttk.Entry(root, font=('Arial', 12))
goal_node = ttk.Entry(root, font=('Arial', 12))
ctr_speed_input = ttk.Entry(root, font=('Arial', 12))

# Set a custom style for ttk buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

def bfs(graph, search_node, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            
            if vertex == search_node:
                break

            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order

def dfs(graph, start_node, search_node, visited = None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        
        if start_node == search_node:
            return order

        for node in graph[start_node]:
            if node not in visited:
                order.extend(dfs(graph, node, search_node, visited))

                if search_node in order:
                    return order
    
    return order

def hill_climbing(graph, start_node, search_node, heuristics):
    return 0

def branch_and_bound(graph, start_node, search_node):
    return 0

def beam(graph, start_node, search_node):
    return 0

def A_star(graph, start_node, search_node):
    return 0

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start = 1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels = True, node_color = ['r' if n in order[:i] else 'skyblue' for n in G.nodes], font_weight = 'bold', node_size = 700)
        plt.draw()
        plt.pause(float(ctr_speed_input.get()))

    plt.show()
    time.sleep(.5)

def add_vertex_function():
    user_input = entry.get()
    if entry.get() == "":
        print("Empty Input")
    else: 
        print("Vertex Added!", user_input) 
        G.add_node(user_input)
        entry.delete(0, tk.END)
        draw_graph()

def add_edges_function():
    entry.get()
    if entry.get() == "":
        print("Empty Input")
    else:
        first, second = entry.get().split(',')
        G.add_edge(first, second)
        print(f"Edge added!{first, second}")
        entry.delete(0, tk.END)
        draw_graph()

def add_weight_function():
    user_input = entry.get()

    if user_input == "":
        print("Empty Input!")
    else:
        try:
            node1, node2, weight = map(str.strip, user_input.split(','))
            G.add_edge(node1, node2, weight=int(weight))
            print(f"Weighted Edge added! {node1} - {node2} with weight {weight}")
            entry.delete(0, tk.END)
            draw_graph()
        except ValueError:
            print("Invalid input format. Please use 'node1,node2,weight' format.")

def add_heuristic_function(G, goal_node):
    for node in G.nodes:
        G.nodes[node]['heuristic'] = random.randint(1, 50)  # Replace this with your heuristic function

def run_bfs_function():
    _label = tk.Label(root, text="_______________________________________________________________________________________________", font=('Arial', 10, 'bold'))
    _label.pack(pady=10)
    welcome_label = tk.Label(root, text="BFS Algorithm", font=('Arial', 10, 'bold'))
    welcome_label.pack(pady=10)
    start_node_label = tk.Label(root, text="Enter Goal Node: ")
    start_node_label.pack()
    goal_node.pack()
    goal_node_label = tk.Label(root, text="Enter Starting Node: ")
    goal_node_label.pack()
    start_node.pack()
    visualize_button = tk.Button(root, text="Visualize Searching", font = ("Arial", 8), command = bfs_visualize_search_button_function)
    ctr_speed_label = tk.Label(root, text="Traversal Speed: (The lower the number = Faster)")
    ctr_speed_label.pack()
    ctr_speed_input.pack()
    visualize_button.pack()

def run_dfs_function():
    _label = tk.Label(root, text="_______________________________________________________________________________________________", font=('Arial', 10, 'bold'))
    _label.pack(pady=10)
    welcome_label = tk.Label(root, text="DFS Algorithm", font=('Arial', 10, 'bold'))
    welcome_label.pack(pady=10)
    start_node_label = tk.Label(root, text="Enter Goal Node: ")
    start_node_label.pack()
    goal_node.pack()
    goal_node_label = tk.Label(root, text="Enter Starting Node: ")
    goal_node_label.pack()
    start_node.pack()
    visualize_button = tk.Button(root, text="Visualize Searching", font = ("Arial", 8), command = dfs_visualize_search_button_function)
    ctr_speed_label = tk.Label(root, text="Traversal Speed: (The lower the number = Faster)")
    ctr_speed_label.pack()
    ctr_speed_input.pack()
    visualize_button.pack(pady=10)

def run_hillclimbing_function():
    # goal_node_label = tk.Label(root, text="Enter Goal Node: ")
    # goal_node_label.pack()
    # goal_node.pack()

    # start_node_label = tk.Label(root, text="Enter Starting Node: ")
    # start_node_label.pack()
    # start_node.pack()

    # generate_heuristics = tk.Button(root, text="Generate Heuristic Values", font = ("Arial", 8), command = add_heuristic_function(G, goal_node.get()))

    # visualize_button = tk.Button(root, text="Visualize Searching", font = ("Arial", 8), command = bfs_visualize_search_button_function)
    # ctr_speed_label = tk.Label(root, text="Traversal Speed: ")
    # ctr_speed_label.pack()
    # ctr_speed_input.pack()
    # generate_heuristics.pack(pady=10)
    # visualize_button.pack()
    return 0


def run_branchbound_function():
    return 0

def run_beam_function():
    return 0

def run_Astar_function():
    return 0

def draw_graph():
    plt.clf()
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights as labels
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Add edge labels
    plt.show()
    plt.pause(0.1)

def bfs_visualize_search_button_function():
    if start_node.get() == "" and goal_node.get() == "":
        print("Please input the start and goal node.")
    else:
        visualize_search(bfs(G, goal_node.get(), start_node.get()), "BFS Visualizer", G, nx.spring_layout(G))
        path = bfs(G, goal_node.get(), start_node.get())
        path_label = tk.Label(root, text= f"Traversed Path: {path}", font=("Arial", 18, 'bold'))
        path_label.pack()

def dfs_visualize_search_button_function():
    if start_node.get() == "" and goal_node.get() == "":
        print("Please input the start and goal node.")
    else:
        visualize_search(dfs(G, start_node.get(), goal_node.get()), "DFS Visualizer", G, nx.spring_layout(G))
        path = dfs(G, start_node.get(), goal_node.get())
        path_label = tk.Label(root, text= f"Traversed Path: {path}", font=("Arial", 18, 'bold'))
        path_label.pack()

def create_predefined_graph():
    weighted_edges = [
        ('A', 'B', random.randint(1, 50)), ('A', 'C', random.randint(1, 50)), ('A', 'D', random.randint(1, 10)),
        ('B', 'C', random.randint(1, 50)), ('B', 'E', random.randint(1, 50)),
        ('C', 'D', random.randint(1, 50)), ('C', 'F', random.randint(1, 50)),
        ('D', 'E', random.randint(1, 50)), ('D', 'G', random.randint(1, 50)),
        ('E', 'F', random.randint(1, 50)), ('E', 'H', random.randint(1, 50)),
        ('F', 'G', random.randint(1, 50)), ('F', 'I', random.randint(1, 50)),
        ('G', 'H', random.randint(1, 50)), ('G', 'J', random.randint(1, 50)),
        ('H', 'I', random.randint(1, 50)),
        ('I', 'J', random.randint(1, 50))
    ]
    G.add_weighted_edges_from(weighted_edges)
    draw_graph()

class SearchVisualizer:
    def __init__(self):
        root.geometry("768x768")
        root.title("Search Visualizer")

        label = ttk.Label(root, text="SEARCHING ALGORITHMS VISUALIZATION", font=("Arial", 18, 'bold'))
        label.pack(pady=10)

        create_graph_label = ttk.Label(root, text="Create Graph", font=("Arial", 14))
        create_graph_label.pack(pady=5)

        entry.pack(pady=5)

        add_vertex_button = ttk.Button(root, text="Add Vertex", command=add_vertex_function)
        add_vertex_button.pack(pady=5)

        add_edges_button = ttk.Button(root, text="Add Edges", command=add_edges_function)
        add_edges_button.pack(pady=5)

        add_weights_button = ttk.Button(root, text="Add Weights", command = add_weight_function)
        add_weights_button.pack(pady=10)

        predefined_graph = ttk.Button(root, text="Create Sample Graph", command=create_predefined_graph)
        predefined_graph.pack(pady=10)

        searching_label = ttk.Label(root, text="Choose Search Algorithm:", font=('Arial', 14))
        searching_label.pack(pady=10)

        run_bfs_button = ttk.Button(root, text="Run BFS", command=run_bfs_function)
        run_bfs_button.pack(pady=5)

        run_dfs_button = ttk.Button(root, text="Run DFS", command=run_dfs_function)
        run_dfs_button.pack(pady=5)

        # run_hillclimbing_btn = ttk.Button(root, text="Run Hill Climbing", command=run_hillclimbing_function)
        # run_hillclimbing_btn.pack(pady=5)

        # run_branchbound_btn = ttk.Button(root, text="Run Branch and Bound", command=run_branchbound_function)
        # run_branchbound_btn.pack(pady=5)

        # run_beam_btn = ttk.Button(root, text="Run Beam", command=run_beam_function)
        # run_beam_btn.pack(pady=5)

        # run_Astar_btn = ttk.Button(root, text="Run A*", command=run_Astar_function)
        # run_Astar_btn.pack(pady=5)
        root.mainloop()

if __name__ == '__main__':
    SearchVisualizer()