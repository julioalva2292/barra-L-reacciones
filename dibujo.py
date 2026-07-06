import matplotlib.pyplot as plt

def dibujar_barra(fuerza, distancia, altura):
    fig, ax = plt.subplots(figsize=(2.5, 2))

    # Barra horizontal verde (entre A y B)
    ax.plot([0, distancia], [0, 0], linewidth=3, color="green")

    # Barra vertical naranja (entre B y C)
    ax.plot([distancia, distancia], [0, altura], linewidth=3, color="orange")

    # Flecha roja (fuerza aplicada)
    ax.arrow(
        distancia + 30, altura,
        -25, 0,
        head_width=8,
        head_length=8,
        length_includes_head=True,
        color="red"
    )

    # Texto estilizado
    ax.text(distancia + 35, altura + 10, f"{fuerza:.0f} N", fontsize=9, color="red", fontweight="bold")
    ax.text(-10, -10, "A", fontsize=9, color="blue", fontweight="bold")
    ax.text(distancia - 5, -10, "B", fontsize=9, color="blue", fontweight="bold")
    ax.text(distancia - 5, altura + 10, "C", fontsize=9, color="orange", fontweight="bold")

    # Fondo claro
    ax.set_facecolor("#f9f9f9")

    ax.set_xlim(-15, distancia + 60)
    ax.set_ylim(-20, altura + 40)
    ax.set_aspect("equal")
    ax.grid(False)

    plt.tight_layout()
    return fig
