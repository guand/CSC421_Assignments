class Confusion:
    """Summary
    Confusion Matrix
    Attributes:
        false_negative (int): False Negative
        false_positive (int): False Positive
        true_negative (int): True Negative
        true_positive (int): True Positive
    """
    def __init__(self):
        self.true_positive = 0
        self.false_positive = 0
        self.true_negative = 0
        self.false_negative = 0

    def incrementTP(self):
        self.true_positive += 1

    def incrementFP(self):
        self.false_positive += 1

    def incrementTN(self):
        self.true_negative += 1

    def incrementFN(self):
        self.false_negative += 1

    def getTP(self):
        return self.true_positive

    def getFP(self):
        return self.false_positive

    def getTN(self):
        return self.true_negative

    def getFN(self):
        return self.false_negative
