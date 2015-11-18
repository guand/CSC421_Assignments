
import glob
import random
from collections import OrderedDict
from confusion import Confusion


def sentimentList(sentiment_list):
    """Summary

    Args:
        sentiment_list (TYPE): A list of Reviews

    Returns:
        TYPE: A list of binary lists for the provided list of key words from the assignment
    """
    new_list = []
    for file in sentiment_list:
        with open(file) as f:
            sentiment_list = [('awful', 0), ('bad', 0), ('boring', 0), ('dull', 0),
                              ('effective', 0), ('enjoyable', 0), ('great', 0), ('hilarious', 0)]
            sentiment_dictionary = OrderedDict(sentiment_list)
            lines = f.readlines()
            lower_lines = [x.lower() for x in lines]
            for key in sentiment_dictionary.iterkeys():
                if any(key in s for s in lines):
                    sentiment_dictionary[key] = 1
            new_list.append(sentiment_dictionary.values())
    return new_list


def sentimentSumList(new_list):
    """Summary
    
    Args:
        new_list (TYPE): A list of binary lists based on the Reviews
    
    Returns:
        TYPE: A summation of the binary lists for each of its individual element into a single list 
    """
    return [sum(i) for i in zip(*new_list)]


def sentimentProbabilityList(new_list, review_count):
    """Summary
    
    Args:
        new_list (TYPE): The summation list of binary lists
        review_count (TYPE): the total number of positive or negative reviews
    
    Returns:
        TYPE: A list of probability values for each element in the list showing up in either the positive or negative reviews
    """
    return [x / float(review_count) for x in new_list]


def likelyhoodProbability(polarity_vector, prior_probability, probability_list):
    """Summary
    
    Args:
        polarity_vector (TYPE): A single binary list from either the positive or negative review
        prior_probability (TYPE): The probability of the positive or negative reviews over both reviews
        probability_list (TYPE): The polarity probability list
    
    Returns:
        TYPE: The probability of the binary list
    """
    likelyhood_probability = prior_probability
    for i, j in zip(polarity_vector, probability_list):
        if i == 0:
            likelyhood_probability *= (1.0 - j)
        else:
            likelyhood_probability *= j
    return likelyhood_probability


def naiveBayesClassifier(polarity_vector, prior_positive_probability, prior_negative_probability, positive_probability_list, negative_probability_list):
    """Summary
    
    Args:
        polarity_vector (TYPE): A single binary list from either the positive or negative review
        prior_positive_probability (TYPE): The probability of the positive reviews over both reviews
        prior_negative_probability (TYPE): The probability of the negative reviews over both reviews
        positive_probability_list (TYPE): The positive polarity probability list
        negative_probability_list (TYPE): The negative polarity probability list
    
    Returns:
        TYPE: A boolean type determing whether the polarity_probability belongs in either True Positive(TP), False Positive(FP), True Negative(TN), False Negative(FN)
    """
    positive_polarity_probability = likelyhoodProbability(
        polarity_vector, prior_positive_probability, positive_probability_list)
    negative_polarity_probability = likelyhoodProbability(
        polarity_vector, prior_negative_probability, negative_probability_list)
    if positive_polarity_probability > negative_polarity_probability:
        return True
    else:
        return False


def completeData(positive_review_count, negative_review_count, new_positive_list, new_negative_list, prior_positive_probability, prior_negative_probability):
    """Summary
    
    Args:
        positive_review_count (TYPE): Total number of positive reviews
        negative_review_count (TYPE): Total number of negative reviews
        new_positive_list (TYPE): Binary list of lists for the positive reviews
        new_negative_list (TYPE): Binary list of lists for the negative reviews
        prior_positive_probability (TYPE): The probability of the positive reviews over both reviews
        prior_negative_probability (TYPE): The probability of the negative reviews over both reviews
    
    Returns:
        TYPE: Runs the complete data set as both the training and testing sets to get the confusion matrix and accuracy
    """
    negative_sum_list = sentimentSumList(new_negative_list)
    negative_probability_list = sentimentProbabilityList(
        negative_sum_list, negative_review_count)
    positive_sum_list = sentimentSumList(new_positive_list)
    positive_probability_list = sentimentProbabilityList(
        positive_sum_list, positive_review_count)
    print positive_probability_list
    print negative_probability_list
    confusion_matrix = Confusion()
    for positive_vector in new_positive_list:
        polarity = naiveBayesClassifier(positive_vector, prior_positive_probability,
                                        prior_negative_probability, positive_probability_list, negative_probability_list)
        if polarity:
            confusion_matrix.incrementTP()
        else:
            confusion_matrix.incrementFP()

    for negative_vector in new_negative_list:
        polarity = naiveBayesClassifier(negative_vector, prior_positive_probability,
                                        prior_negative_probability, positive_probability_list, negative_probability_list)
        if polarity:
            confusion_matrix.incrementFN()
        else:
            confusion_matrix.incrementTN()

    accuracy = (confusion_matrix.getTP() + confusion_matrix.getTN()) / float(confusion_matrix.getTP() +
                                                                             confusion_matrix.getFP() + confusion_matrix.getTN() + confusion_matrix.getFN())

    print "True Positive: " + str(confusion_matrix.getTP())
    print "False Positive: " + str(confusion_matrix.getFP())
    print "True Negative: " + str(confusion_matrix.getTN())
    print "False Negative: " + str(confusion_matrix.getFN())
    print "Complete Data Method"
    print "Accuracy: " + str(accuracy)


def tenFoldData(k, positive_training_size, negative_training_size, prior_positive_fold_probability, prior_negative_fold_probability):
    """Summary
    
    Args:
        k (TYPE): Fold number
        positive_training_size (TYPE): The training size for the positive reviews in the fold method
        negative_training_size (TYPE): The training size for the positive reviews in the fold method
        prior_positive_fold_probability (TYPE): The probability of the positive reviews over both reviews for fold method
        prior_negative_fold_probability (TYPE): The probability of the negative reviews over both reviews for fold method
    
    Returns:
        TYPE: Calculates the confusion_matrix and accuracy of the reviews using the 10 fold cross validation method
    """
    total_tp = []
    total_fp = []
    total_tn = []
    total_fn = []
    total_accuracy = []
    for f in xrange(0, k):
        confusion_matrix = Confusion()
        positive_training_list = glob.glob(
            'review_polarity/txt_sentoken/pos/cv[!' + str(f) + ']*.txt')
        new_positive_training_list = sentimentList(positive_training_list)
        positive_sum_training_list = sentimentSumList(
            new_positive_training_list)
        positive_probability_training_list = sentimentProbabilityList(
            positive_sum_training_list, positive_training_size)
        positive_testing_list = glob.glob(
            'review_polarity/txt_sentoken/pos/cv' + str(f) + '*.txt')
        new_positive_testing_list = sentimentList(positive_testing_list)
        negative_training_list = glob.glob(
            'review_polarity/txt_sentoken/neg/cv[!' + str(f) + ']*.txt')
        new_negative_training_list = sentimentList(negative_training_list)
        negative_sum_training_list = sentimentSumList(
            new_negative_training_list)
        negative_probability_training_list = sentimentProbabilityList(
            negative_sum_training_list, negative_training_size)
        negative_testing_list = glob.glob(
            'review_polarity/txt_sentoken/neg/cv' + str(f) + '*.txt')
        new_negative_testing_list = sentimentList(negative_testing_list)
        for positive_vector in new_positive_testing_list:
            polarity = naiveBayesClassifier(positive_vector, prior_positive_fold_probability,
                                            prior_negative_fold_probability, positive_probability_training_list, negative_probability_training_list)
            if polarity:
                confusion_matrix.incrementTP()
            else:
                confusion_matrix.incrementFP()

        for negative_vector in new_negative_testing_list:
            polarity = naiveBayesClassifier(negative_vector, prior_positive_fold_probability,
                                            prior_negative_fold_probability, positive_probability_training_list, negative_probability_training_list)
            if polarity:
                confusion_matrix.incrementFN()
            else:
                confusion_matrix.incrementTN()
        total_tp.append(confusion_matrix.getTP())
        total_fp.append(confusion_matrix.getFP())
        total_tn.append(confusion_matrix.getTN())
        total_fn.append(confusion_matrix.getFN())
        accuracy = (confusion_matrix.getTP() + confusion_matrix.getTN()) / float(confusion_matrix.getTP() +
                                                                                 confusion_matrix.getFP() + confusion_matrix.getTN() + confusion_matrix.getFN())
        total_accuracy.append(accuracy)
    print "True Positive: " + str(sum(total_tp))
    print "False Positive: " + str(sum(total_fp))
    print "True Negative: " + str(sum(total_tn))
    print "False Negative: " + str(sum(total_fn))
    print "10-Fold Cross Validation Method"
    print "Accuracy: " + str(sum(total_accuracy) / k)


def review_generation(polarity_probability):
    """Summary
    
    Args:
        polarity_probability (TYPE): Polarity probability list of either the positive or negative reviews
    
    Returns:
        TYPE: Randomly generated binary list of either a positive review or negative review based on the polarity probability
    """
    review_list = []
    sentiment_word_list = [
        'awful', 'bad', 'boring', 'dull', 'effective', 'enjoyable', 'great', 'hilarious']
    sentiment_dictionary = dict(zip(sentiment_word_list, polarity_probability))
    for key, item in sentiment_dictionary.iteritems():
        sample = random.random()
        if sample <= item:
            review_list.append(key)
    return review_list


def main():
	# read the files from pos directory
    positive_list = glob.glob('review_polarity/txt_sentoken/pos/*.txt')
    # convert them to binary lists
    new_positive_list = sentimentList(positive_list)
    # read the files from neg directory
    negative_list = glob.glob('review_polarity/txt_sentoken/neg/*.txt')
    # convert them to binary lists
    new_negative_list = sentimentList(negative_list)
    # get number of reviews
    positive_review_count = len(new_positive_list)
    negative_review_count = len(new_negative_list)
    # get total number of reviews
    total_count = positive_review_count + negative_review_count
    # calculate prior probability
    prior_positive_probability = positive_review_count / float(total_count)
    prior_negative_probability = negative_review_count / float(total_count)
    # run all data training and testing set
    completeData(positive_review_count, negative_review_count, new_positive_list,
                 new_negative_list, prior_positive_probability, prior_negative_probability)
    # fold number
    k = 10
    # set the training size based on the fold number
    positive_training_size = (positive_review_count / k) * (k - 1)
    negative_training_size = (negative_review_count / k) * (k - 1)
    # set the testing size based on the fold number
    positive_testing_size = positive_review_count - positive_training_size
    negative_testing_size = negative_review_count - negative_training_size
    # get fold size
    fold_size = total_count / k

    training_total_size = fold_size * (k - 1)
    # get prior probability based on fold size
    prior_positive_fold_probability = positive_training_size / \
        float(training_total_size)
    prior_negative_fold_probability = negative_training_size / \
        float(training_total_size)
    # run 10-fold cross validation method
    tenFoldData(k, positive_training_size, negative_training_size,
                prior_positive_fold_probability, prior_negative_fold_probability)

    negative_sum_list = sentimentSumList(new_negative_list)
    negative_probability_list = sentimentProbabilityList(
        negative_sum_list, negative_review_count)
    positive_sum_list = sentimentSumList(new_positive_list)
    positive_probability_list = sentimentProbabilityList(
        positive_sum_list, positive_review_count)
    # set number of randomly genrated reviews
    number_of_reviews = 5
    # run and get 5 random reviews for both positive and negative polarity probability lists
    print "Random Positive Reviews"
    for i in range(number_of_reviews):
        print review_generation(positive_probability_list)
    print "Random Negative Reviews"
    for i in range(number_of_reviews):
        print review_generation(negative_probability_list)

if __name__ == "__main__":
    main()
