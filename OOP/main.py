from imputation.imputers import MeanImputer

if __name__ == '__main__':

    x = [1, 2, 3, None]
    imputer = MeanImputer()
    # imputer.fit(x)
    # print(imputer.mean)
    y = imputer.transform([7, 5, None, None])
    print(y)
