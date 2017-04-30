Data

The data in data/mr/ yelp reviews.
The current data/word2vec directory is empty. Need to download the Google News pretrained vector data using following command "wget https://s3.amazonaws.com/mordecai-geo/GoogleNews-vectors-negative300.bin.gz" and unzip it into the directory. It will be a .bin file.

Usage

1. Preprocess the data

	python text_input.py

2. Train

	python train.py

Python packages Required
	1. simplejson
	2. tensorflow
	3. pandas
	4. cPickle
	5. numpy
	6. collections
