from collections import Counter

class BaseImputer:

    def __init__(self):
        self.fill_value = None

    def _filter_none(self, x):
        return [el for el in x if el is not None]

    def transform(self, x):
        if self.fill_value is None:
            raise AttributeError("You have to call `fit` method first.")
        return [el if el is not None else self.fill_value for el in x]


class MeanImputer(BaseImputer):

    def fit(self, x):
        x_numbers_only = self._filter_none(x)
        self.fill_value = sum(x_numbers_only) / len(x_numbers_only)


class ModeImputer(BaseImputer):

    def fit(self, x):
        x_numbers_only = self._filter_none(x)
        self.fill_value = Counter(x_numbers_only).most_common(1)[0][0]


# class MeanImputer:
#
#     def __init__(self):
#         self.mean = None
#
#     def fit(self, x):
#         x_numbers_only = [el for el in x if el is not None]
#         self.mean = sum(x_numbers_only) / len(x_numbers_only)
#
#     def transform(self, x):
#         if self.mean is None:
#             raise AttributeError("You have to call `fit` method first.")
#         return [el if el is not None else self.mean for el in x]
#
#
# class ModeImputer:
#
#     def __init__(self):
#         self.mode = None
#
#     def fit(self, x):
#         x_numbers_only = [el for el in x if el is not None]
#         self.mode = Counter(x_numbers_only).most_common(1)[0][0]
#
#     def transform(self, x):
#         if self.mode is None:
#             raise AttributeError("You have to call `fit` method first.")
#         return [el if el is not None else self.mode for el in x]


class Imputer:

    def __init__(self, method):
        self.method = method # "mean" albo "mode"
        self.fill_value = None

    def fit(self, x):
        x_numbers_only = [el for el in x if el is not None]
        if self.method == "mode":
            self.fill_value = Counter(x_numbers_only).most_common(1)[0][0]
        elif self.method == "mean":
            self.fill_value = sum(x_numbers_only) / len(x_numbers_only)

    def transform(self, x):
        # if self.mode is None and self.mean is None:
        #     raise AttributeError("You have to call `fit` method first.")
        return [el if el is not None else self.fill_value for el in x]

# BaseImputer -> MeanImputer, ModeImputer
# Chcemy zaimplementować klasy MeanImputer, ModeImputer zastępujące None
# odpowiednio średnią lub modą i te klasy w jak największym stopniu
# powinny wykorzystywać klasę BaseImputer, z której będą dziedziczyć

