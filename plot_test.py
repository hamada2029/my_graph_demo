import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from qbstyles import mpl_style


DR = Path(__file__).parent


def main():
    """Main."""
    fp = DR / '2018.csv'
    df = pd.read_csv(str(fp))

    mpl_style(dark=True)
    fig = plt.figure(figsize=(10, 8), dpi=72)  # figsize * dpi
    ax = fig.add_subplot(111, xlabel=df['GameID'].name, ylabel='number')
    ax.plot(df['H'])
    ax.plot(df['HR'], 'rs:', label='HR', ms=10, mew=5, mec='green')
    ax.plot(df['K'], marker='^', linestyle='-.')

    fig.savefig(str(DR / 'plot.png'))
    plt.show()


if __name__ == '__main__':
    main()
