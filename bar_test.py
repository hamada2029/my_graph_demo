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
    fig = plt.figure(figsize=(12, 6), dpi=72)  # figsize * dpi
    ax = fig.add_subplot(
        111,  # 1行目1列の1番目
        xlabel=df['GameID'].name,
        # ylabel='number'
    )
    plt.ylabel('number', rotation=0, labelpad=30)
    fig.suptitle('Multi Bars')
    col_list = ['H', 'HR', 'K', 'BB']
    w = 0.15

    for i, col in enumerate(col_list):
        ax.bar(
            df.index + w * (i - len(col_list) / 2),
            df.loc[:, col],
            label=col,
            width=w,
            align='edge',
            zorder=10
        )

    ax.tick_params(bottom=False)
    ax.grid(axis='y', c='gainsboro', zorder=9)
    for side in ['right', 'top']:
        ax.spines[side].set_visible(False)
    ax.legend()

    fig.savefig(str(DR / 'bar.png'))
    plt.show()


if __name__ == '__main__':
    main()
