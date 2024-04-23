import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download required NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

def perform_tokenization(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def perform_pos_tagging(tokens):
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

def perform_named_entity_recognition(text):
    named_entities = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
    return named_entities

def perform_sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)

    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_score

def perform_dependency_parsing(text):
    # Dependency parsing requires more advanced libraries such as spaCy
    # This example uses NLTK's shallow parser as an alternative
    grammar = r"""
        NP: {<DT|JJ|NN.*>+}          # Noun Phrase
        PP: {<IN><NP>}                # Prepositional Phrase
        VP: {<VB.*><NP|PP|CLAUSE>+$}  # Verb Phrase
        CLAUSE: {<NP><VP>}            # Clause
    """
    parser = nltk.RegexpParser(grammar)
    parsed_text = parser.parse(nltk.pos_tag(nltk.word_tokenize(text)))
    return parsed_text

def main():
    # Example text for NLP tasks
    text = "Natural Language Processing (NLP) is a fascinating field. It involves " \
           "tokenization, part-of-speech tagging, named entity recognition, sentiment " \
           "analysis, and dependency parsing."

    # Perform NLP tasks
    tokens = perform_tokenization(text)
    pos_tags = perform_pos_tagging(tokens)
    named_entities = perform_named_entity_recognition(text)
    sentiment, sentiment_score = perform_sentiment_analysis(text)
    dependency_tree = perform_dependency_parsing(text)

    # Display results
    print("Text:", text)
    print("\n1. Tokenization:")
    print(tokens)
    print("\n2. Part-of-Speech Tagging:")
    print(pos_tags)
    print("\n3. Named Entity Recognition:")
    print(named_entities)
    print("\n4. Sentiment Analysis:")
    print("Sentiment:", sentiment)
    print("Sentiment Score:", sentiment_score)
    print("\n5. Dependency Parsing:")
    print(dependency_tree)

if __name__ == "__main__":
    main()
