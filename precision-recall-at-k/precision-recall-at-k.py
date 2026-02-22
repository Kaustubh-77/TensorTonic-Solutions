def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended=recommended[:k]
    prec=len(set(recommended).intersection(set(relevant)))/k
    if k==0:
        prec=0
    rec=len(set(recommended).intersection(set(relevant)))/len(relevant)
    if len(relevant)==0:
        rec=0
    return [prec,rec]
    