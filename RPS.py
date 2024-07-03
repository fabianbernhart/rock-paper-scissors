def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess: str = 'S'
    if not prev_play:
        opponent_history.clear()
        return guess

    rock_count: int = 0
    paper_count: int = 0
    scissors_count: int = 0
    for i in range(len(opponent_history) - 1):
        if opponent_history[i] == prev_play:
            next = opponent_history[i + 1]
            if next == 'R':
                rock_count += 1
            if next == 'P':
                paper_count += 1
            if next == 'S':
                scissors_count += 1

    rock_guess: int = scissors_count
    paper_guess: int = rock_count
    scissors_guess: int = paper_count

    max_guess = max(rock_guess, paper_guess, scissors_guess)
    if max_guess == rock_guess:
        guess = 'R'
    if max_guess == paper_guess:
        guess = 'P'
    if max_guess == scissors_guess:
        guess = 'S'

    big_brain = {
        'P': 'R',
        'R': 'S',
        'S': 'P',
    }
    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2] != opponent_history[-3]:
            guess = big_brain[prev_play]

    if rock_count == paper_count == scissors_count == 0:
        guess = prev_play

    return guess
