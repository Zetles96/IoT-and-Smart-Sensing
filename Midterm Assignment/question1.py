import matplotlib.pyplot as plt
import numpy as np


def ALOHA(G: float, N: int = None) -> float:
    """
    Calculate the successful rate of ALOHA
    :param G: Offered load rate
    :param N: Number of RFID tags
    :return: The successful rate of ALOHA
    """
    if N is None:
        return G * np.exp(-2 * G)
    else:
        return G * pow(1 - G / N, 2 * (N - 1))


def slotted_ALOHA(G: float, N: int = None) -> float:
    """
    Calculate the successful rate of Slotted ALOHA
    :param G: Offered load rate
    :param N: Number of RFID tags
    :return: The successful rate of Slotted ALOHA
    """
    if N is None:
        return G * np.exp(-G)
    else:
        return G * pow(1 - G / N, N - 1)


def plot_task_1() -> None:
    """
    Plot the successful rate of ALOHA and Slotted ALOHA
    :return: None
    """
    # Generate the x and y values for both curves
    x = np.linspace(0, 5, 100)
    y_aloha = ALOHA(x)
    y_slotted_aloha = slotted_ALOHA(x)

    # Plot the curves
    plt.plot(x, y_aloha, label='ALOHA', color='blue')
    plt.plot(x, y_slotted_aloha, label='Slotted ALOHA', color='orange')

    # Find the maximum values for both curves
    max_aloha = max(y_aloha)
    max_slotted_aloha = max(y_slotted_aloha)
    x_max_aloha = x[np.argmax(y_aloha)]
    x_max_slotted_aloha = x[np.argmax(y_slotted_aloha)]

    # Draw horizontal lines at the maximum values
    plt.axhline(max_aloha, color='blue', linestyle='--', label=f'Y Max ALOHA: {max_aloha:.2f}')
    plt.axhline(max_slotted_aloha, color='orange', linestyle='--',
                label=f'Y Max Slotted ALOHA: {max_slotted_aloha:.2f}')

    # Draw vertical lines at the x-values where y is max
    plt.axvline(x_max_aloha, color='blue', linestyle='--', label=f'X for Max ALOHA: {x_max_aloha:.2f}')
    plt.axvline(x_max_slotted_aloha, color='orange', linestyle='--',
                label=f'X for Max Slotted ALOHA: {x_max_slotted_aloha:.2f}')

    plt.xlabel('G = offered load rate')
    plt.ylabel('S = successful rate')
    plt.grid()
    plt.legend()
    plt.show()


def plot_task_2() -> None:
    """
    Plot the successful rate of ALOHA and Slotted ALOHA with different N in a 2x2 grid.
    :return:
    """
    N_values = [2, 10, 50, 100]
    x = np.linspace(0, 2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('ALOHA vs Slotted ALOHA')

    for i in range(2):
        for j in range(2):
            n = N_values[i * 2 + j]
            y_aloha = ALOHA(x, n)
            y_slotted_aloha = slotted_ALOHA(x, n)

            axs[i, j].plot(x, y_aloha, label=f'ALOHA N={n}')
            axs[i, j].plot(x, y_slotted_aloha, label=f'S_ALOHA N={n}')
            axs[i, j].set_title(f'N={n}')
            axs[i, j].set_xlabel('G = offered load rate')
            axs[i, j].set_ylabel('S = successful rate')
            axs[i, j].grid()
            axs[i, j].legend()

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)  # Add some space for the title
    plt.show()


if __name__ == '__main__':
    plot_task_1()
    plot_task_2()
