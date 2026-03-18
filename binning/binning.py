def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    try:
        minn=min(values)
        maxx=max(values)
        wid=(maxx-minn)/num_bins
    
        for i in range(len(values)):
            values[i]=min((values[i]-minn)//wid,num_bins-1)
    
        return values
    except ZeroDivisionError as ze:
        return [0]*len(values)