# PythonCore - Problèmes déjà résolus

## Tâches
- Résolvez chaque de telle sorte que la complexité d'exécution et d'espace de votre solution
soit optimale.
- Déterminez la complexité d'exécution.
- Déterminez la complexité d'espace.

**Convention** concernant le **nom de branche** de chaque **nouvelle fonctionnalité** à implémenter :
+ solution_easy-id # id est l'id du problème
+ solution_medium-id
+ solution_hard-id

## Problèmes faciles

### 001 - Deux sommes
Étant donné un tableau d'entiers, renvoyer les indices des deux nombres tels que leur somme atteigne une cible 
spécifique. <br/>
Vous pouvez supposer que chaque entrée aura exactement une solution.

### 007 Entier inversé
Inverse les chiffres d'un nombre entier. <br/>
Exemple 1 : x = 123, renvoie 321 <br/>
Exemple 2 : x = -123, renvoie -321 <br/>

### 009 Déterminer le palindrome
Déterminez si un nombre entier est un palindrome. Faites-le sans espace supplémentaire.
Exemple 1: 1 renvoie True <br/>
Exemple 2: 1111 renvoie True <br/>
Exemple 3: 13731 renvoie True <br/>
Exemple 4: 123 renvoie False <br/>

### 013 De Romain à Entier
Étant donné un chiffre romain, convertissez-le en un nombre entier. <br/>
L'entrée est garantie dans l'intervalle de 1 à 3999. <br/>
Exemple 1: I renvoie 1 <br/>
Exemple 2: V renvoie 5 <br/>
Exemple 3: X renvoie 10 <br/>
Exemple 4: L renvoie 50 <br/>
Exemple 5: C renvoie 100 <br/>
Exemple 6: D renvoie 500 <br/>
Exemple 7: M renvoie 1000 <br/>
Exemple 8: III renvoie 3 <br/>
Exemple 9: IV renvoie 4 <br/>
Exemple 10: MCMLXXXVIII renvoie 1988 <br/>
Exemple 11: MMXXII renvoie 2022 <br/>
Exemple 12: MMMCMXCIX renvoie 3999 <br/>

### 014 Préfixe commun le plus long
Écrivez une fonction pour trouver le préfixe commun le plus long parmi un tableau de chaînes de caractères.
Exemple 1: ['django', 'python', 'exit', 'framework'] renvoie ''
Exemple 2: ['papaye', 'python', 'papa', 'pater'] renvoie 'p'
Exemple 3: ['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'


### 020 Valid Parentheses
Étant donné une chaîne s contenant uniquement les caractères '(', ')', '{', '}', '[' et ']', déterminez si la
chaîne d'entrée est valide.
Une chaîne d'entrée est valide si :
Les parenthèses ouvertes doivent être fermées par le même type de parenthèses.
Les parenthèses ouvertes doivent être fermées dans le bon ordre.

Exemple 1 : <br/>
Entrée : s = "()"
Sortie : true

Exemple 2 : <br/>
Entrée : s = "()[]{}"
Sortie : true

Exemple 3 : <br/>
Entrée : s = "(]"
Sortie : false

Contraintes : <br/>
1 <= s.length <= 104
s se compose uniquement de parenthèses '()[]{}'.

### 021 Fusionner deux listes triées
On vous donne les têtes de deux listes chaînées triées, list1 et list2.
Fusionnez les deux listes en une seule liste triée. La liste doit être faite en épissant les noeuds des deux premières listes.
Retournez la tête de la liste fusionnée.

Exemple 1 :
Entrée : liste1 = [1,2,4], liste2 = [1,3,4].
Sortie : [1,1,2,3,4,4]

Exemple 2 :
Entrée : list1 = [], list2 = []
Sortie : []

Exemple 3 :
Entrée : list1 = [], list2 = [0]
Sortie : [0]

Contraintes :
Le nombre de nœuds dans les deux listes est compris dans l'intervalle [0, 50].
-100 <= Node.val <= 100
La liste1 et la liste2 sont triées dans un ordre non décroissant.

### 026 Suppression des doublons dans un tableau trié
Étant donné un tableau d'entiers nums triés par ordre non décroissant, supprimez les doublons en place de sorte que chaque élément unique n'apparaisse qu'une seule fois. L'ordre relatif des éléments doit rester le même.
Comme il est impossible de modifier la longueur du tableau dans certains langages, il faut plutôt faire en sorte que le résultat soit placé dans la première partie du tableau nums. Plus formellement, s'il reste k éléments après avoir supprimé les doublons, alors les k premiers éléments de nums doivent contenir le résultat final. Ce que vous laissez au-delà des k premiers éléments n'a pas d'importance.
Retournez k après avoir placé le résultat final dans les k premiers emplacements de nums.
N'allouez pas d'espace supplémentaire pour un autre tableau. Vous devez le faire en modifiant le tableau d'entrée en place avec O(1) de mémoire supplémentaire.

Juge personnalisé :
Le juge testera votre solution avec le code suivant :
int[] nums = [...] ; // Tableau d'entrée
int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte
int k = removeDuplicates(nums) ; // Appelle votre implémentation
assert k == expectedNums.length ;
for (int i = 0 ; i < k ; i++) {
assert nums[i] == expectedNums[i] ;
}
Si toutes les assertions passent, alors votre solution sera acceptée.

#### Exemple 1 :
Entrée : nums = [1,1,2]
Sortie : 2, nums = [1,2,_]
Explication : Votre fonction doit retourner k = 2, les deux premiers éléments de nums étant respectivement 1 et 2.
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Exemple 2 :
Entrée : nums = [0,0,1,1,1,2,2,3,3,4]
Sortie : 5, nums = [0,1,2,3,4,,,,,_]
Explication : Votre fonction devrait renvoyer k = 5, les cinq premiers éléments de nums étant respectivement 0, 1, 2, 3 et 4.
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Contraintes :
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums est trié dans un ordre non décroissant.

### 027 Remove Element - Supprimer un élément

Étant donné un tableau de nombres entiers et un nombre entier val, supprime toutes les occurrences de val dans nums en 
place. L'ordre relatif des éléments peut être modifié.
Comme il est impossible de modifier la longueur du tableau dans certains langages, il faut plutôt faire en sorte que 
le résultat soit placé dans la première partie du tableau nums. Plus formellement, s'il reste k éléments après avoir 
supprimé les doublons, alors les k premiers éléments de nums doivent contenir le résultat final. Ce que vous laissez 
au-delà des k premiers éléments n'a pas d'importance.

Retournez k après avoir placé le résultat final dans les k premiers emplacements de nums.

N'allouez pas d'espace supplémentaire pour un autre tableau. Vous devez le faire en modifiant le tableau d'entrée en 
place avec O(1) de mémoire supplémentaire.

Juge personnalisé :

Le juge testera votre solution avec le code suivant :

int[] nums = [...] ; // Tableau d'entrée
int val = ... ; // Valeur à supprimer
int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte.
// Elle est triée et aucune valeur n'est égale à val.

int k = removeElement(nums, val) ; // Appelle votre implémentation

assert k == expectedNums.length ;
sort(nums, 0, k) ; // Trie les k premiers éléments de nums
for (int i = 0 ; i < actualLength ; i++) {
assert nums[i] == expectedNums[i] ;
}
Si toutes les assertions passent, alors votre solution sera acceptée.

#### Exemple 1 :
Entrée : nums = [3,2,2,3], val = 3
Sortie : 2, nums = [2,2,,]
Explication : Votre fonction doit renvoyer k = 2, les deux premiers éléments de nums étant 2.
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Exemple 2 :
Entrée : nums = [0,1,2,2,3,0,4,2], val = 2
Sortie : 5, nums = [0,1,4,0,3,,,_]
Explication : Votre fonction devrait retourner k = 5, avec les cinq premiers éléments de nums contenant 0, 0, 1, 3, et 4.
Notez que les cinq éléments peuvent être retournés dans n'importe quel ordre.
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Contraintes :
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

---

## Problèmes à difficulté moyenne

---

## Problèmes difficiles

