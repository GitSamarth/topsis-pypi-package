def main():
    import sys
    import pandas as pd
    import numpy as np

    # ---------- Argument check ----------
    if len(sys.argv) != 5:
        print("Error: Please provide exactly 4 arguments")
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    output_file = sys.argv[4]

    # ---------- Read CSV ----------
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)

    # ---------- Numeric check ----------
    try:
        matrix = data.iloc[:, 1:].astype(float).values
    except ValueError:
        print("Error: All columns except first must be numeric")
        sys.exit(1)

    n_criteria = matrix.shape[1]

    # ---------- Weights ----------
    try:
        weights = list(map(float, weights_input.split(",")))
    except:
        print("Error: Weights must be numeric and comma separated")
        sys.exit(1)

    if len(weights) != n_criteria:
        print("Error: Number of weights must equal number of criteria")
        sys.exit(1)

    # ---------- Impacts ----------
    impacts = impacts_input.split(",")

    if len(impacts) != n_criteria:
        print("Error: Number of impacts must equal number of criteria")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be either + or -")
            sys.exit(1)

    weights = np.array(weights)

    # ================= TOPSIS START =================

    # Step 1: Normalize
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm

    # Step 2: Weighted normalized matrix
    weighted = normalized * weights

    # Step 3: Ideal best and worst
    ideal_best = np.zeros(n_criteria)
    ideal_worst = np.zeros(n_criteria)

    for i in range(n_criteria):
        if impacts[i] == '+':
            ideal_best[i] = weighted[:, i].max()
            ideal_worst[i] = weighted[:, i].min()
        else:
            ideal_best[i] = weighted[:, i].min()
            ideal_worst[i] = weighted[:, i].max()

    # Step 4: Distance calculation
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)

    # Step 6: Rank
    data["Topsis Score"] = scores
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    # ---------- Output ----------
    data.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully")

if __name__ == "__main__":
    main()




