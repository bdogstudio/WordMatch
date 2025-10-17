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
    "Overrated", "Underrated", "Toxic", "Cringe", "Valid", "Sus",
    "A Red Flag", "A Vibe", "Iconic", "Unhinged", "Based", "Problematic",
    "Elite", "Mid", "Cursed", "Chaotic", "Legendary", "Sketchy",
    "Fire", "Peak"
]

CATEGORIES = {
    "Social Media Apps": [
        "TikTok", "Instagram", "Twitter/X", "BeReal", "Snapchat",
        "Facebook", "LinkedIn", "Reddit", "Threads", "Hinge",
        "Tinder", "Bumble", "Discord", "Twitch", "YouTube"
    ],
    "Celebrities": [
        "Kanye West", "Taylor Swift", "Elon Musk", "Kim Kardashian", "Joe Rogan",
        "The Rock", "Lizzo", "Andrew Tate", "Mr. Beast", "Charli D'Amelio",
        "Bad Bunny", "Billie Eilish", "Drake", "Olivia Rodrigo", "Harry Styles"
    ],
    "Foods & Drinks": [
        "Pineapple on Pizza", "IPAs", "Oat Milk", "Kombucha", "Avocado Toast",
        "Hot Dogs", "Espresso Martinis", "White Claws", "Sushi", "Kale",
        "Chipotle", "Energy Drinks", "Vegan Burgers", "Mimosas", "Ranch Dressing"
    ],
    "Pop Culture": [
        "Marvel Movies", "Game of Thrones Ending", "The Office", "K-Pop", "Anime",
        "Reality TV", "True Crime Podcasts", "Fortnite", "Crypto", "NFTs",
        "Astrology", "CrossFit", "Yoga", "Therapy", "Self-Help Books"
    ],
    "Hot Takes": [
        "Pumpkin Spice Season", "New Year's Eve", "Valentine's Day", "Brunch",
        "Going to the Gym", "Working from Home", "Night Clubs", "Karaoke",
        "Double Texting", "Splitting the Bill", "Small Talk", "Ghosting",
        "Music Festivals", "House Parties", "Day Drinking"
    ],
    "Modern Life": [
        "Cancel Culture", "Hustle Culture", "Influencers", "Podcasts",
        "Fast Fashion", "Uber/Lyft", "DoorDash", "Airbnb", "Dating Apps",
        "Group Chats", "Voice Messages", "Read Receipts", "FaceTime",
        "Thrift Shopping", "Meal Prep"
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
