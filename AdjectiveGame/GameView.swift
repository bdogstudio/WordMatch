import SwiftUI

struct GameView: View {
    let adjective: Adjective
    let category: GameCategory
    @Binding var score: Int
    @Binding var totalQuestions: Int
    let onGameEnd: () -> Void

    @State private var currentItem: String = ""
    @State private var timeRemaining: Double = 10.0
    @State private var questionsAnswered: Int = 0
    @State private var isAnswering: Bool = false
    @State private var showFeedback: Bool = false
    @State private var lastAnswerCorrect: Bool = false
    @State private var usedItems: Set<String> = []

    let timer = Timer.publish(every: 0.1, on: .main, in: .common).autoconnect()
    let maxQuestions = 10
    let timeLimit = 10.0

    var body: some View {
        VStack(spacing: 0) {
            // Header
            VStack(spacing: 15) {
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("QUESTION \(questionsAnswered + 1)/\(maxQuestions)")
                            .font(.system(size: 14, weight: .bold))
                            .foregroundColor(.white.opacity(0.8))

                        Text("Score: \(score)")
                            .font(.system(size: 20, weight: .black))
                            .foregroundColor(.white)
                    }

                    Spacer()

                    VStack(alignment: .trailing, spacing: 4) {
                        Text("TIME")
                            .font(.system(size: 14, weight: .bold))
                            .foregroundColor(.white.opacity(0.8))

                        Text("\(Int(timeRemaining))s")
                            .font(.system(size: 20, weight: .black))
                            .foregroundColor(.white)
                    }
                }

                // Progress Bar
                GeometryReader { geometry in
                    ZStack(alignment: .leading) {
                        Rectangle()
                            .fill(Color.white.opacity(0.3))

                        Rectangle()
                            .fill(Color.white)
                            .frame(width: geometry.size.width * (timeRemaining / timeLimit))
                    }
                }
                .frame(height: 8)
                .cornerRadius(4)
            }
            .padding(30)

            Spacer()

            // Question Display
            VStack(spacing: 30) {
                // Adjective
                VStack(spacing: 10) {
                    Text("Is this...")
                        .font(.system(size: 24, weight: .medium))
                        .foregroundColor(.white.opacity(0.9))

                    Text(adjective.word.uppercased())
                        .font(.system(size: 48, weight: .black))
                        .foregroundColor(.white)
                        .padding(.horizontal, 40)
                        .padding(.vertical, 20)
                        .background(Color.white.opacity(0.2))
                        .cornerRadius(20)
                }

                // Item
                Text(currentItem)
                    .font(.system(size: 56, weight: .black))
                    .foregroundColor(.white)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 30)
                    .frame(minHeight: 150)
                    .scaleEffect(showFeedback ? 1.1 : 1.0)
                    .animation(.spring(response: 0.3), value: showFeedback)
            }

            Spacer()

            // Answer Buttons
            HStack(spacing: 20) {
                // NO Button
                Button(action: { handleAnswer(isYes: false) }) {
                    VStack(spacing: 8) {
                        Image(systemName: "xmark")
                            .font(.system(size: 40, weight: .bold))

                        Text("NO")
                            .font(.system(size: 24, weight: .black))
                    }
                    .foregroundColor(Color(hex: "FF6B6B"))
                    .frame(maxWidth: .infinity)
                    .frame(height: 140)
                    .background(Color.white)
                    .cornerRadius(25)
                }
                .disabled(isAnswering)

                // YES Button
                Button(action: { handleAnswer(isYes: true) }) {
                    VStack(spacing: 8) {
                        Image(systemName: "checkmark")
                            .font(.system(size: 40, weight: .bold))

                        Text("YES")
                            .font(.system(size: 24, weight: .black))
                    }
                    .foregroundColor(Color(hex: "4ECDC4"))
                    .frame(maxWidth: .infinity)
                    .frame(height: 140)
                    .background(Color.white)
                    .cornerRadius(25)
                }
                .disabled(isAnswering)
            }
            .padding(.horizontal, 30)
            .padding(.bottom, 40)
        }
        .onReceive(timer) { _ in
            if timeRemaining > 0 && !isAnswering {
                timeRemaining -= 0.1
            } else if timeRemaining <= 0 && !isAnswering {
                handleTimeout()
            }
        }
        .onAppear {
            nextQuestion()
        }
    }

    private func handleAnswer(isYes: Bool) {
        guard !isAnswering else { return }

        isAnswering = true
        showFeedback = true

        // For demo purposes, we'll accept the user's answer as correct
        // In a real game, you'd have logic to determine correctness
        lastAnswerCorrect = true
        score += 100

        totalQuestions += 1
        questionsAnswered += 1

        // Show feedback briefly
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            showFeedback = false

            if questionsAnswered >= maxQuestions {
                onGameEnd()
            } else {
                nextQuestion()
                isAnswering = false
            }
        }
    }

    private func handleTimeout() {
        isAnswering = true
        totalQuestions += 1
        questionsAnswered += 1

        if questionsAnswered >= maxQuestions {
            onGameEnd()
        } else {
            nextQuestion()
            isAnswering = false
        }
    }

    private func nextQuestion() {
        var availableItems = category.items.filter { !usedItems.contains($0) }

        if availableItems.isEmpty {
            usedItems.removeAll()
            availableItems = category.items
        }

        if let randomItem = availableItems.randomElement() {
            currentItem = randomItem
            usedItems.insert(randomItem)
        }

        timeRemaining = timeLimit
    }
}
