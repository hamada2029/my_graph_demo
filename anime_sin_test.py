import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path
from qbstyles import mpl_style


DR = Path(__file__).parent


def main():
    '''Main.'''
    mpl_style(dark=False)
    fig = plt.figure()
    x = np.arange(0, 10, 0.1)
    ims = []
    for a in range(50):
        y = np.sin(x - a)
        line, = plt.plot(x, y, 'r')
        ims.append([line])

    ani = animation.ArtistAnimation(fig, ims)
    ani.save(
        str(DR / 'anime_sin.gif'),
        writer='pillow'
    )
    # ani.save(
    #     'anime_sin.mp4',
    #     writer='ffmpeg'
    # )
    plt.show()


if __name__ == '__main__':
    main()
