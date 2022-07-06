from os import lseek


print("Hello World")

num_candiate = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
