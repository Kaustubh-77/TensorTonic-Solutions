def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    # prec=len(set(recommended).intersection(set(relevant)))/k
    # rec=len(set(recommended).intersection(set(relevant)))/len(relevant)
    # return [prec,rec]
    recommended_k = recommended[:k]
    hits = len(set(recommended_k) & set(relevant))
    
    precision = hits / k if k > 0 else 0
    recall = hits / len(relevant) if len(relevant) > 0 else 0
    
    return [precision, recall]