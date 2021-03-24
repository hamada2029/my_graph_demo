import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path
from qbstyles import mpl_style


DR = Path(__file__).parent


def main():
    '''Main.'''
    mpl_style(dark=True)
    fig = plt.figure()

    ims = []

    for i in range(10):
        rand = np.random.randn(100)  # 100個の乱数を生成
        im = plt.plot(rand)  # 乱数をグラフにする
        ims.append(im)  # グラフを配列 ims に追加

    # 10枚のプロットを 100ms ごとに表示
    # aniは絶対要る
    ani = animation.ArtistAnimation(fig, ims, interval=100)
    ani.save(
        str(DR / 'anime.gif'),
        writer='pillow'
    )
    plt.show()


if __name__ == '__main__':
    main()
