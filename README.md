Description:

Binary tweet classification using tweet encodings.

Instructions:

Download http://nlp.stanford.edu/data/wordvecs/glove.twitter.27B.zip and move the file glove.twitter.27B.100d.txt to src directory.

Train file format: data.train,data.test

Test file format: labels.test,labels.train

All the above files should be kept in src directory.

It already contains sample training and test data. 

Run "sh run.sh" to train and test on the given data. 

It generates file "labels.generated" which is the predicted labels for test dataset. 

Run FSCORE.py with three arguments:
1. Generated labels 2. True labels 3. Test dataset filename. 

It calculates precision, recall and fscore.
