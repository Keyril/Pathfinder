import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()
import pandas as pd


def Show_Acc():
    df = pd.read_csv('Results.csv', usecols=['Grid', 'Range', 'Avg_Accuracy']).dropna()
    df['Grid'] = df['Grid'].str.partition('x')[2].astype(int)
    df['Range'] = df['Range'].str.partition(' - ')[2].astype(int)
    df['Avg_Accuracy'] = df['Avg_Accuracy'].str[:-1].astype(float)
    grid = sns.FacetGrid(df, col="Grid", hue="Grid", col_wrap=3, height=3)

    grid.map(plt.scatter, "Range", "Avg_Accuracy", marker="o", alpha=0.5)
    grid.fig.tight_layout(w_pad=1)
    plt.show()


def Show_Lowest_Acc():
    df = pd.read_csv('Results.csv', usecols=['Grid', 'Range', 'Lowest Accuracy']).dropna()
    df['Grid'] = df['Grid'].str.partition('x')[2].astype(int)
    df['Range'] = df['Range'].str.partition(' - ')[2].astype(int)
    df['Lowest Accuracy'] = df['Lowest Accuracy'].str[:-1].astype(float)
    grid = sns.FacetGrid(df, col="Grid", hue="Grid", col_wrap=3, height=3)

    grid.map(plt.scatter, "Range", "Lowest Accuracy", marker="o", alpha=0.5)
    grid.fig.tight_layout(w_pad=1)
    plt.show()


def Show_Speed():
    df = pd.read_csv('Results.csv', usecols=['Grid', 'Range', 'Avg_Faster']).dropna()
    df['Grid'] = df['Grid'].str.partition('x')[2].astype(int)
    df['Range'] = df['Range'].str.partition(' - ')[2].astype(int)
    df['Avg_Faster'] = df['Avg_Faster'].str[:-1].astype(float)
    grid = sns.FacetGrid(df, col="Grid", hue="Grid", col_wrap=3, height=3)

    grid.map(plt.scatter, "Range", "Avg_Faster", marker="o", alpha=0.5)
    grid.fig.tight_layout(w_pad=1)
    plt.show()


def Show_Speed_VS_Accuracy():
    df = pd.read_csv('Results.csv', usecols=['Range', 'Avg_Accuracy', 'Avg_Faster']).dropna()
    df['Range'] = df['Range'].str.partition(' - ')[2].astype(int)
    df['Avg_Accuracy'] = df['Avg_Accuracy'].str[:-1].astype(float)
    df['Avg_Faster'] = df['Avg_Faster'].str[:-1].astype(float)
    grid = sns.FacetGrid(df, col="Range", hue="Range", col_wrap=3, height=3)

    grid.map(plt.scatter, "Avg_Faster", "Avg_Accuracy", marker="o", alpha=0.5)
    grid.fig.tight_layout(w_pad=1)
    plt.show()


def Show_Speed_Grid_Accuracy():
    df = pd.read_csv('Results.csv', usecols=['Grid', 'Avg_Accuracy', 'Avg_Faster']).dropna()
    df['Grid'] = df['Grid'].str.partition('x')[2].astype(int)
    df['Avg_Faster'] = df['Avg_Faster'].str[:-1].astype(float)
    df['Avg_Accuracy'] = df['Avg_Accuracy'].str[:-1].astype(float)
    grid = sns.FacetGrid(df, col="Grid", hue="Grid", col_wrap=3, height=3)

    grid.map(plt.scatter, "Avg_Faster", "Avg_Accuracy", marker="o", alpha=0.5)
    grid.fig.tight_layout(w_pad=1)
    plt.show()


# Show_Speed_VS_Accuracy()
Show_Speed_Grid_Accuracy()
# sns.lmplot(x="Range", y=
# "Avg_Accuracy", data=df, fit_reg=False, hue='Grid', legend=False)
# plt.legend(loc='lower right')
#
# plt.show()
