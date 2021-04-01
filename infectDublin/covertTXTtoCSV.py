import pandas as pd

read_file = pd.read_csv(r'/home/mimbele/PycharmProjects/pythonProject/infectDublin_edges.txt')
read_file.to_csv(r'/home/mimbele/PycharmProjects/pythonProject/infectDublin_edges_CSV.csv', index=None)
