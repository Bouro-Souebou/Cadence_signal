import serial
import numpy as np
import matplotlib.pyplot as plt

# Paramètres pour la communication série
ser = serial.Serial('COM3', 9600)  # Remplacez 'COM3' par le port série approprié
min_sample_rate = 66  # Taux d'échantillonnage minimal en échantillons par seconde
max_sample_rate = 80  # Taux d'échantillonnage maximal en échantillons par seconde

# Calcul du taux d'échantillonnage effectif
effective_sample_rate = (min_sample_rate + max_sample_rate) / 2  # Valeur moyenne

# Calcul de la plage de cadence en Hz
min_cadence = 70 / 60  # Conversion de cpm en Hz
max_cadence = 180 / 60

# Calcul du nombre de cycles à couvrir
min_cycles = min_cadence / effective_sample_rate
max_cycles = max_cadence / effective_sample_rate

# Calcul de la taille du tampon en secondes
min_buffer_size = int(min_cycles) + 1  # Arrondi à l'entier supérieur
max_buffer_size = int(max_cycles) + 1

# Initialisation des listes pour stocker les données
time_data = []  # Temps en millisecondes
force_data = []  # Données de force sur la pagaie

# Initialisation de la figure pour l'affichage en temps réel
plt.figure()
plt.ion()  # Mode interactif pour mise à jour en temps réel

try:
    ser.open()
    while True:
        line = ser.readline().decode().strip()  # Lire une ligne de données
        if line:
            parts = line.split(',')  # Les données sont séparées par des virgules
            time_data.append(float(parts[0]))
            force_data.append(float(parts[1]))

            if len(time_data) > max_buffer_size:
                # Tronquer les données pour maintenir la taille du tampon
                time_data = time_data[-max_buffer_size:]
                force_data = force_data[-max_buffer_size:]

            if len(time_data) >= min_buffer_size:
                # Calcul de l'autocorrélation
                autocorrelation = np.correlate(force_data, force_data, mode='full')
                lags = np.arange(-len(force_data) + 1, len(force_data))

                # Recherche du pic principal dans l'autocorrélation
                cadence_period = lags[np.argmax(autocorrelation)]

                # Calcul de la cadence de pagayage en cpm
                cadence_cpm = 60.0 * 1000.0 / abs(cadence_period)

                # Affichage de l'autocorrélation en temps réel
                plt.clf()
                plt.plot(lags, autocorrelation)
                plt.xlabel('Lag')
                plt.ylabel('Autocorrelation')
                plt.title(f'Autocorrelation for Cadence Estimation (Period = {cadence_period} samples)')
                plt.grid(True)
                plt.draw()
                plt.pause(0.01)

                print(f'Cadence de pagayage estimée : {cadence_cpm} cpm')
finally:
    ser.close()
