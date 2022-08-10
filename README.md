Projet 9 - Formation OpenClassRooms Python

Réalisation d'une application web avec Django ayant pour but de commercialiser un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

L'application contient un module d'inscription et de connexion.

Les utilisateurs connectés peuvent :
<ul>
<li>Demander des critiques de livres et des articles grâce à la création de ticket;</li>
<li>Publier des critiques de livres et des articles;</li>
<li>Suivre plusieurs utilisateurs avec la possibilité de saisir le nom de l'utilisateur qu'ils souhaitent suivre;</li>
<li>Accéder à un flux contenant les tickets et avis de tous les utilisateurs qu'ils suivent;</li>
<li>Voir dans leur flux leurs propres tickets et avis ainsi les réponses des autres utilisateurs;</li>
<li>Modifier ou supprimer les tickets;</li>
<li>Ne plus suivre des utilisateurs.</li>
</ul>

Vous pouvez accéder à l'application en :

clonant le projet à l'aide de votre terminal en tapant la commande :
<br> 

```

https://github.com/EmmanuelD79/OpenClassrooms_Projet_09_LITReview.git

```

Pré-requis
créer un environnement virtuel à l'aide de votre terminal en tapant la commande:

```

python -m venv env

````

puis l'activer :
sur windows :

```

.\env\scripts\activate

```

sur mac et linux :

```

source env/bin/activate

```

Installation
Pour utiliser ce projet, il est nécessaire d'installer les modules du fichier requirements.txt.

Pour installer automatiquement ces modules, dans votre terminal, vous devez aller dans le dossier du projet et ensuite taper la commande suivante :
```

pip install -r requirements.txt

```

ou le faire manuellement en consultant le fichier requirements.txt en tapant sur votre terminal la commande :

```

cat requirements.txt

```

puis les installer un par un avec la commande :

```

pip install <nom du paquage>

```

Démarrage
Pour démarrer le projet, vous devez aller dans le répertoire du projet et taper sur votre terminal la commande:

<br> 
```
	
python manage.py migrate
python manage.py runserver
	
```

L'application web est disponible en local à l'adresse:  http://localhost:8000/
