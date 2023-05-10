import string


from constant.prepro import NORMALIZATION_RULES, STOP_WORDS

class PrePro():
    def lower_case(self, text):
        return text.lower()
    
    def remove_punctuation(self, text):
        text_transform = text.translate(str.maketrans('','', string.punctuation))
        text = text_transform
        return text
    
    def remove_stopwords(self, text):
        words  = text.split()
        filtered_words = [word for word in words if word.lower() not in STOP_WORDS]
        filtered_text = " ".join(filtered_words)
        return filtered_text
    
    def lemmatize_text(self, text):
        words = text.split()
        lemmatized = [self.lemmatized_word(word) for word in words]
        filt_text = " ".join(lemmatized)
        return filt_text
    
    def lemmatized_word(self, text):
        for suffix, replacement in NORMALIZATION_RULES.items():
            if word.endswith(suffix):
                word = word[:-len(suffix)] + replacement
                break
        return word


    def pre_all(self, text):
        text = self.lower_case(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lemmatized_word(text)
        return text