# 📅 YouTube - Downloader by SoloZambously

Une API simple et rapide pour rechercher et télécharger des vidéos YouTube en **audio (MP3/M4A)** ou en **vidéo (MP4)** avec une interface web intégrée.  

---

## ✨ Fonctionnalités

- 🔍 Recherche de vidéos par mot-clé
- 📥 Téléchargement audio (MP3, M4A)
- 📺 Téléchargement vidéo (MP4)
- ⚡ Serveur léger avec Flask + envoi automatique du fichier
- 🎨 UI responsive et animée (CDN TailwindCSS)

---

## ⚙️ Prérequis

- 🐍 Python **3.9+**
- 🐳 Docker *(optionnel mais recommandé)*
- 🎮 ffmpeg *(installé automatiquement via Docker ou à installer manuellement)*

---

## 🚀 Installation

### ✅ Option 1 : Exécution locale

```bash
git clone https://github.com/solozambously/VideoYoutubeDownloader.git
cd VideoYoutubeDownloader
pip install -r requirements.txt
python app.py
```

⚠️ N'oubliez pas d'avoir `ffmpeg` installé sur votre système.

### 🐳 Option 2 : Exécution avec Docker

```bash
docker-compose build
docker-compose up
```

L'application sera disponible sur [http://localhost:5500](http://localhost:5500) 🌐

> L'API est disponible aussi sur https://szdev.engineer/api-ytdownload/(endpoint)

---

## 📱 Utilisation de l'API

### 🔌 API - Routes Flask

| Méthode | Endpoint                | Description                     |
|---------|-------------------------|---------------------------------|
| GET     | `/ping`                | Vérifie que le serveur fonctionne |
| POST    | `/search_video`        | Recherche de vidéos YouTube      |
| POST    | `/download_audio_mp3`  | Télécharge audio en `.mp3`       |
| POST    | `/download_audio_m4a`  | Télécharge audio en `.m4a`       |
| POST    | `/download_video`      | Télécharge vidéo en `.mp4`       |


---

## 🤝 Contribution

Les contributions sont les bienvenues !  
Pour proposer une fonctionnalité ou corriger un bug :
- Ouvrez une **issue**
- Ou soumettez une **pull request**

---

## 🧑‍💻 Auteur

Développé par Solal Bouzanquet

✉️ zambouslysolo@gmail.com
🌐 szdev.engineer

---

## 🔒 Licence

Ce projet est sous licence MIT.
Consulte le fichier LICENSE pour plus de détails.

---

## 🌐 Hébergement du projet

L'API est hébergée sur mon serveur et accessible à l'adresse suivante : https://szdev.engineer/api-ytdownload/(endpoint)

Vous pouvez tester le projet sur ce site : [https://szdev.engineer/yt/](https://szdev.engineer/yt/)

Ce dépôt GitHub a pour but de présenter le projet et de fournir les instructions nécessaires pour l'utiliser ou l'héberger vous-même.
