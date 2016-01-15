#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    ### your code goes here
    
    cleaned_data = sorted(zip(ages, net_worths, (net_worths - predictions)**2),
                          key=lambda x: x[2])

    
    return cleaned_data[:int(0.9*len(cleaned_data))]

