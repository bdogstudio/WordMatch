import SwiftUI

struct ResultsView: View {
    let score: Int
    let total: Int
    let onPlayAgain: () -> Void

    var percentage: Int {
        guard total > 0 else { return 0 }
        return Int((Double(score) / Double(total * 100)) * 100)
    }

    var body: some View {
        VStack(spacing: 40) {
            Spacer()

            // Title
            Text("GAME OVER")
                .font(.system(size: 48, weight: .black))
                .foregroundColor(.white)

            // Score Display
            VStack(spacing: 20) {
                Text("\(score)")
                    .font(.system(size: 80, weight: .black))
                    .foregroundColor(.white)

                Text("POINTS")
                    .font(.system(size: 24, weight: .bold))
                    .foregroundColor(.white.opacity(0.8))

                // Stats
                VStack(spacing: 12) {
                    StatRow(label: "Questions", value: "\(total)")
                    StatRow(label: "Accuracy", value: "\(percentage)%")
                }
                .padding(25)
                .background(Color.white.opacity(0.2))
                .cornerRadius(20)
            }

            Spacer()

            // Play Again Button
            Button(action: onPlayAgain) {
                HStack(spacing: 12) {
                    Image(systemName: "arrow.clockwise")
                        .font(.system(size: 24, weight: .bold))

                    Text("PLAY AGAIN")
                        .font(.system(size: 28, weight: .black))
                }
                .foregroundColor(Color(hex: "4ECDC4"))
                .frame(maxWidth: .infinity)
                .frame(height: 70)
                .background(Color.white)
                .cornerRadius(35)
            }
            .padding(.horizontal, 30)
            .padding(.bottom, 40)
        }
    }
}

struct StatRow: View {
    let label: String
    let value: String

    var body: some View {
        HStack {
            Text(label)
                .font(.system(size: 18, weight: .medium))
                .foregroundColor(.white.opacity(0.9))

            Spacer()

            Text(value)
                .font(.system(size: 18, weight: .bold))
                .foregroundColor(.white)
        }
    }
}
