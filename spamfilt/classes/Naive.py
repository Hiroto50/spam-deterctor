import pandas as pd
from tqdm import tqdm

from classes.PreProcess import PrePro

class NaiveBayes():
    def __init__(self, df, x, y):
        self.df = df.copy
        self.x = x
        self.y = y
        self.classes = df["y"].unique()

    def fit(self):
        self.relative_freq_table = dict()
        for class_ in self.classes:
            filter_df = self.df.query(f"{self.y} == @class_")
            class_words = ''.join(filter_df[self.x])
            class_words_format = pd.Series(class_words.split())
            freq_table = class_words_format.value_counts(True)
            self.relative_freq_table[class_] = freq_table

    def predict_single(self, phrase):
        prepro = PrePro()
        phrase = prepro.pre_all(phrase)
        words = phrase.split(" ")
        p_total = 0
        predicted_class = ""
        for class_ in self.classes:
            p_class = 1
            for word in words:
                if word in self.relative_freq_table[class_]:
                    p_word = self.relative_freq_table[class_][word]
                else:
                    p_word = self.relative_freq_table[class_].mean()
                p_class *= p_word
            if p_class >= p_total:
                p_total = p_class
                predicted_class = class_

        return predicted_class
    

    def predict(self, list_of_phrases):
        predictions = list()
        bar = tqdm(total=len(list_of_phrases))
        for phrase in list_of_phrases:
            prediction = self.predict_single(phrase)
            predictions.append(prediction)
            bar.update(1)

        return predictions