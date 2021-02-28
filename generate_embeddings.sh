#!/usr/bin/bash
set -x

python umap_fit.py --input_path='swiss_roll_data/rawdata_swiss_roll.csv' --output_path='output/umap_swiss_roll.csv' --d=2
python umap_fit.py --input_path='circle_data/rawdata_circle.csv' --output_path='output/umap_circle.csv' --d=2
python umap_fit.py --input_path='circle_data/rawdata_circle.csv' --output_path='output/umap_circle.csv' --d=3
python umap_fit.py --input_path='world_data/rawdata_world_2d.csv' --output_path='output/umap_world.csv' --d=2
python umap_fit.py --input_path='world_data/rawdata_world_3d.csv' --output_path='output/umap_world.csv' --d=2

python visualize_embedding.py --input_path='output/umap_world_2d.csv' --title='Embedding of World Dataset via UMAP' --storage_name='umap_world'
python visualize_embedding.py --input_path='output/umap_world_3d.csv' --title='Embedding of World Dataset via UMAP' --storage_name='umap_world'
python visualize_embedding.py --input_path='output/umap_swiss_roll_2d.csv' --title='Embedding of Swiss roll Dataset via UMAP' --storage_name='umap_swiss_roll'
python visualize_embedding.py --input_path='output/umap_circle_2d.csv' --title='Embedding of Circle Dataset via UMAP' --storage_name='umap_circle'
python visualize_embedding.py --input_path='output/umap_circle_3d.csv' --title='Embedding of Circle Dataset via UMAP' --storage_name='umap_circle'

echo "Finished!"
