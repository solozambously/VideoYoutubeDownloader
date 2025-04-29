# 📅 VideoYoutubeDownloader

**VideoYoutubeDownloader** est une application Python permettant de 👇 **télécharger des vidéos ou de l'audio depuis YouTube**.
Elle prend en charge les formats **MP4**, **M4A** et **MP3**, avec une **API REST** simple pour une intégration facile.

---

## ✨ Fonctionnalités

- 🎮 **Téléchargement de vidéos** YouTube dans leur meilleure qualité
- 🎵 **Téléchargement de l'audio** (format M4A ou conversion en MP3)
- 🔎 **Recherche de vidéos** par mots-clés
- 🐛 **API REST** pour interagir avec l'application

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

> ⌛ Une version accessible en ligne arrivera bientôt.

---

## 📱 Utilisation de l'API

### 🎥 Télécharger une vidéo
- **Endpoint** : `POST /download_video`
- **Paramètres** : `url` (URL YouTube)
- **Réponse** :
```json
{ "message": "Download started successfully" }
```

### 🎶 Télécharger l'audio
- **Endpoint** : `POST /download_audio`
- **Paramètres** : `url` (URL YouTube)
- **Réponse** :
```json
{ "message": "Download started successfully" }
```

### 🔍 Rechercher une vidéo
- **Endpoint** : `POST /search_video`
- **Paramètres** : `search` (mot-clé)
- **Réponse** :
```json
[
  {
    "title": "Example Video",
    "url": "https://youtube.com/watch?v=example",
    "duration": 300
  }
]
```

---

## 🤝 Contribution

Les contributions sont les bienvenues !  
Pour proposer une fonctionnalité ou corriger un bug :
- Ouvrez une **issue**
- Ou soumettez une **pull request**

---

## 📄 Auteur

Projet développé par **Solal Bouzanquet**.

---

## 🔒 Licence

Ce projet est sous licence MIT.
Consulte le fichier LICENSE pour plus de détails.

