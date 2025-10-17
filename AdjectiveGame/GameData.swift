import Foundation

// MARK: - Data Models

struct GameCategory: Identifiable, Hashable {
    let id = UUID()
    let name: String
    let items: [String]
}

struct Adjective: Identifiable, Hashable {
    let id = UUID()
    let word: String
}

// MARK: - Game Data

class GameData {
    static let adjectives: [Adjective] = [
        Adjective(word: "Fast"),
        Adjective(word: "Slow"),
        Adjective(word: "Big"),
        Adjective(word: "Small"),
        Adjective(word: "Hot"),
        Adjective(word: "Cold"),
        Adjective(word: "Expensive"),
        Adjective(word: "Cheap"),
        Adjective(word: "Beautiful"),
        Adjective(word: "Ugly"),
        Adjective(word: "Loud"),
        Adjective(word: "Quiet"),
        Adjective(word: "Heavy"),
        Adjective(word: "Light"),
        Adjective(word: "Dangerous"),
        Adjective(word: "Safe"),
        Adjective(word: "Famous"),
        Adjective(word: "Unknown"),
        Adjective(word: "Old"),
        Adjective(word: "New")
    ]

    static let categories: [GameCategory] = [
        GameCategory(name: "Animals", items: [
            "Elephant", "Cheetah", "Snail", "Mouse", "Blue Whale",
            "Hummingbird", "Lion", "Butterfly", "Shark", "Goldfish",
            "Eagle", "Penguin", "Giraffe", "Ant", "Bear"
        ]),
        GameCategory(name: "Cities", items: [
            "New York", "Tokyo", "Paris", "London", "Dubai",
            "Mumbai", "Sydney", "Moscow", "Rio de Janeiro", "Cairo",
            "Los Angeles", "Bangkok", "Rome", "Barcelona", "Singapore"
        ]),
        GameCategory(name: "Foods", items: [
            "Pizza", "Sushi", "Ice Cream", "Broccoli", "Lobster",
            "Bread", "Caviar", "Hot Dog", "Truffle", "Ramen",
            "Burger", "Salad", "Steak", "Popcorn", "Chocolate"
        ]),
        GameCategory(name: "Objects", items: [
            "Ferrari", "Bicycle", "Diamond", "Pencil", "Airplane",
            "Rocket", "Feather", "Anvil", "Smartphone", "Book",
            "Piano", "Guitar", "Laptop", "Candle", "Mirror"
        ]),
        GameCategory(name: "People", items: [
            "Albert Einstein", "Beyoncé", "Abraham Lincoln", "Leonardo da Vinci", "Oprah Winfrey",
            "Michael Jordan", "Shakespeare", "Lady Gaga", "Nelson Mandela", "Taylor Swift",
            "Steve Jobs", "Mozart", "Cleopatra", "Elon Musk", "Marie Curie"
        ]),
        GameCategory(name: "Places", items: [
            "Grand Canyon", "Eiffel Tower", "Mount Everest", "Sahara Desert", "Amazon Rainforest",
            "Great Wall of China", "Antarctica", "Niagara Falls", "Statue of Liberty", "Taj Mahal",
            "Colosseum", "Great Barrier Reef", "Stonehenge", "Pyramids of Giza", "Machu Picchu"
        ])
    ]
}
