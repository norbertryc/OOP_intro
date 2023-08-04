from imputation.imputers import MeanImputer

if __name__ == '__main__':

    x = [1,2,3,3, None]
    imputer = MeanImputer()
    imputer.fit(x)
    print(imputer.transform([1, None, 4]))

