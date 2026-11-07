def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    return [token for token in tokens if (token not in stopwords)]
    pass