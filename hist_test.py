import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from qbstyles import mpl_style


DR = Path(__file__).parent


def main():
    """Main."""
    fp = DR / '2018.csv'
    data = pd.read_csv(str(fp))

    mpl_style(dark=True)
    fig = plt.figure(figsize=(8, 4), dpi=72)  # figsize * dpi
    ax = fig.add_subplot(
        111,  # 1行目1列の1番目
        xticks=range(0, 20, 2)
    )
    n, bins, patches = ax.hist(data['R'], bins=data['R'].max() - data['R'].min())

    fig.suptitle('Hist')

    for i in range(len(bins) - 1):
        ax.text(
            (bins[i + 1] + bins[i]) / 2,
            n[i],
            int(n[i]),
            horizontalalignment='center'
        )

    fig.savefig(str(DR / 'hist.png'))
    plt.show()


if __name__ == '__main__':
    main()
