# generate-survey-comments

Generate artificial survey comments based on real data.

Steps

1.  Collected sample data from multiple publicly available sources, including data.world. Shoot me a note if you would like the training data set, \~4k comments.

2.  Combine and clean data (*compile_data.R*). Save as *data/training_comments.csv*

3.  Save a copy of *training_comments.csv* to Google Drive. Location: '/content/gdrive/MyDrive/Development/seq2seqcomments/training_comments.csv'

4.  Train model on Google Colab using [seq2seqcomments.ipynb](https://github.com/harryahlas/generate-survey-comments/blob/master/seq2seqcomments.ipynb). Results were subpar.

5.  Trained model on Google Colab using [Interactive_textgenrnn_Comment_Generator_w_GPU.ipynb](https://github.com/harryahlas/generate-survey-comments/blob/master/Interactive_textgenrnn_Comment_Generator_w_GPU.ipynb), by [Max Woolf](https://minimaxir.com/). Results were much better but still not entirely coherent. Trying again with 40 epochs.

5.  Generate comments **TBD**

### Standalone script

[comments-not-on-github.py](https://github.com/harryahlas/generate-survey-comments/blob/master/comments-not-on-github.py) is a standalone Python script proof of concept using a small sample data set. Note that instead of `model.predict_classes()` the code below should be used when making predictions, per a Keras change in 2021.

`predicted = np.argmax(model.predict(token_list), axis=-1)`

   
