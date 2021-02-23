# Text-Classification Examples

Text classification task of NLP is the process of categorizing text into pre-defined categories. There are lots of use-cases for this task like:

* Spam e-mail filtering
* Fake news detection
* Sentiment analysis
* News topic categorization etc.

Beyond use-cases, several approaches have been proposed for this task so far. In this task, firstly textual data are converted to numerical values so that ML algorithms can process.
This representations can be extracted via:

* Bag-of-Words approaches (e.g. TF-IDF)
* Pre-trained word embeddings - noncontextual representations (e.g. Word2Vec, GloVe, FastText etc.)
* Pre-trained language models - contextual representations (e.g. BERT, ELECTRA, GPT-3 :smile:, XLNET, RoBERTa etc.)

Secondly, by adding extra classifier layers on top of these representations, texts can be categorized into related categories.

In this repo, you can find some example codes with related datasets for text classification.

## [News Topic Classification](https://github.com/ozcangundes/Text-Classification/tree/master/News%20Topic%20Classification)

| Embedding Approach        | Dataset           | # of Classes |
| ------------- |:-------------:| -----:|
| TF-IDF Scores    |  [AG's News Topic Classification Dataset](https://github.com/mhjabreel/CharCnn_Keras/tree/master/data/ag_news_csv)| 4 (World news, Business news, Sports news, Sci-Tech news) |
| Word2Vec    |  [AG's News Topic Classification Dataset](https://github.com/mhjabreel/CharCnn_Keras/tree/master/data/ag_news_csv)| 4 (World news, Business news, Sports news, Sci-Tech news) |
| FastText    |  [AG's News Topic Classification Dataset](https://github.com/mhjabreel/CharCnn_Keras/tree/master/data/ag_news_csv)| 4 (World news, Business news, Sports news, Sci-Tech news)|
| BERT  |  [AG's News Topic Classification Dataset](https://github.com/mhjabreel/CharCnn_Keras/tree/master/data/ag_news_csv)| 4 (World news, Business news, Sports news, Sci-Tech news)|

## [Sentiment Analysis - TR](https://github.com/ozcangundes/Text-Classification/tree/master/Sentiment%20Analysis%20-%20TR)

| Embedding Approach        | Dataset           | # of Classes |
| ------------- |:-------------:| -----:|
| TF-IDF Scores    |  kitapyurdu.com book reviews| 3 (negative, neutral, positive) |
| Word2Vec    |  kitapyurdu.com book reviews| 3 (negative, neutral, positive) |
| FastText    |  kitapyurdu.com book reviews| 3 (negative, neutral, positive)|
| [BERTurk](https://github.com/stefan-it/turkish-bert)    |  kitapyurdu.com book reviews| 3 (negative, neutral, positive) |
| [DistilBERTurk](https://github.com/stefan-it/turkish-bert)    |  kitapyurdu.com book reviews| 3 (negative, neutral, positive)|


## [Sentiment Analysis - EN](https://github.com/ozcangundes/Text-Classification/tree/master/Sentiment%20Analysis%20-%20EN)

| Embedding Approach        | Dataset           | # of Classes |
| ------------- |:-------------:| -----:|
| TF-IDF Scores    |  Amazon Musical Instruments reviews| 3 (negative, neutral, positive) |
| Word2Vec    |  Amazon Musical Instruments reviews| 3 (negative, neutral, positive) |
| FastText    |  Amazon Musical Instruments reviews| 3 (negative, neutral, positive)|


If you have any question about codes, dataset, models etc., feel free to reach me.
