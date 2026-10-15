import random
import time

names = {"1": "rock", "2": "paper", "3": "scissors"}
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
TIME_LIMIT = 8

you = 0
comp_score = 0

print("Rock, Paper, Scissors - 3 rounds, most wins takes it!")
print("Type 1 for rock, 2 for paper, 3 for scissors.")
print(f"After the countdown you have {TIME_LIMIT} seconds to type your choice.\n")

for round_no in range(1, 4):
    print(f"--- Round {round_no} of 3 ---")

    
    for word in ["Rock...", "Paper...", "Scissors..."]:
        print(word)
        time.sleep(0.7)
    print("SHOOT!")

    comp = random.choice(list(names.values()))
    start = time.time()
    key = input("Your choice (1=rock, 2=paper, 3=scissors): ").strip()
    took = time.time() - start

    if took > TIME_LIMIT:
        print(f"Too slow ({took:.1f}s)! Computer wins this round.")
        comp_score += 1
    elif key not in names:
        print("Invalid choice! Computer wins this round.")
        comp_score += 1
    else:
        p = names[key]
        print(f"You: {p} | Computer: {comp}")
        if p == comp:
            print("Tie!")
        elif beats[p] == comp:
            print("You win this round!")
            you += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

    print(f"Score -> You: {you} | Computer: {comp_score}\n")

print("=== Final Result ===")
if you > comp_score:
    print("You win the match!")
elif comp_score > you:
    print("Computer wins the match!")
else:
    print("The match is a draw!")