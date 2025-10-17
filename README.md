# Word Match - iOS Game

A fast-paced iOS game inspired by charades where players decide whether an adjective describes a given person, place, or thing within a time limit.

## 🎮 How to Play

1. **Select an Adjective** - Choose from 20 different adjectives (Fast, Slow, Big, Small, Hot, Cold, etc.)
2. **Choose a Category** - Pick from Animals, Cities, Foods, Objects, People, or Places
3. **Start Playing** - You'll be shown an item from your category and must decide if the adjective describes it
4. **Beat the Clock** - Each question has a 10-second timer
5. **Score Points** - Answer 10 questions and see your final score!

## 🎨 Features

- **Bold, Charades-Style Design** - Large text, vibrant colors, and clear UI
- **6 Categories** - Animals, Cities, Foods, Objects, People, Places
- **20 Adjectives** - Fast, Slow, Big, Small, Hot, Cold, and more
- **Timed Gameplay** - 10 seconds per question
- **Score Tracking** - 100 points per correct answer
- **Smooth Animations** - SwiftUI animations for feedback and transitions

## 📱 Requirements

- iOS 16.0 or later
- Xcode 14.0 or later
- Swift 5.0 or later

## 🚀 Getting Started

1. Open `AdjectiveGame.xcodeproj` in Xcode
2. Select your target device (iPhone or iPad)
3. Press ⌘R to build and run

## 🏗️ Project Structure

```
AdjectiveGame/
├── AdjectiveGameApp.swift    # Main app entry point
├── ContentView.swift          # Navigation and state management
├── GameData.swift            # Data models and game content
├── SetupView.swift           # Adjective and category selection
├── GameView.swift            # Main gameplay screen
├── ResultsView.swift         # Score and results display
└── Assets.xcassets           # App assets and icons
```

## 🎯 Game Mechanics

- **Questions**: 10 per game
- **Time Limit**: 10 seconds per question
- **Scoring**: 100 points per correct answer
- **No Repeats**: Items won't repeat within the same game session

## 🎨 Design Philosophy

The game follows a **charades-inspired design**:
- Bold, high-contrast colors (coral red and turquoise gradient)
- Large, readable text (no small fonts)
- Minimal UI elements (focus on gameplay)
- Fast-paced interaction (10s timer)
- Clear feedback (animations and visual cues)

## 🔧 Customization

### Adding More Adjectives
Edit `GameData.swift` and add to the `adjectives` array:
```swift
Adjective(word: "Your Adjective")
```

### Adding More Categories
Edit `GameData.swift` and add to the `categories` array:
```swift
GameCategory(name: "Category Name", items: [
    "Item 1", "Item 2", "Item 3", ...
])
```

### Adjusting Gameplay
In `GameView.swift`, modify:
- `maxQuestions` - Number of questions per game (default: 10)
- `timeLimit` - Seconds per question (default: 10.0)
- Score values in `handleAnswer()` function

## 📄 License

This project is provided as-is for educational and entertainment purposes.

---

Built with SwiftUI ❤️
