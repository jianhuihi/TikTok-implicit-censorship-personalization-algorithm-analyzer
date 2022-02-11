import gensim
import nltk
from gensim import corpora, models
from nltk.stem import WordNetLemmatizer, SnowballStemmer

nltk.download('wordnet')
nltk.download('omw-1.4')


def lemmatize_stemming(text):
    stemmer = SnowballStemmer('english')
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


def topic_model(subtitles):
    # Preprocessing
    p_subs = map(preprocess, subtitles)

    # Bag of words
    dictionary = corpora.Dictionary(p_subs)
    dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

    bow_corpus = [dictionary.doc2bow(sub) for sub in p_subs]

    # TF-IDF
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    # LDA
    lda_model = gensim.models.LdaMulticore(corpus_tfidf, id2word=dictionary, passes=2, workers=4)
    topics = [lda_model[corpus_tfidf[i]] for i in range(len(subtitles))]

    return topics
