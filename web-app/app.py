#!/usr/bin/env python3
"""
Hot Take - Multiplayer Web Game
A Quiplash-style party game where players vote on hot takes
"""

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hot-take-secret-key-change-in-production'
socketio = SocketIO(app, cors_allowed_origins="*")

# Game rooms storage
game_rooms = {}

def generate_room_code():
    """Generate a 4-character room code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

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
    ],
    "Spicy 🌶️": [
        "Your Ex", "Your Current Partner", "One Night Stands", "Exes Texting You",
        "Dating Your Friend's Ex", "Friends With Benefits", "Situationships",
        "Age Gap Relationships", "Long Distance", "Open Relationships",
        "Sliding Into DMs", "Dating Coworkers", "Clubbing", "Bar Hookups",
        "Kissing on the First Date"
    ],
    "Party Dares": [
        "Take a Shot", "Truth or Dare", "Spin the Bottle", "Beer Pong",
        "Never Have I Ever", "Strip Poker", "Body Shots", "Karaoke Battle",
        "Shotgunning Beers", "Flip Cup", "Drunk Texting", "Late Night Food Runs",
        "Dancing on Tables", "Sneaking Out", "Breakfast After Partying"
    ],
    "This Person": [
        "The Host", "The Person to Your Left", "The Person to Your Right",
        "The Youngest Person Here", "The Oldest Person Here", "The Tallest Person",
        "The Person Who Arrived Last", "The Person Wearing Black",
        "The Person With the Longest Hair", "The Loudest Person Here",
        "The Quietest Person Here", "The Person Who Drank the Most",
        "The Single Person Here", "The Person Most Likely to Party",
        "The Person Who Suggested This Game"
    ]
}


@app.route('/')
def index():
    """Serve the main landing page"""
    return render_template('index.html')


@app.route('/host')
def host():
    """Serve the host screen"""
    return render_template('host.html')


@app.route('/play')
def play():
    """Serve the player screen"""
    return render_template('play.html')


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


# SocketIO Events
@socketio.on('create_room')
def handle_create_room(data):
    """Host creates a new game room"""
    room_code = generate_room_code()
    while room_code in game_rooms:
        room_code = generate_room_code()

    host_name = data.get('host_name', 'Host')

    game_rooms[room_code] = {
        'host_sid': request.sid,
        'players': {
            request.sid: {
                'name': host_name,
                'voted': False,
                'prompts': [],
                'prompts_submitted': False
            }
        },
        'state': 'lobby',
        'adjective': data.get('adjective'),
        'category': data.get('category'),
        'current_item': None,
        'votes': {'yay': 0, 'nah': 0},
        'voted_players': set(),
        'player_votes': {}  # Track individual votes: {player_sid: 'yay' or 'nah'}
    }

    join_room(room_code)
    emit('room_created', {
        'room_code': room_code,
        'adjective': data.get('adjective'),
        'category': data.get('category')
    })


@socketio.on('join_room')
def handle_join_room(data):
    """Player joins a game room"""
    room_code = data.get('room_code', '').upper()
    player_name = data.get('player_name', 'Anonymous')

    if room_code not in game_rooms:
        emit('error', {'message': 'Room not found'})
        return

    room = game_rooms[room_code]
    room['players'][request.sid] = {
        'name': player_name,
        'voted': False,
        'prompts': [],
        'prompts_submitted': False
    }

    join_room(room_code)
    emit('joined_room', {
        'player_name': player_name,
        'room_code': room_code,
        'adjective': room['adjective'],
        'category': room['category']
    })

    # Notify host of new player
    socketio.emit('player_joined', {
        'player_name': player_name,
        'player_count': len(room['players'])
    }, room=room_code)


@socketio.on('submit_prompts')
def handle_submit_prompts(data):
    """Player submits their 5 prompts"""
    room_code = data.get('room_code')
    prompts = data.get('prompts', [])

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid not in room['players']:
        return

    # Store player's prompts
    room['players'][request.sid]['prompts'] = prompts[:5]  # Max 5 prompts
    room['players'][request.sid]['prompts_submitted'] = True

    # Count how many players have submitted prompts
    total_players = len(room['players'])
    submitted_count = sum(1 for p in room['players'].values() if p['prompts_submitted'])

    # Notify host of progress
    socketio.emit('prompts_progress', {
        'submitted': submitted_count,
        'total': total_players
    }, room=room_code)

    # Notify player their prompts were received
    emit('prompts_confirmed', {})


@socketio.on('start_game')
def handle_start_game(data):
    """Host starts the game"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid != room['host_sid']:
        return

    # Start with category items
    category = room['category']
    all_prompts = CATEGORIES.get(category, []).copy()

    # Add player-submitted prompts to the pool
    for player_sid, player_data in room['players'].items():
        all_prompts.extend(player_data['prompts'])

    # Store in room for game use
    room['all_prompts'] = all_prompts
    room['used_prompts'] = set()
    room['state'] = 'playing'

    # Send all prompts to host
    socketio.emit('game_started', {
        'prompts': all_prompts
    }, room=room_code)


@socketio.on('next_question')
def handle_next_question(data):
    """Host requests next question"""
    room_code = data.get('room_code')
    item = data.get('item')
    adjective = data.get('adjective')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    room['current_item'] = item
    room['votes'] = {'yay': 0, 'nah': 0}
    room['voted_players'] = set()
    room['player_votes'] = {}  # Reset individual votes

    # Reset player voted status
    for player_sid in room['players']:
        room['players'][player_sid]['voted'] = False

    socketio.emit('new_question', {
        'item': item,
        'adjective': adjective
    }, room=room_code)


@socketio.on('submit_vote')
def handle_vote(data):
    """Player submits their vote"""
    room_code = data.get('room_code')
    vote = data.get('vote')  # 'yay' or 'nah'

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]

    # Check if player already voted
    if request.sid in room['voted_players']:
        return

    # Record vote
    room['voted_players'].add(request.sid)
    room['players'][request.sid]['voted'] = True
    room['votes'][vote] += 1
    room['player_votes'][request.sid] = vote  # Track individual vote

    # Send updated vote counts to host
    total_players = len(room['players'])
    votes_received = len(room['voted_players'])

    socketio.emit('vote_received', {
        'votes': room['votes'],
        'votes_received': votes_received,
        'total_players': total_players
    }, room=room_code)

    # Notify player their vote was counted
    emit('vote_confirmed', {'vote': vote})


@socketio.on('show_results')
def handle_show_results(data):
    """Host shows poll results"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]

    # Build detailed voter breakdown
    voter_breakdown = {
        'yay': [],
        'nah': []
    }

    for player_sid, vote in room['player_votes'].items():
        player_name = room['players'][player_sid]['name']
        voter_breakdown[vote].append(player_name)

    socketio.emit('display_results', {
        'votes': room['votes'],
        'voter_breakdown': voter_breakdown
    }, room=room_code)


@socketio.on('disconnect')
def handle_disconnect():
    """Handle player/host disconnect"""
    # Find and remove player from their room
    for room_code, room in list(game_rooms.items()):
        if request.sid == room['host_sid']:
            # Host left, close the room
            socketio.emit('room_closed', {}, room=room_code)
            del game_rooms[room_code]
        elif request.sid in room['players']:
            player_name = room['players'][request.sid]['name']
            del room['players'][request.sid]
            socketio.emit('player_left', {
                'player_name': player_name,
                'player_count': len(room['players'])
            }, room=room_code)


if __name__ == '__main__':
    # Run on all interfaces so it's accessible from network
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, allow_unsafe_werkzeug=True)
