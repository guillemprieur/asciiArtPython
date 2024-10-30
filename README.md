# Nouvelle version du  [programme Mika](https://fr.wikipedia.org/wiki/Art_ASCII)
## Introduction
N'avez-vous jamais rêvé de pouvoir afficher une **photographie** de Mika avec uniquement des **caractères** ? Et bien figurez-vous que selon une [étude](https://fr.wikipedia.org/wiki/Mensonge) effectuée sur une population presque significative, c'est le rêve absolu de plus de 50% des français !

C'est pourquoi, une équipe de développeurs nommé _les roues détachables_ s'est lancé dans ce projet aussi **passionnant** qu'**essentiel** pour toute l'humanité.
## Les fonctions principales
Ce programme se compose de plusieurs fonctions principales, en voici les détails :
### Fonction I :
La fonction **fromImages** permet de tranformer une image en une liste de chaine de caractère ascii, chaque éléments de la liste formant les lignes de l'image.

Cette fonction peut prendre de 1 à 2 arguments. Le premier (qui est obligatoire), doit être au format String et doit être le chemin d'accès au fichier image à transformer en ascii. Le deuxième (qui est facultatif et qui est par défaut égal à 250 000) permet de définir le nombre de caractères souhaité pour représenter l'image.

Voici un exemple d'utilisation de cette fonction :
```
import asciiArtPython as aap
asciiCaracListe = aap.fromImages("image.jpg", 100000)
```
### Fonction II :
La fonction **toImages** permet d'exporter des caractère formant de l'Art Ascii en un fichier au format png. Elle s'utilise parfaitement à la suite de la fonction **fromImages**.

Cette fonction peut prendre plusieurs arguments, voici les plus essentiels. L'argument (obligatoire) **liste** doit contenir une liste de chaine de caractère ascii (c'est elle qui sera exportée avec chaque éléments de la liste qui forment les lignes de l'image). L'argument **path** contient le chemin d'accès souhaité de l'image (cet argument est par défaut égal à "mika_export"). Enfin, l'argument **backgrColor** (par défaut réglé sur "white") doit être soit "white" soit "black". Dans le cas où celui-ci est réglé sur "black", la couleur des caractère et leur ordre sera inversé pour correspondre au fond de l'image.

Voici un exemple d'utilisation de cette fonction :
```
aap.toImages(liste=asciiCaracListe, path="ma_superbe_image", backgrColor="black")
```
### Fonction III :
La fonction **toTxt** permet d'exporter des caractère formant de l'Art Ascii en un fichier au format txt. Elle s'utilise parfaitement à la suite de la fonction **fromImages**.

Cette fonction peut prendre de 1 à 2 arguments. Le premier (qui est obligatoire), doit contenir une liste de chaine de caractère ascii (c'est elle qui sera exportée avec chaque éléments de la liste qui forment les lignes de l'image). Le deuxième (qui vaut par défaut "file.txt") est le nom du fichier dans lequel on souhaite exporter notre image (**attention** : bien mettre l'extension de fichier dans l'argument).

Voici un exemple d'utilisation de cette fonction :
```
aap.toTxt(asciiCaracListe,"mon_mika.txt")
```
### Fonction IV :
La fonction **printInTerminal** permet d'afficher des caractère formant de l'Art Ascii directement dans le terminal. Elle s'utilise parfaitement à la suite de la fonction fromImages.

Cette fonction ne prend que la liste en argument. **Attention** : cette fonction n'est pas équivalente à la fonction **print** par défaut de python, elle supprime une ligne sur deux pour ne pas déformer l'image.

Voici un exemple d'utilisation de cette fonction :

```
aap.printInTerminal(asciiCaracListe)
```
### Fonction V :
La fonction **fromAndToImages** équivaut simplement aux fonctions **fromImages** et **toImages** imbriqués l'une dans l'autre.
```
# Pour être plus clair, faire :
aap.toImages(aap.fromImages("mika.jpg"))
# Equivaut à faire :
aap.fromAndToImages("mika.jpg")
```
### Fonction VI et VII :
Les fonctions **fromAndToVideos** et **fromAndToVideosDark** créent, à partir de vidéos, une vidéo de caractères (soit en mode sombre, soit en mode clair). Mais comme un exemple vaut mieux que milles mots, je vous renvoie vers [cette vidéo](https://www.instagram.com/guill_prieur/reel/DAd2l_PN7bv/).
### Fonction VIII :
La focntion **liveFromWebcam** ne prend aucun argument mais permet de redécouvrir [votre visage](https://fr.wikipedia.org/wiki/Miroir) en Art Ascii à l'aide de votre propre webcam !
