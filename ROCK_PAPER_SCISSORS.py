import random

print("=" * 40)
print("ROCK-PAPER-SCISSORS")
print("=" * 40)

options = ["rock", "paper", "scissors"]

while True:
    print("\nChoose: rock, paper, or scissors")
    user = input("Your choice: ").lower()
    
    if user not in options:
        print("❌ Invalid choice! Try again.")
        continue
    
    computer = random.choice(options)
    
    print(f"\n🤖 Computer chose: {computer}")
    print(f"👤 You chose: {user}")
    
    if user == computer:
        print("🤝 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if (play_again != "yes"):
        print"\n👋 Thanks for playing!"
        break
