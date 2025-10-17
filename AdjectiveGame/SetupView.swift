import SwiftUI

struct SetupView: View {
    @Binding var selectedAdjective: Adjective?
    @Binding var selectedCategory: GameCategory?
    let onStart: () -> Void

    var body: some View {
        VStack(spacing: 30) {
            // Title
            VStack(spacing: 10) {
                Text("WORD")
                    .font(.system(size: 60, weight: .black))
                    .foregroundColor(.white)

                Text("MATCH")
                    .font(.system(size: 60, weight: .black))
                    .foregroundColor(.white)
                    .offset(y: -20)
            }
            .padding(.top, 60)

            Spacer()

            // Selection Cards
            VStack(spacing: 20) {
                // Adjective Selection
                SelectionCard(
                    title: "ADJECTIVE",
                    selection: selectedAdjective?.word ?? "Choose",
                    options: GameData.adjectives.map { $0.word },
                    onSelect: { word in
                        selectedAdjective = GameData.adjectives.first { $0.word == word }
                    }
                )

                // Category Selection
                SelectionCard(
                    title: "CATEGORY",
                    selection: selectedCategory?.name ?? "Choose",
                    options: GameData.categories.map { $0.name },
                    onSelect: { name in
                        selectedCategory = GameData.categories.first { $0.name == name }
                    }
                )
            }
            .padding(.horizontal, 30)

            Spacer()

            // Start Button
            Button(action: onStart) {
                Text("START")
                    .font(.system(size: 32, weight: .black))
                    .foregroundColor(Color(hex: "FF6B6B"))
                    .frame(maxWidth: .infinity)
                    .frame(height: 70)
                    .background(Color.white)
                    .cornerRadius(35)
            }
            .padding(.horizontal, 30)
            .padding(.bottom, 40)
            .disabled(selectedAdjective == nil || selectedCategory == nil)
            .opacity(selectedAdjective == nil || selectedCategory == nil ? 0.5 : 1.0)
        }
    }
}

struct SelectionCard: View {
    let title: String
    let selection: String
    let options: [String]
    let onSelect: (String) -> Void

    @State private var showingOptions = false

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.system(size: 14, weight: .bold))
                .foregroundColor(.white.opacity(0.8))

            Button(action: { showingOptions = true }) {
                HStack {
                    Text(selection)
                        .font(.system(size: 24, weight: .bold))
                        .foregroundColor(.white)

                    Spacer()

                    Image(systemName: "chevron.down")
                        .foregroundColor(.white)
                }
                .padding(20)
                .background(Color.white.opacity(0.2))
                .cornerRadius(15)
            }
        }
        .confirmationDialog(title, isPresented: $showingOptions, titleVisibility: .visible) {
            ForEach(options, id: \.self) { option in
                Button(option) {
                    onSelect(option)
                }
            }
        }
    }
}
