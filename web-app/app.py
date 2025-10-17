#!/usr/bin/env python3
"""
Word Match - Web Game
A fast-paced game where players decide if adjectives describe items
"""

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Game Data
ADJECTIVES = [
    "Fast", "Slow", "Big", "Small", "Hot", "Cold",
    "Expensive", "Cheap", "Beautiful", "Ugly", "Loud", "Quiet",
    "Heavy", "Light", "Dangerous", "Safe", "Famous", "Unknown",
    "Old", "New"
]

CATEGORIES = {
    "Animals": [
        "Elephant", "Cheetah", "Snail", "Mouse", "Blue Whale",
        "Hummingbird", "Lion", "Butterfly", "Shark", "Goldfish",
        "Eagle", "Penguin", "Giraffe", "Ant", "Bear"
    ],
    "Cities": [
        "New York", "Tokyo", "Paris", "London", "Dubai",
        "Mumbai", "Sydney", "Moscow", "Rio de Janeiro", "Cairo",
        "Los Angeles", "Bangkok", "Rome", "Barcelona", "Singapore"
    ],
    "Foods": [
        "Pizza", "Sushi", "Ice Cream", "Broccoli", "Lobster",
        "Bread", "Caviar", "Hot Dog", "Truffle", "Ramen",
        "Burger", "Salad", "Steak", "Popcorn", "Chocolate"
    ],
    "Objects": [
        "Ferrari", "Bicycle", "Diamond", "Pencil", "Airplane",
        "Rocket", "Feather", "Anvil", "Smartphone", "Book",
        "Piano", "Guitar", "Laptop", "Candle", "Mirror"
    ],
    "People": [
        "Albert Einstein", "Beyoncé", "Abraham Lincoln", "Leonardo da Vinci", "Oprah Winfrey",
        "Michael Jordan", "Shakespeare", "Lady Gaga", "Nelson Mandela", "Taylor Swift",
        "Steve Jobs", "Mozart", "Cleopatra", "Elon Musk", "Marie Curie"
    ],
    "Places": [
        "Grand Canyon", "Eiffel Tower", "Mount Everest", "Sahara Desert", "Amazon Rainforest",
        "Great Wall of China", "Antarctica", "Niagara Falls", "Statue of Liberty", "Taj Mahal",
        "Colosseum", "Great Barrier Reef", "Stonehenge", "Pyramids of Giza", "Machu Picchu"
    ]
}


@app.route('/')
def index():
    """Serve the main game page"""
    return render_template('index.html')


@app.route('/api/adjectives')
def get_adjectives():
    """Return list of available adjectives"""
    return jsonify(ADJECTIVES)


@app.route('/api/categories')
def get_categories():
    """Return list of available categories"""
    return jsonify(list(CATEGORIES.keys()))


@app.route('/api/items/<category>')
def get_items(category):
    """Return items for a specific category"""
    if category in CATEGORIES:
        return jsonify(CATEGORIES[category])
    return jsonify([]), 404


if __name__ == '__main__':
    # Run on all interfaces so it's accessible from network
    app.run(host='0.0.0.0', port=5001, debug=True)
