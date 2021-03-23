import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from qbstyles import mpl_style


DR = Path(__file__).parent


def main():
    """Main."""
    # Create a random (normal distribution) dataset
    observation_count = 1000
    series_count = 5
    random_data = np.random.randn(observation_count, series_count)
    # print(random_data)
    bucket_count = 10

    mpl_style(dark=False)
    fig = plt.figure(figsize=(14, 6), dpi=72)
    fig.suptitle('Hist Random')

    # Use default styling
    plt.hist(random_data, bucket_count)
    fig.savefig(str(DR / 'hist_rand.png'))
    plt.show()


if __name__ == '__main__':
    main()
