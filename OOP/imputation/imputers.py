# Transformatory danych
#
# Zadanie 1.
#
# Zdfiniuje klasę `MeanImputer`, która będzie służyła do uzupełniania braków w danych,
# na podstawie danych historycznych:
#
# a) `fit`, która jako argument wejściowy będzie przyjmowała listę wartości liczbowych i `None`,
#     a jej wywołanie policzy średnią z liczbowych wartości w liście i zapisze wynik w atrybucie.
#     Przed pójściem dalej przetestuje metodę.
#
# b) `transform`, która dla listy wejściowej zawierajacej wartości liczbowe oraz `None`,
#    zwróci modyfikacje tej listy, w której zastapi wartości `None` wyliczoną wcześniej średnią.
#
# Zaprezentuj działanie metod.

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
