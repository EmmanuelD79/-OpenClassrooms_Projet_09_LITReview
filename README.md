Projet 9 - Formation OpenClassRooms Python

Réalisation d'une application web avec Django ayant pour but de commercialiser un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

L'application contient un module d'inscription et de connexion.

Les utilisateurs connectés peuvent :
<ul>
<li>Demander des critiques de livres et des articles grâce à la création de ticket;</li>
<li>Publier des critiques de livres et des articles;</li>
<li>Suivre plusieurs utilisateurs avec la possibilité de saisir le nom de l'utilisateur qu'il souhaite suivre;</li>
<li>Accéder à un flux contenant les tickets et avis de tous les utilisateurs qu'il suit;</li>
<li>Voir dans son flux ses propres tickets et avis ainsi les réponses des autres utilisateurs;</li>
<li>Modifier ou supprimer les tickets;</li>
<li>Ne plus suivre des utilisateurs.</li>
</ul>

Vous pouvez accéder à l'application en :

clonant le projet à l'aide de votre terminal en tapant la commande :
<br> 

```

https://github.com/EmmanuelD79/OpenClassrooms_Projet_09_LITReview.git

```


Pour l'execution , vous devez aller dans le répertoire du projet et taper la commande:
	<br> 
```
	
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
	
```
