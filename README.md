Ce code Python est conçu pour mesurer la cadence de pagayage à partir de données de force échantillonnées sur une pagaie. Le code utilise l'autocorrélation pour estimer la cadence de pagayage en temps réel. Il prend en compte les spécifications du capteur, notamment le taux d'échantillonnage effectif et la plage attendue de la cadence de pagayage.

## Spécifications du Capteur

Le code est conçu pour fonctionner avec un capteur qui échantillonne les données de force à une fréquence maximale de 80 Hz. Cependant, en pratique, le taux d'échantillonnage effectif varie généralement entre 66 et 80 échantillons par seconde en raison de fluctuations.

## Démarche pour Déterminer la Taille du Tampon

Pour obtenir des mesures de cadence précises, il est essentiel de déterminer la taille du tampon (buffer) utilisée pour le calcul de l'autocorrélation. La taille du tampon doit être choisie de manière à capturer les variations de la cadence de pagayage tout en maintenant des performances en temps réel. Voici comment la taille du tampon est calculée :

1. **Fréquence de la Cadence de Pagayage** : La plage attendue de la cadence de pagayage est de 70 à 180 coups par minute (cpm), ce qui équivaut à une plage de fréquence allant de 1,17 Hz à 3 Hz.

2. **Taux d'Échantillonnage Effectif** : Le code calcule un taux d'échantillonnage effectif en prenant la moyenne entre le taux d'échantillonnage minimal (66 échantillons par seconde) et le taux maximal (80 échantillons par seconde). Cela équivaut à environ 73 échantillons par seconde.

3. **Nombre de Cycles** : Pour capturer efficacement les variations de la cadence de pagayage, le code calcule le nombre de cycles de cadence minimum et maximum pouvant être couverts dans le tampon en fonction du taux d'échantillonnage effectif.

4. **Taille du Tampon** : La taille du tampon est déterminée en arrondissant le nombre de cycles calculé à l'entier supérieur. Cette taille est ensuite utilisée pour maintenir le tampon à la longueur requise.

## Utilisation du Tampon pour l'Autocorrélation

Le code lit en continu les données de force sur la pagaie depuis le capteur via un port série. Il maintient un tampon de données de force de la taille appropriée, tronquant les données les plus anciennes à mesure que de nouvelles données arrivent.

À partir de ces données tamponnées, le code calcule l'autocorrélation en utilisant la bibliothèque NumPy. L'autocorrélation permet de déterminer la période de répétition des variations dans les données, ce qui correspond à la cadence de pagayage.

Le pic principal dans l'autocorrélation est identifié, et la période de ce pic est utilisée pour calculer la cadence de pagayage en coups par minute (cpm).

## Affichage en Temps Réel

Le code utilise également la bibliothèque Matplotlib pour afficher en temps réel l'autocorrélation, ce qui peut être utile pour le débogage et la visualisation.

En fin de compte, l'estimation de la cadence de pagayage est affichée en temps réel, permettant aux utilisateurs de surveiller la cadence pendant l'activité sportive.

N'oubliez pas d'ajuster les paramètres du port série et d'autres détails en fonction de votre configuration réelle. Ce code peut être un outil précieux pour mesurer la cadence de pagayage dans des sports nautiques tels que le kayak et le canoë.
