def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    fin=[]
    if chunk_size>len(tokens) and tokens:
        return [tokens]
    elif tokens==[]:
        return tokens
    for i in range(0,len(tokens),chunk_size-overlap):
        if len(tokens[i:i+chunk_size])!=chunk_size:
            pass
        else:
            fin.append(tokens[i:i+chunk_size])
    return fin