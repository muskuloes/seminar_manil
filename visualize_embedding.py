import matplotlib.pyplot as plt
from sklearn.manifold import locally_linear_embedding
import pandas as pd
import pdb
import argparse
# needed for fancy 3d plotting
from mpl_toolkits.mplot3d import Axes3D
Axes3D

def parse_args():
    parser = argparse.ArgumentParser(description='plots')
    parser.add_argument('--input_path', type=str, default='example/umap_circles_3d.csv',
                        help='input path')
    parser.add_argument('--title', type=str, default='Embedding of Circles Dataset via LLE',
                        help='input path')
    parser.add_argument('--storage_name', type=str, default='umap_circles',
                        help='input path')
    return parser.parse_args()

def plot_embedding(args):
    output = pd.read_csv(args.input_path)
    y = output['y']
    output.drop(['y'], 1, inplace=True)
    d = output.shape[1]
    X = output.values
    # plot resulting embedding in 2d or 3d
    if d == 2:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
        legend = ax.legend(*scatter.legend_elements(), bbox_to_anchor=(1.05, 1), loc="best")
        ax.add_artist(legend)
        plt.title(f'2d {args.title}')
        plt.savefig(f'output/{args.storage_name}_2d.png', dpi=300)

    elif d == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.Spectral)
        legend = ax.legend(*scatter.legend_elements(), bbox_to_anchor=(1.05, 1), loc="best")
        ax.add_artist(legend)
        plt.title(f'3d {args.title}')
        plt.savefig(f'output/{args.storage_name}_3d.png', dpi=300)

if __name__ == "__main__":
    args = parse_args()
    plot_embedding(args=args)
