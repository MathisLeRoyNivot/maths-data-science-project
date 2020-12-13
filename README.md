# Maths & Data Science
> ****
> **LE ROY-NIVOT** Mathis
> 
> Projet #4 : Marche aléatoire


## Les contantes

**4 contantes** sont modifiables par l'utilisateur et permettent de régler les paramètres du programme.

Les constantes disponibles sont les suivantes :

```python
INTERVAL = [-10, 10]  # L'intervalle sur lequel la marche aléatoire va fonctionner
NUM_EXPERIENCE = 50000  # Le nombre de fois que l'on souhaite exécuter l'expérience
NUM_OF_TRIPS = 30  # Le nombre de 'trajet' que doit faire le programme pour trouver sa position finale
INITIAL_POSITION = 0  # La position de départ (qui doit être comprise dans l'intervalle déclaré plus haut)
```

## Fonctions disponibles

Plusieurs fonctions sont implémentées et servent à alléger et à rendre plus propre la compréhension du programme.

Les fonctions disponibles sont les suivantes :

```python 
def get_interval_length(interval)
```
Cette fonction prend une liste de taille 2 en argument et permet de retourner le nombre de 'pas' que peut effectuer le curseur entre l'intervalle.

```python 
def generate_random_prob(interval)
```
Cette fonction va générer une chaîne de Markov basée sur l'intervalle renseigné en paramètre de la fonction.


```python 
def walk_simulation(initial_pos, interval, num_of_walks, probs)
```
Cette fonction est la "fonction principale" du programme et va permettre de réaliser la marche aléatoire. Cette focntion prend 4 paramètres :
- `initial_pos` qui est la position de départ de notre curseur
- `interval` qui est l'intervalle sur lequel le curseur doit se déplacer
- `num_of_walks` qui est le nombre de trajets que le curseur doit effectuer avant de s'arrêter
- `probs` qui est la chaîne de Markov


## Observation des résultats

Sur l'histogramme obtenu lors l'expérience, nous pouvons obsezrver une loi normale avec une tendance à tendre vers la borne maximale de notre intervalle.