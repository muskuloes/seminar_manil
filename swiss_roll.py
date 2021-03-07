import pdb
import pandas as pd
import numpy as np
import argparse
import os
from sklearn.datasets import make_swiss_roll
from matplotlib import pyplot as plt
# needed for fancy 3d plotting
from mpl_toolkits.mplot3d import Axes3D
Axes3D

def parse_args():
    parser = argparse.ArgumentParser(description='Circle plots')
    parser.add_argument('--n', type=int, default=1000,
                        help='max amount of plots to make')
    parser.add_argument('--noise', type=int, default=0.0,
                        help='delta for the clock hands distance, the larger the greater the stripe')
    return parser.parse_args()

def generate_swiss_roll_data(args):
    # generate folder for storage
    if not os.path.exists('swiss_roll_data'):
        os.mkdir('swiss_roll_data')

    # draw swiss roll samples with y, the main latent dimension
    X, y = make_swiss_roll(n_samples=args.n, noise=args.noise, random_state=1337)

    swiss_roll_data = pd.DataFrame({'x_1': X[:, 0],
                                    'x_2': X[:, 1],
                                    'x_3': X[:, 2],
                                    'y': y})
    swiss_roll_data.to_csv(f'swiss_roll_data/rawdata_swiss_roll_{args.n}.csv', index=False)

    # plot it
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # use 'label' y for coloring
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.Spectral)
    ax.set_title(f'The Swiss Roll Dataset with {args.n} samples')
    plt.savefig('swiss_roll_data/swiss_roll.png')

if __name__ == "__main__":
    args = parse_args()
    generate_swiss_roll_data(args=args)
