import SwiftUI

struct ContentView: View {
    @State private var gameState: GameState = .setup
    @State private var selectedAdjective: Adjective?
    @State private var selectedCategory: GameCategory?
    @State private var score: Int = 0
    @State private var totalQuestions: Int = 0

    enum GameState {
        case setup
        case playing
        case results
    }

    var body: some View {
        ZStack {
            // Background gradient
            LinearGradient(
                colors: [Color(hex: "FF6B6B"), Color(hex: "4ECDC4")],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            // Content
            switch gameState {
            case .setup:
                SetupView(
                    selectedAdjective: $selectedAdjective,
                    selectedCategory: $selectedCategory,
                    onStart: startGame
                )
            case .playing:
                if let adjective = selectedAdjective, let category = selectedCategory {
                    GameView(
                        adjective: adjective,
                        category: category,
                        score: $score,
                        totalQuestions: $totalQuestions,
                        onGameEnd: endGame
                    )
                }
            case .results:
                ResultsView(
                    score: score,
                    total: totalQuestions,
                    onPlayAgain: resetGame
                )
            }
        }
    }

    private func startGame() {
        score = 0
        totalQuestions = 0
        gameState = .playing
    }

    private func endGame() {
        gameState = .results
    }

    private func resetGame() {
        selectedAdjective = nil
        selectedCategory = nil
        score = 0
        totalQuestions = 0
        gameState = .setup
    }
}

// MARK: - Color Extension

extension Color {
    init(hex: String) {
        let scanner = Scanner(string: hex)
        var rgbValue: UInt64 = 0
        scanner.scanHexInt64(&rgbValue)

        let r = Double((rgbValue & 0xFF0000) >> 16) / 255.0
        let g = Double((rgbValue & 0x00FF00) >> 8) / 255.0
        let b = Double(rgbValue & 0x0000FF) / 255.0

        self.init(red: r, green: g, blue: b)
    }
}
