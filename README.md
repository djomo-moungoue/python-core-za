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

### 001 - Two Sum - Deux sommes
Étant donné un tableau d'entiers, renvoyer les indices des deux nombres tels que leur somme atteigne une cible 
spécifique. <br/>
Vous pouvez supposer que chaque entrée aura exactement une solution.

### 007 Reverse Integer - Entier inversé
Inverse les chiffres d'un nombre entier. <br/>
Exemple 1 : x = 123, renvoie 321 <br/>
Exemple 2 : x = -123, renvoie -321 <br/>

### 009 Palindrome Number - Déterminer le palindrome
Déterminez si un nombre entier est un palindrome. Faites-le sans espace supplémentaire. <br/>
Exemple 1: 1 renvoie True <br/>
Exemple 2: 1111 renvoie True <br/>
Exemple 3: 13731 renvoie True <br/>
Exemple 4: 123 renvoie False <br/>

### 013 Roman to Integer - De Romain à Entier
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

### 014 Longest Common Prefix - Préfixe commun le plus long
Écrivez une fonction pour trouver le préfixe commun le plus long parmi un tableau de chaînes de caractères.

### Exemple 1: 
['django', 'python', 'exit', 'framework'] renvoie ''

#### Exemple 2: 
['papaye', 'python', 'papa', 'pater'] renvoie 'p'

#### Exemple 3: 
['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'


### 020 Valid Parentheses - Valid Parentheses
Étant donné une chaîne s contenant uniquement les caractères '(', ')', '{', '}', '[' et ']', déterminez si la
chaîne d'entrée est valide. <br/>
Une chaîne d'entrée est valide si : <br/>
Les parenthèses ouvertes doivent être fermées par le même type de parenthèses. <br/>
Les parenthèses ouvertes doivent être fermées dans le bon ordre.

#### Exemple 1 : 
Entrée : s = "()" <br/>
Sortie : true

#### Exemple 2 :
Entrée : s = "()[]{}" <br/>
Sortie : true

#### Exemple 3 :
Entrée : s = "(]" <br/>
Sortie : false

#### Contraintes :
1 <= s.length <= 104 <br/>
s se compose uniquement de parenthèses '()[]{}'.

### 021 Merge Two Sorted Lists - Fusionner deux listes triées
On vous donne les têtes de deux listes chaînées triées, list1 et list2. <br/>
Fusionnez les deux listes en une seule liste triée. La liste doit être faite en épissant les noeuds des deux premières 
listes. <br/>
Retournez la tête de la liste fusionnée.

#### Exemple 1 :
Entrée : liste1 = [1,2,4], liste2 = [1,3,4]. <br/>
Sortie : [1,1,2,3,4,4]

#### Exemple 2 :
Entrée : list1 = [], list2 = [] <br/>
Sortie : []

#### Exemple 3 :
Entrée : list1 = [], list2 = [0] <br/>
Sortie : [0]

#### Contraintes :
Le nombre de nœuds dans les deux listes est compris dans l'intervalle [0, 50]. <br/>
-100 <= Node.val <= 100 <br/>
La liste1 et la liste2 sont triées dans un ordre non décroissant.

### 026 Remove Duplicates from Sorted Array - Suppression des doublons dans un tableau trié
Étant donné un tableau d'entiers nums triés par ordre non décroissant, supprimez les doublons en place de sorte que 
chaque élément unique n'apparaisse qu'une seule fois. L'ordre relatif des éléments doit rester le même. <br/>
Comme il est impossible de modifier la longueur du tableau dans certains langages, il faut plutôt faire en sorte que 
le résultat soit placé dans la première partie du tableau nums. Plus formellement, s'il reste k éléments après avoir 
supprimé les doublons, alors les k premiers éléments de nums doivent contenir le résultat final. Ce que vous laissez 
au-delà des k premiers éléments n'a pas d'importance. <br/>
Retournez k après avoir placé le résultat final dans les k premiers emplacements de nums. <br/>
N'allouez pas d'espace supplémentaire pour un autre tableau. Vous devez le faire en modifiant le tableau d'entrée en 
place avec O(1) de mémoire supplémentaire.

#### Juge personnalisé :
Le juge testera votre solution avec le code suivant :

int[] nums = [...] ; // Tableau d'entrée <br/>
int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte <br/>
int k = removeDuplicates(nums) ; // Appelle votre implémentation <br/>
assert k == expectedNums.length ; <br/>
for (int i = 0 ; i < k ; i++) { <br/>
assert nums[i] == expectedNums[i] ; <br/>
} <br/>
Si toutes les assertions passent, alors votre solution sera acceptée.

#### Exemple 1 :
Entrée : nums = [1,1,2] <br/>
Sortie : 2, nums = [1,2,_] <br/>
Explication :  <br/>
Votre fonction doit retourner k = 2, les deux premiers éléments de nums étant respectivement 1 et 2. <br/>
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Exemple 2 :
Entrée : nums = [0,0,1,1,1,2,2,3,3,4] <br/>
Sortie : 5, nums = [0,1,2,3,4,,,,,_] <br/>
Explication :  <br/>
Votre fonction devrait renvoyer k = 5, les cinq premiers éléments de nums étant respectivement 0, 1, 2, 3 et 4. <br/>
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Contraintes :
1 <= nums.length <= 3 * 104 <br/>
-100 <= nums[i] <= 100 <br/>
nums est trié dans un ordre non décroissant.

### 027 Remove Element - Supprimer un élément

Étant donné un tableau de nombres entiers et un nombre entier val, supprime toutes les occurrences de val dans nums en 
place. L'ordre relatif des éléments peut être modifié. <br/>
Comme il est impossible de modifier la longueur du tableau dans certains langages, il faut plutôt faire en sorte que 
le résultat soit placé dans la première partie du tableau nums. Plus formellement, s'il reste k éléments après avoir 
supprimé les doublons, alors les k premiers éléments de nums doivent contenir le résultat final. Ce que vous laissez 
au-delà des k premiers éléments n'a pas d'importance.

Retournez k après avoir placé le résultat final dans les k premiers emplacements de nums.

N'allouez pas d'espace supplémentaire pour un autre tableau. Vous devez le faire en modifiant le tableau d'entrée en 
place avec O(1) de mémoire supplémentaire.

#### Juge personnalisé :

Le juge testera votre solution avec le code suivant :

int[] nums = [...] ; // Tableau d'entrée <br/>
int val = ... ; // Valeur à supprimer <br/>
int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte. <br/>
// Elle est triée et aucune valeur n'est égale à val.

int k = removeElement(nums, val) ; // Appelle votre implémentation

assert k == expectedNums.length ; <br/>
sort(nums, 0, k) ; // Trie les k premiers éléments de nums <br/>
for (int i = 0 ; i < actualLength ; i++) { <br/>
assert nums[i] == expectedNums[i] ; <br/>
} <br/>
Si toutes les assertions passent, alors votre solution sera acceptée.

#### Exemple 1 :
Entrée : nums = [3,2,2,3], val = 3 <br/>
Sortie : 2, nums = [2,2,,] <br/>
Explication :  <br/>
Votre fonction doit renvoyer k = 2, les deux premiers éléments de nums étant 2. <br/>
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Exemple 2 :
Entrée : nums = [0,1,2,2,3,0,4,2], val = 2 <br/>
Sortie : 5, nums = [0,1,4,0,3,,,_] <br/>
Explication :  <br/>
Votre fonction devrait retourner k = 5, avec les cinq premiers éléments de nums contenant 0, 0, 1, 3, et 4. <br/>
Notez que les cinq éléments peuvent être retournés dans n'importe quel ordre. <br/>
Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).

#### Contraintes :
0 <= nums.length <= 100 <br/>
0 <= nums[i] <= 50 <br/>
0 <= val <= 100

### 028 Implement strStr() - Implémenter strStr()
Étant donné deux chaînes de caractères, aiguille et botte de foin, retourne l'indice de la première occurrence 
d'aiguille dans botte de foin, ou -1 si aiguille ne fait pas partie de botte de foin.

Clarification : <br/>
Que devrions-nous retourner si aiguille est une chaîne vide ? C'est une excellente question à poser lors d'un entretien.

Pour les besoins de ce problème, nous renverrons 0 lorsque aiguille est une chaîne vide. Ceci est cohérent avec strstr() 
en C et indexOf() en Java.

#### Exemple 1 :
Entrée : botte de foin = "hello", aiguille = "ll".
Sortie : 2

#### Exemple 2 :
Entrée : botte de foin = "aaaaa", aiguille = "bba".
Résultat : -1

#### Contraintes :
1 <= botte de foin.longueur, aiguille.longueur <= 104 <br/>
La meule de foin et l'aiguille ne sont constituées que de caractères anglais minuscules.

---

### 035 Search Insert Position - Cherche la position d'insertion
Étant donné un tableau trié d'entiers distincts et une valeur cible, retournez l'index si la cible est trouvée. Si ce 
n'est pas le cas, renvoyez l'indice où il se trouverait s'il était inséré dans l'ordre. <br/>
Vous devez écrire un algorithme dont la complexité d'exécution est de O(log n).

#### Exemple 1 :
Entrée : nums = [1,3,5,6], cible = 5 <br/>
Sortie : 2

#### Exemple 2 : 
Entrée : nums = [1,3,5,6], cible = 2 <br/>
Sortie : 1

#### Exemple 3 :
Entrée : nums = [1,3,5,6], cible = 7 <br/>
Sortie : 4

#### Contraintes :
1 <= nums.length <= 104 <br/>
-104 <= nums[i] <= 104 <br/>
nums contient des valeurs distinctes triées par ordre croissant. <br/>
-104 <= cible <= 104

### 053 Maximum Subarray - Sous-tableau maximum
Étant donné un tableau de nombres entiers, trouvez le sous-groupe contigu (contenant au moins un nombre) qui a la plus 
grande somme et renvoyez sa somme.

Un sous-groupe est une partie contiguë d'un tableau.

#### Exemple 1 :
Entrée : nums = [-2,1,-3,4,-1,2,1,-5,4] <br/>
Sortie : 6 <br/>
Explication : [4,-1,2,1] a la plus grande somme = 6.

#### Exemple 2 : 
Entrée : nums = [1] <br/>
Sortie : 1

#### Exemple 3 : 
Entrée : nums = [5,4,-1,7,8] <br/>
Sortie : 23
 
#### Contraintes : 
1 <= nums.length <= 105 <br/>
-104 <= nums[i] <= 104
 
Suivi : Si vous avez compris la solution O(n), essayez de coder une autre solution en utilisant l'approche diviser pour 
régner, qui est plus subtile.

### 038 Count and Say - Compter et Dire
La séquence count-and-say est une séquence de chaînes de chiffres définie par la formule récursive :
    
countAndSay(1) = "1" <br/>
countAndSay(n) est la façon dont vous "dites" la chaîne de chiffres de countAndSay(n-1), qui est ensuite convertie en 
une chaîne de chiffres différente. <br/>
Pour déterminer la façon dont vous "dites" une chaîne de chiffres, divisez-la en un nombre minimal de sous-chaînes de 
sorte que chaque sous-chaîne contienne exactement un chiffre unique. Ensuite, pour chaque sous-chaîne, dites le nombre 
de chiffres, puis dites le chiffre. Enfin, concaténer chaque chiffre. <br/>

Par exemple, l'énoncé et la conversion pour la chaîne de chiffres "3322251" :

Étant donné un nombre entier positif n, retourner le nième terme de la séquence de comptage et de conversion.

#### Exemple 1 : 
Entrée : n = 1 <br/>
Sortie : "1" <br/>
Explication : C'est le cas de base.

#### Exemple 2 : 
Entrée : n = 4 <br/>
Sortie : "1211" <br/>
Explication : <br/>
countAndSay(1) = "1" (compte et dit) <br/>
countAndSay(2) = dites "1" = un 1 = "11" <br/>
countAndSay(3) = dites "11" = deux 1 = "21" <br/>
Comptez et dites(4) = dites "21" = un 2 + un 1 = "12" + "11" = "1211".

#### Exemple 3 :
Entrée : n = 5 <br/>
Sortie : "111221" <br/>
Explication : <br/>
countAndSay(1) = "1" (compte et dit) <br/>
countAndSay(2) = dites "1" = un 1 = "11" <br/>
countAndSay(3) = dites "11" = deux 1 = "21" <br/>
Comptez et dites(4) = dites "21" = un 2 + un 1 = "12" + "11" = "1211". <br/>
Comptez et dites(5) = dites "1211" = 1 un + un 2 + deux 1 = "11" + "12" + "21" = "111221".

#### Contraintes : 
1 <= n <= 30


---

## Problèmes à difficulté moyenne

---

## Problèmes difficiles

