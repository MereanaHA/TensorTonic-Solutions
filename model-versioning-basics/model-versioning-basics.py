def promote_model(models: list) -> str:
    """
    Returns the model name as a string.
    """
    # Write code here
    sorted_models=sorted(models,key= lambda x: (x["accuracy"],-x["latency"],x["timestamp"]),reverse=True)
    return sorted_models[0]["name"]
    pass