Data

The data in data/mr/ yelp reviews.
The current data/word2vec directory is empty. To use the pretrained word2vec embeddings, download the Google News pretrained vector data with following command "wget https://s3.amazonaws.com/mordecai-geo/GoogleNews-vectors-negative300.bin.gz" and unzip it to the directory. It will be a .bin file.

Usage

1. Preprocess the data

	python text_input.py

2. Train

	python train.py

