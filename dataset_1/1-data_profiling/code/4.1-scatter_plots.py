from numpy import ndarray
from pandas import read_csv, DataFrame
from matplotlib.figure import Figure
from matplotlib.pyplot import subplots, savefig
from dataset_1.dslabs_functions import HEIGHT, plot_multi_scatters_chart

filename = "../../class_pos_covid.csv"
file_tag = "CovidPos"
data: DataFrame = read_csv(filename)
data = data.dropna()

vars: list = data.columns.to_list()

if [] != vars:
    target = "CovidPos"

    fig: Figure
    n: int = len(vars) - 1
    fig, axs = subplots(n, n, figsize=(n * HEIGHT, n * HEIGHT), squeeze=False)
    for i in range(len(vars)):
        var1: str = vars[i]
        for j in range(i + 1, len(vars)):
            var2: str = vars[j]
            plot_multi_scatters_chart(data, var1, var2, target, ax=axs[i, j - 1])
    print("Saving")
    savefig(f"../images/{file_tag}_sparsity_per_class_study.png")
else:
    print("Sparsity per class: there are no variables.")