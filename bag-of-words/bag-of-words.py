import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    bow=np.zeros(len(vocab))
    for i in range(len(vocab)) :
        bow[i] = len([token for token in tokens if token == vocab[i]])
    return bow
    pass