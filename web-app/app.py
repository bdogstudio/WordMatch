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
    "A Red Flag", "A Green Flag", "A Vibe", "Iconic", "Unhinged", "Based",
    "Problematic", "Elite", "Mid", "Cursed", "Chaotic", "Legendary", "Sketchy",
    "Fire", "Peak", "The Worst", "Giving Main Character Energy", "Giving NPC Energy",
    "Bussin", "No Cap", "Delulu", "Slay", "Ate and Left No Crumbs", "Lowkey Fire",
    "Highkey Sus", "Giving Ick", "Living Rent Free in My Head"
]

CATEGORIES = {
    "Social Media Discourse": [
        "TikTok", "Instagram Reels", "BeReal", "Snapchat Streaks",
        "LinkedIn Influencers", "Twitter Discourse", "Reddit Arguments", "Discord Mods",
        "Posting Thirst Traps", "Posting Your Gym Progress", "Posting Your Relationship",
        "Main Character Instagram Stories", "Vague Posting", "Oversharing on Social Media",
        "Posting Food Before Eating"
    ],
    "Dating & Relationship Chaos": [
        "Your Ex", "Your Ex's New Partner", "Situationships", "Friends With Benefits",
        "Exes Texting You at 2AM", "Dating Your Friend's Ex", "Sliding Into DMs",
        "First Date Small Talk", "Kissing on the First Date", "Saying 'I Love You' First",
        "Drunk Confessions of Love", "Getting Back With Your Ex", "Love Triangles",
        "Age Gap Relationships", "Long Distance Relationships"
    ],
    "Spicy Truth or Drink": [
        "Body Count Conversations", "Hookup Stories", "Walk of Shame",
        "Your Most Embarrassing Hookup", "Fake Orgasms", "Sex Dreams About Friends",
        "One Night Stands", "Dating App Horror Stories", "Catfishing",
        "Sending Nudes", "Getting Caught by Parents", "Bar Bathrooms",
        "Your Wildest Fantasy", "Threesomes", "Sugar Daddies/Mommies"
    ],
    "Most Likely To... (Drink If You're It!)": [
        "Most Likely to Go Viral on TikTok", "Most Likely to Drunk Text Their Ex",
        "Most Likely to Hook Up With Someone Here", "Most Likely to Get Arrested",
        "Most Likely to Become Famous", "Most Likely to Sleep Through an Alarm",
        "Most Likely to Start Drama", "Most Likely to Cry While Drunk",
        "Most Likely to Blackout Tonight", "Most Likely to Get a Tattoo They Regret",
        "Most Likely to Date a Celebrity", "Most Likely to Move to Another Country",
        "Most Likely to Get Married First", "Most Likely to Have Kids First",
        "Most Likely to Still Be Single in 10 Years"
    ],
    "Party Chaos": [
        "Shots Before 10PM", "Playing Beer Pong", "Strip Poker", "Body Shots",
        "Drunk Karaoke", "Shotgunning Beers", "Doing Keg Stands", "Flip Cup",
        "Kings Cup", "Drunk Dancing", "Making Out at Parties",
        "Throwing Up at a Party", "Crying in the Bathroom", "Losing Your Phone",
        "Uber Rides Home"
    ],
    "Gen Z Takes": [
        "Therapy", "Astrology", "Manifestation", "Crystals and Tarot Cards",
        "Taking Mental Health Days", "Cancel Culture", "Calling Everything Trauma",
        "Quiet Quitting", "Side Hustles", "Hustle Culture",
        "Being a Girl Boss", "Adulting", "Main Character Energy",
        "Romanticizing Your Life", "Self Care Sundays"
    ],
    "The Ick List": [
        "Guys Who Go to the Gym 7 Days a Week", "People Who Don't Drink",
        "Picky Eaters", "Being Rude to Waiters", "Bad Texters",
        "People Who Still Use Facebook", "Guys With Man Buns",
        "Cargo Shorts", "Fedoras", "Excessive Cologne/Perfume",
        "Talking About Their Ex", "Being Mean to Animals",
        "People Who Don't Tip", "Chewing With Your Mouth Open", "Not Washing Your Hands"
    ],
    "This Friend Group": [
        "The Mom Friend", "The Drunk Friend", "The Therapy Friend",
        "The Party Animal", "The One Always in a Relationship",
        "The Serial Ghoster", "The Overthinker", "The Hot Mess",
        "The One With Commitment Issues", "The Flirt", "The Drama Starter",
        "The Heartbreaker", "The Hopeless Romantic", "The Wild Card",
        "The One Everyone Has a Crush On"
    ],
    "Broke College Student": [
        "Ramen Noodles for Every Meal", "Overdrafting Your Bank Account",
        "Student Loans", "Living With Your Parents", "Unpaid Internships",
        "Cheap Beer", "Happy Hour Only", "Stealing From Dining Halls",
        "Sharing Netflix Passwords", "Walking Instead of Ubering",
        "Free Food at Events", "Thrifting", "Selling Your Stuff for Cash",
        "Asking Parents for Money", "Working Three Jobs"
    ],
    "Absolute Chaos": [
        "Screaming Crying Throwing Up", "Being Delulu", "Having the Ick",
        "Stalking Your Crush on Instagram", "Overthinking Everything",
        "Main Character Syndrome", "Posting Cringe", "Being Chronically Online",
        "Parasocial Relationships", "Simping", "Touch Grass Moments",
        "Living in a Situationship", "Being Down Bad", "Getting No Bitches",
        "Ratio'd on Twitter"
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
