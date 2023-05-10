from classes.PreProcess import PrePro
from classes.Naive import NaiveBayes
from classes.Metric import Metric
from dataset.database import get_df


df = get_df

prepro = PrePro()

df["x"] = df["x"].apply(prepro.lower_case)
df["x"] = df["x"].apply(prepro.remove_punctuation)
df["x"] = df["x"].apply(prepro.remove_stopwords)
df["x"] = df["x"].apply(prepro.lemmatized_word)

df.head()



