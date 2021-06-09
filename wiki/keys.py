import wikipedia
import yake

def ExtractKeysFromWiki(subject):
    wikipedia.set_lang("pt")
    text = wikipedia.summary(subject)

    keys = yake.KeywordExtractor(lang="pt")
    keywords = keys.extract_keywords(text)

    return keywords