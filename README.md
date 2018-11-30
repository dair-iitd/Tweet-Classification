Description:

Binary tweet classification using tweet encodings.

Instructions:

Install python requirements using command pip install -r libraries.txt

Download http://nlp.stanford.edu/data/wordvecs/glove.twitter.27B.zip and move the file glove.twitter.27B.100d.txt to src directory.

Train dataset filename: data.train,labels.train
Test dataset filename: data.test,labels.test

All the above files should be kept in src directory.

It already contains sample training and test data. 

Run "sh run.sh" to train and test on the given data. 

It generates file "labels.predicted" which is the predicted labels for test dataset. 

Run FSCORE.py with three arguments:
1. Generated labels 2. True test labels 3. Test dataset filename. 

It calculates precision, recall and fscore.
