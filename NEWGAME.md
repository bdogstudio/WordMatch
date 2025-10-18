# SPOT THE LIE - New Game Design

## Game Flow

### 1. Lobby Phase
- Players join with room code
- Host sees player count
- Host starts game when ready

### 2. Lie Writing Phase (30 seconds)
- Host screen shows: "In 2019, a Florida man was arrested for throwing a _____ at his girlfriend."
- All players submit their fake answer to fill the blank
- Timer counts down

### 3. Voting Phase (20 seconds)
- Host screen shows ALL answers (player lies + real answer) shuffled
- Players vote for which one they think is the TRUTH
- Can't vote for your own lie

### 4. Results Phase
- Host screen reveals:
  - The correct answer (highlighted)
  - Who wrote each lie
  - Who voted for what
  - Points awarded:
    - +1000 points for guessing correctly
    - +500 points for each person who voted for your lie
- Show running leaderboard

### 5. Next Round
- Repeat with new prompt
- After 5-7 rounds, show final winner

## Technical Implementation

### Backend Changes Needed:
1. Replace adjectives/categories with PROMPTS array
2. Game states: lobby → writing → voting → results
3. Track: lies submitted, votes cast, scores
4. Shuffle answers before showing to vote

### Frontend Changes:
- Host: Big screen showing prompt, then answers, then results
- Player: Text input for lies, multiple choice for voting
- Clean, simple UI focused on the text

## Why This Is FUN:
- Creative challenge (write funny lies)
- Suspense (can you fool your friends?)
- Social interaction (laughing at ridiculous answers)
- Competition (points and leaderboard)
- Replayable (20 prompts, random order)
