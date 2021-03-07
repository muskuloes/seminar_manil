import os
import umap
import numpy as np
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="world")
    parser.add_argument(
        "--input_path",
        type=str,
        default="swiss_roll_data/rawdata_swiss_roll.csv",
        help="path to the input data",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="output/umap_swiss_roll.csv",
        help="path to the input data",
    )
    parser.add_argument(
        "--d", type=int, default=2, help="dimensionality of the final embedding"
    )
    return parser.parse_args()


def fit_embedding(args):
    data = pd.read_csv(args.input_path)
    print(f"data shape: {data.shape}")
    y = data["y"]

    data.drop(["y"], axis=1, inplace=True)
    reducer = umap.UMAP(n_neighbors=30, min_dist=0.3, n_components=args.d)
    reducer.fit(data)
    embedding = reducer.transform(data)

    print(f"embedding shape: {embedding.shape}")
    output = pd.DataFrame(embedding)

    output.columns = [f"x_{idx}" for idx in range(embedding.shape[1])]

    output["y"] = y

    output_name = args.output_path.split(".csv")[0]

    output.to_csv(f"{output_name}_{args.d}d.csv", index=False)
    print(f"saved to file: {output_name}_{args.d}d.csv")


if __name__ == "__main__":
    args = parse_args()
    if not os.path.exists("output"):
        os.mkdir("output")
    fit_embedding(args)
