import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    """Main."""
    # print(mpl.get_configdir())
    # print(mpl.matplotlib_fname())
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)
    # sns.set()
    # sns.set_palette("winter", 8)
    plt.style.use('grayscale')
    plt.plot(x, y)
    plt.savefig('matplotlib_style_default.png')
    return

    # plt.style.use('ggplot')
    with plt.style.context(['ggplot', 'dark_background']):
        plt.plot(x, y)
        plt.savefig('matplotlib_style_default.png')
        # plt.show()


if __name__ == '__main__':
    main()
