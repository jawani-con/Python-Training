class Voting:
    def __init__(self):
        self.vote_done = set()
        self.vote_count={}

    def cast_vote(self, name, candidate):
        if name not in self.vote_done:
            self.vote_done.add(name)
            if candidate in self.vote_count:
                self.vote_count[candidate] += 1
            else:
                self.vote_count[candidate] = 1
            print(f"Vote casted for {candidate} by {name}")
        else:
            print("You have already casted vote")

    def display_vote_count(self):
        print(self.vote_count)

def display_menu():
    print("\nVoting System")
    print("1. Cast Vote")
    print("2. Display Vote Count")
    print("3. Exit")

def main():
    vote=Voting()

    while True:
        display_menu()
        choice = int(input("Choose option (1-3):"))
        
        if choice == 1:
            name=input("Enter your name:")
            candidate=input("Enter the candidate you ant to cast vote for:")
            vote.cast_vote(name, candidate)

        elif choice == 2:
            vote.display_vote_count()
        
        else:
            print("Thanks for using voting system")
            break

main()  

    
