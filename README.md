# 🤖 Telegram Auto Messenger – Script Python d'Envoi Automatique de Messages sur Telegram

**Telegram Auto Messenger** est un script Python conçu pour **envoyer automatiquement des messages personnalisés de manière périodique** dans un **groupe** ou **canal Telegram**.

---

## 📌 Objectif du projet

Ce script permet :

- L'envoi de **messages programmés** à des heures définies (quotidiennement, hebdomadairement, etc.)
- La **personnalisation du message** (avec noms, dates, emojis, etc.)
- Le fonctionnement **24h/24 - 7j/7**, grâce à son hébergement sur la plateforme **[PythonAnywhere](https://www.pythonanywhere.com/)**

---

## ☁️ Hébergement & prérequis

Le script est **hébergé sur PythonAnywhere**. Pour un fonctionnement continu sans interruption :

> 💡 Il est **fortement recommandé** de souscrire au **forfait payant le plus bas** de PythonAnywhere (env. 5 $/mois) afin d'activer les **tâches programmées illimitées** et éviter les interruptions automatiques.

---

## 🛠️ Technologies utilisées

- 🐍 Python 3.x
- 📦 Bibliothèques :
  - `python-telegram-bot`
  - `apscheduler` (pour la planification)
  - `requests` ou `aiohttp` selon l'implémentation
- 🧠 Optionnel : gestion dynamique via un fichier `JSON` ou base de données SQLite

---
## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/noumedem237/yonkocross.git
cd yonkocross

## 2. Créer un environnement virtuel (facultatif mais recommandé)
 
 
```python3 -m venv venv
```source venv/bin/activate
## 3. Installer les dépendances
 
```pip install -r requirements.txt

## 🚀 Lancer le script localement
 
```python main.py
