import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).ratio()


print(string_similar("张三吃屎","张三吃了"))