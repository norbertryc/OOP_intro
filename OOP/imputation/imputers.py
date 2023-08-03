from collections import Counter

class MeanImputer:

    def __init__(self):
        self.mean = None

    def fit(self, x):
        x_numbers_only = [el for el in x if el is not None]
        self.mean = sum(x_numbers_only) / len(x_numbers_only)

    def transform(self, x):
        if self.mean is None:
            raise AttributeError("You have to call `fit` method first.")
        # if not hasattr(self, "mean"): # przy tworzeniu mean w fit
        #     raise AttributeError("There is not 'mean' attribute. "
        #                          "You have to call `fit` method first.")
        return [el if el is not None else self.mean for el in x]


class ModeImputer:

    def __init__(self):
        self.mode = None

    def fit(self, x):
        x_numbers_only = [el for el in x if el is not None]
        self.mode = Counter(x_numbers_only).most_common(1)

    def transform(self, x):
        if self.mode is None:
            raise AttributeError("You have to call `fit` method first.")
        # if not hasattr(self, "mean"): # przy tworzeniu mean w fit
        #     raise AttributeError("There is not 'mean' attribute. "
        #                          "You have to call `fit` method first.")
        return [el if el is not None else self.mode for el in x]
