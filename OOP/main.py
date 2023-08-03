from imputation.imputers import ModeImputer

if __name__ == '__main__':

    x = [1, 2, 3, 3, None]
    imputer = ModeImputer()
    # imputer.fit(x)
    # print(imputer.mean)
    y = imputer.transform([7, 5, None, None])
    print(y)
