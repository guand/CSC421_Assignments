"""Summary"""
import random


def probability_first_level(true_probability):
    """Summary
    
    Args:
        true_probability (TYPE): probability of a single value
    
    Returns:
        TYPE: Boolean value of whether it is within the probability or not
    """
    sample = random.random()
    if sample > true_probability:
        return False
    return True


def probability_second_level(first, true_probability, false_probability):
    """Summary
    
    Args:
        first (BOOLEAN): The element that the current element is basing its probability on
        true_probability (TYPE): If the element is true check is within the probability or not
        false_probability (TYPE): If the element is false check is within the probability or not
    
    Returns:
        TYPE: Boolean value based on a previous element and if it is within the probability or not
    """
    sample = random.random()
    if first:
        if sample > true_probability:
            return False
        return True
    else:
        if sample > false_probability:
            return False
        return True


def probability_third_level(first_a, first_b, true_true_probability, true_false_probability, false_true_probability, false_false_probability):
    """Summary
    
    Args:b
        first_a (BOOLEAN): Element one
        first_b (BOOLEAN): Element two
        true_true_probability (TYPE): If both one and two are true
        true_false_probability (TYPE): If one is true and two is false
        false_true_probability (TYPE): If one is false and two is true
        false_false_probability (TYPE): If both one and two are false
    
    Returns:
        TYPE: Boolean value for two element truth table, meaning it is based on the outcome of two previous elements and if it is within the probability or not
    """
    sample = random.random()
    if first_a and first_b:
        if sample > true_true_probability:
            return False
        return True
    elif first_a and not first_b:
        if sample > true_false_probability:
            return False
        return True
    elif not first_a and first_b:
        if sample > false_true_probability:
            return False
        return True
    else:
        if sample > false_false_probability:
            return False
        return True

def baysianBeliefNetworks(sample_size):
    """Summary
    
    Args:
        sample_size (TYPE): The number of times to run random samples
    
    Returns:
        TYPE: A approximate probability of each of the probabilities requested of assignment 2 part 2 the
        higher the sample size the more accurate the probability is
    """
    # probability(fl, st, fe, !br, !sm, co, !wh)
    true_table = [True, True, True, False, False, True, False]
    # probability(fl | co, !wh)
    true_table_two = [True, True, False]
    # probability(co, !wh)
    true_table_three = [True, False]
    # counter used to see the number of probability(fl, st, fe, !br, !sm, co, !wh) that are hit based on the sample size
    counter = 0
    # ounter used to see the number of probability(fl | co, !wh) that are hit based on the sample size
    counter_two = 0
    # ounter used to see the number of probability(co, !wh) that are hit based on the sample size
    counter_three = 0
    for i in range(sample_size):
        flu = probability_first_level(0.05)
        smokes = probability_first_level(0.15)
        fever = probability_second_level(flu, 0.75, 0.01)
        sore_throat = probability_second_level(flu, 0.90, 0.04)
        bronchitis = probability_third_level(
            flu, smokes, 0.95, 0.90, 0.25, 0.03)
        coughing = probability_second_level(bronchitis, 0.80, 0.08)
        wheezing = probability_second_level(bronchitis, 0.70, 0.05)
        current_table = [
            flu, sore_throat, fever, bronchitis, smokes, coughing, wheezing]
        current_table_two = [flu, coughing, wheezing]
        current_table_three = [coughing, wheezing]
        if current_table == true_table:
            counter = counter + 1
        if current_table_two == true_table_two:
            counter_two = counter_two + 1
        if current_table_three == true_table_three:
            counter_three = counter_three + 1
    print "probability(fl, st, fe, !br, !sm, co, !wh): " + str(counter / float(sample_size))
    # rejection sampling
    if counter_three != 0:
        print "probability(fl | co, !wh): " + str(counter_two / float(counter_three))
    else:
        print 0

def main():
    # sample size
    sample_size = 10
    baysianBeliefNetworks(sample_size)
    sample_size = 100
    baysianBeliefNetworks(sample_size)
    sample_size = 1000
    baysianBeliefNetworks(sample_size)
    sample_size = 10000
    baysianBeliefNetworks(sample_size)
    sample_size = 100000
    baysianBeliefNetworks(sample_size)
    sample_size = 1000000
    baysianBeliefNetworks(sample_size)
    sample_size = 10000000
    baysianBeliefNetworks(sample_size)



if __name__ == "__main__":
    main()
