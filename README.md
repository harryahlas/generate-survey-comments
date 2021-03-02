# generate-survey-comments

Generate artificial survey comments based on real data.

Steps

1.  Collected sample data from multiple publicly available sources, including data.world. Shoot me a note if you would like the training data set, \~4k comments.

2.  Combine and clean data (*compile_data.R*). Save as *data/training_comments.csv*

3.  Save a copy of *training_comments.csv* to Google Drive. Location: '/content/gdrive/MyDrive/Development/seq2seqcomments/training_comments.csv'

4.  Train model on Google Colab using *seq2seqcomments.ipynb*.

5.  Generate comments **TBD**
