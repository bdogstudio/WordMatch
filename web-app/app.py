#!/usr/bin/env python3
"""
Spot The Lie - Multiplayer Web Game
A Fibbage-style party game where players create fake answers and vote for the truth
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

# Game Data - Wild facts with blanks for players to fill
PROMPTS = [
    {
        "text": "In 2019, a Florida man was arrested for throwing a _____ at his girlfriend during an argument.",
        "answer": "alligator",
        "category": "Florida Man"
    },
    {
        "text": "Scientists discovered that _____ can get drunk and act aggressively when intoxicated.",
        "answer": "bees",
        "category": "Weird Science"
    },
    {
        "text": "A man in Japan married a _____ in 2018.",
        "answer": "hologram anime character",
        "category": "WTF Weddings"
    },
    {
        "text": "The world record for the longest _____ is 17 hours and 2 minutes.",
        "answer": "burp",
        "category": "Weird Records"
    },
    {
        "text": "In ancient Rome, people used _____ as mouthwash.",
        "answer": "urine",
        "category": "Gross History"
    },
    {
        "text": "A study found that _____ makes you more attractive to mosquitoes.",
        "answer": "drinking beer",
        "category": "Weird Science"
    },
    {
        "text": "In 2023, a TikToker went viral for eating _____ for 100 days straight.",
        "answer": "raw liver",
        "category": "Viral Stunts"
    },
    {
        "text": "The average person spends 6 months of their life _____ .",
        "answer": "waiting for red lights to turn green",
        "category": "Weird Facts"
    },
    {
        "text": "A woman was banned from Walmart for riding around on a _____ while drinking wine.",
        "answer": "motorized scooter cart",
        "category": "Walmart Stories"
    },
    {
        "text": "In Sweden, there's a museum dedicated entirely to _____ .",
        "answer": "failures and bad ideas",
        "category": "Weird Museums"
    },
    {
        "text": "A man proposed to his girlfriend using _____ and she said yes.",
        "answer": "100 tacos arranged in a heart",
        "category": "Creative Proposals"
    },
    {
        "text": "The most expensive _____ ever sold was $69 million.",
        "answer": "NFT",
        "category": "Crazy Expensive"
    },
    {
        "text": "In 2022, a Twitter user became famous for _____ for 365 days.",
        "answer": "posting pictures of their pet rock",
        "category": "Social Media Fame"
    },
    {
        "text": "Scientists proved that _____ can actually improve your memory.",
        "answer": "smelling rosemary",
        "category": "Brain Facts"
    },
    {
        "text": "A restaurant in Tokyo only serves dishes made with _____ .",
        "answer": "insects",
        "category": "Weird Restaurants"
    },
    {
        "text": "The world's most expensive coffee is made from _____ .",
        "answer": "beans pooped out by civets",
        "category": "Gross Food"
    },
    {
        "text": "In 2024, a YouTuber got 10 million views for _____ for 24 hours.",
        "answer": "living in a Walmart",
        "category": "YouTube Challenges"
    },
    {
        "text": "A couple got married at _____ because the groom proposed there.",
        "answer": "Taco Bell",
        "category": "Unusual Venues"
    },
    {
        "text": "The most bizarre item ever stolen was _____ from a museum in 2023.",
        "answer": "a 18 karat gold toilet",
        "category": "Weird Crimes"
    },
    {
        "text": "A fitness influencer went viral for working out with _____ instead of weights.",
        "answer": "frozen turkeys",
        "category": "Fitness Fails"
    }
]


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


@app.route('/api/prompts')
def get_prompts():
    """Return list of available prompts"""
    return jsonify([p['category'] for p in PROMPTS])


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
        'players': {},
        'state': 'lobby',
        'current_prompt': None,
        'current_lies': {},  # {player_sid: lie_text}
        'current_votes': {},  # {player_sid: voted_answer}
        'scores': {},  # {player_sid: points}
        'used_prompts': [],
        'round': 0
    }

    join_room(room_code)
    emit('room_created', {
        'room_code': room_code
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
        'name': player_name
    }
    room['scores'][request.sid] = 0

    join_room(room_code)
    emit('joined_room', {
        'player_name': player_name,
        'room_code': room_code
    })

    # Notify host of new player
    socketio.emit('player_joined', {
        'player_name': player_name,
        'player_count': len(room['players'])
    }, room=room_code)


@socketio.on('submit_lie')
def handle_submit_lie(data):
    """Player submits their lie for the current prompt"""
    room_code = data.get('room_code')
    lie = data.get('lie', '').strip()

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid not in room['players']:
        return

    # Store player's lie
    room['current_lies'][request.sid] = lie

    # Check if all players have submitted
    total_players = len(room['players'])
    submitted_count = len(room['current_lies'])

    # Notify host of progress
    socketio.emit('lies_progress', {
        'submitted': submitted_count,
        'total': total_players
    }, room=room_code)

    # Notify player their lie was received
    emit('lie_confirmed', {})

    # If all players submitted, move to voting
    if submitted_count == total_players:
        socketio.emit('all_lies_submitted', {}, room=room_code)


@socketio.on('start_game')
def handle_start_game(data):
    """Host starts the game"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid != room['host_sid']:
        return

    room['state'] = 'playing'
    room['round'] = 0

    # Start first round
    start_new_round(room_code)


def start_new_round(room_code):
    """Start a new round with a fresh prompt"""
    room = game_rooms[room_code]
    room['round'] += 1

    # Pick a random unused prompt
    available_prompts = [p for p in PROMPTS if p['text'] not in room['used_prompts']]
    if not available_prompts:
        # Game over
        socketio.emit('game_over', {
            'scores': room['scores'],
            'players': {sid: p['name'] for sid, p in room['players'].items()}
        }, room=room_code)
        return

    prompt = random.choice(available_prompts)
    room['used_prompts'].append(prompt['text'])
    room['current_prompt'] = prompt
    room['current_lies'] = {}
    room['current_votes'] = {}
    room['state'] = 'writing'

    # Send prompt to everyone
    socketio.emit('new_round', {
        'round': room['round'],
        'prompt_text': prompt['text'],
        'category': prompt['category']
    }, room=room_code)


@socketio.on('start_voting')
def handle_start_voting(data):
    """Host starts the voting phase"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid != room['host_sid']:
        return

    room['state'] = 'voting'

    # Shuffle all answers (lies + truth)
    answers = list(room['current_lies'].values())
    answers.append(room['current_prompt']['answer'])
    random.shuffle(answers)

    # Send shuffled answers to everyone
    socketio.emit('voting_started', {
        'answers': answers
    }, room=room_code)


@socketio.on('submit_vote')
def handle_vote(data):
    """Player submits their vote for which answer is true"""
    room_code = data.get('room_code')
    voted_answer = data.get('answer')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]

    # Check if player already voted
    if request.sid in room['current_votes']:
        return

    # Record vote
    room['current_votes'][request.sid] = voted_answer

    # Notify host of progress
    total_players = len(room['players'])
    votes_received = len(room['current_votes'])

    socketio.emit('votes_progress', {
        'votes_received': votes_received,
        'total_players': total_players
    }, room=room_code)

    # Notify player their vote was counted
    emit('vote_confirmed', {})

    # If all players voted, notify host
    if votes_received == total_players:
        socketio.emit('all_votes_in', {}, room=room_code)


@socketio.on('show_results')
def handle_show_results(data):
    """Host shows results and calculates scores"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    room['state'] = 'results'

    correct_answer = room['current_prompt']['answer']

    # Calculate scores
    results = []
    for player_sid, voted_answer in room['current_votes'].items():
        player_name = room['players'][player_sid]['name']

        # +1000 points for guessing correctly
        if voted_answer == correct_answer:
            room['scores'][player_sid] += 1000
            results.append({
                'player': player_name,
                'voted_for': voted_answer,
                'correct': True,
                'points_earned': 1000
            })
        else:
            results.append({
                'player': player_name,
                'voted_for': voted_answer,
                'correct': False,
                'points_earned': 0
            })

    # +500 points for each person who voted for your lie
    for liar_sid, lie_text in room['current_lies'].items():
        votes_for_lie = sum(1 for voted in room['current_votes'].values() if voted == lie_text)
        if votes_for_lie > 0:
            points = votes_for_lie * 500
            room['scores'][liar_sid] += points
            liar_name = room['players'][liar_sid]['name']
            results.append({
                'player': liar_name,
                'lie': lie_text,
                'fooled': votes_for_lie,
                'points_earned': points
            })

    # Send results to everyone
    socketio.emit('display_results', {
        'correct_answer': correct_answer,
        'all_answers': list(room['current_lies'].values()) + [correct_answer],
        'results': results,
        'scores': room['scores'],
        'players': {sid: p['name'] for sid, p in room['players'].items()}
    }, room=room_code)


@socketio.on('next_round')
def handle_next_round(data):
    """Host starts next round"""
    room_code = data.get('room_code')

    if room_code not in game_rooms:
        return

    room = game_rooms[room_code]
    if request.sid != room['host_sid']:
        return

    start_new_round(room_code)


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
            if request.sid in room['scores']:
                del room['scores'][request.sid]
            socketio.emit('player_left', {
                'player_name': player_name,
                'player_count': len(room['players'])
            }, room=room_code)


if __name__ == '__main__':
    # Run on all interfaces so it's accessible from network
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, allow_unsafe_werkzeug=True)
