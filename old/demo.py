# import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

# from qbstyles import mpl_style
# mpl_style(dark=False)

# sns.set(style="ticks", context="talk")
# plt.style.use("dark_background")


DR = Path(__file__).parent


def main():
    """Main."""

    # Create a random (normal distribution) dataset
    observation_count = 1000
    series_count = 5
    random_data = np.random.randn(observation_count, series_count)
    print(random_data)
    bucket_count = 10

    fig = plt.figure(figsize=(14, 6))

    # Use context styling to change a single plot
    # with plt.style.context(('grayscale')):
    #     ax1 = fig.add_subplot(121)
    #     ax1.hist(random_data, bucket_count, cumulative=True)
    #     ax1.set_title('Context Styling')

    # # The overall style has stayed the same
    # ax2 = fig.add_subplot(122)
    # ax2.hist(random_data, bucket_count)
    # ax2.set_title('Existing Style')

    with plt.style.context(['seaborn-deep']):
        plt.hist(random_data, bucket_count)

    # Use default styling
    plt.hist(random_data, bucket_count)
    plt.show()
    return

    # df = sns.load_dataset('iris')
    # df.head()
    # return

    # # Plot the histogram thanks to the distplot function
    # sns.distplot(a=df["sepal_length"], hist=True, kde=False, rug=False)

    # sns.set_style("dark")

    # x = np.random.normal(size=100)
    # sns.displot(x)  # instead of dis't'plot

    # plt.show()
    # return


    fp = DR / '2018.csv'

    data = pd.read_csv(str(fp))
    df = data.iloc[0:10]
    print(df.head())

    # fig = plt.figure(figsize=(6.4, 4.8), dpi=100, facecolor='w', linewidth=0, edgecolor='w')
    # print(fig)
    # print(fig.get_figwidth(), fig.get_figheight())

    # fig = plt.figure(figsize=(6, 4), dpi=72,
    #                  facecolor='skyblue', linewidth=10, edgecolor='green')
    # fig.add_subplot(111)
    # fig.savefig('1-1_a.png',
    #             facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())

    fig = plt.figure()
    print(df.index[1])
    ax = fig.add_subplot(
        111,
        xlabel=df['GameID'].name,
        # ylabel=df['R'].name
    )
    # plt.yticks(rotation=70)
    plt.ylabel(df['R'].name, rotation=0)

    ax.bar(df.index, df['R'])

    for i in df.index:
        ax.text(
            i,
            df.at[i, 'R'],
            df.at[i, 'R'],
            horizontalalignment='center'
        )

    # fig.savefig('3-3_a.png')
    # sns.set_style("whitegrid")

    # plt.style.use('ggplot')
    # plt.style.use('pitayasmoothie-dark')
    fig.savefig('3-3_a.png')
    plt.show()

    # with plt.style.context('dark_background'):
    #     # plt.plot(x, y)
    #     plt.savefig('3-3_a.png')
    #     plt.show()


if __name__ == '__main__':
    main()
