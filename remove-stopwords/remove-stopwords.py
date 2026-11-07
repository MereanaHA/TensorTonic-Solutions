def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    i=0
    while i<len(tokens) :
        if tokens[i] in stopwords :
            tokens=tokens[:i]+tokens[i+1:]
        else:
            i+=1
    return tokens
    pass