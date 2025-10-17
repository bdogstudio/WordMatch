# Word Match - Web Version

A fast-paced web game where players decide whether adjectives describe given items within a time limit.

## 🚀 Quick Start (Ubuntu/Linux)

### 1. Install Python and Flask
```bash
cd web-app
pip3 install -r requirements.txt
```

### 2. Run the server
```bash
python3 app.py
```

### 3. Access the game
- **Local**: http://localhost:5001
- **Network**: http://assman:5001 or http://192.168.1.161:5001

## 🎮 How to Play

1. Select an **adjective** (Fast, Slow, Big, etc.)
2. Choose a **category** (Animals, Cities, Foods, etc.)
3. Click **START**
4. Decide if the adjective describes each item - **YES** or **NO**
5. Beat the 10-second timer for each question!
6. Complete 10 questions and see your score

## 📱 Features

- **Responsive Design** - Works on mobile, tablet, and desktop
- **Touch Optimized** - Large buttons for easy tapping
- **Real-time Timer** - 10 seconds per question with progress bar
- **Score Tracking** - 100 points per answer
- **6 Categories** - Animals, Cities, Foods, Objects, People, Places
- **20 Adjectives** - Fast, Slow, Big, Small, Hot, Cold, and more

## 🏗️ Project Structure

```
web-app/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Single-page game (HTML/CSS/JS)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Configuration

### Change Port
Edit `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Add More Game Data
Edit the `ADJECTIVES` and `CATEGORIES` dictionaries in `app.py`.

## 🌐 Production Deployment

### Option 1: Screen/tmux
```bash
screen -S wordmatch
python3 app.py
# Press Ctrl+A, then D to detach
```

### Option 2: Systemd Service
Create `/etc/systemd/system/wordmatch.service`:
```ini
[Unit]
Description=Word Match Game
After=network.target

[Service]
User=your-username
WorkingDirectory=/path/to/web-app
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable wordmatch
sudo systemctl start wordmatch
```

## 🎨 Design

- **Color Scheme**: Coral red (#FF6B6B) to turquoise (#4ECDC4) gradient
- **Typography**: System fonts, bold weights for impact
- **UI Style**: Glass-morphism, large tap targets
- **Mobile-First**: Optimized for phones and tablets

## 📄 License

This project is provided as-is for educational and entertainment purposes.

---

Built with Flask + Vanilla JS ❤️
