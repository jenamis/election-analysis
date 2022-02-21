# -*- coding: UTF-8 -*-

# Add dependencies
import csv
import os

# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign variable to save file to path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declare candidate options list
candidate_options = []

# Declare candidate vote count dictionary
candidate_votes = {}

# Declare county list
county_list = []

# Declare county vote count dictionary
county_votes = {}

# Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track largest turnout county and vote count
largest_turnout_county = ""
largest_count = 0

# Read election data csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read header
    header = next(reader)

    # Get total, candidate, and county vote counts
    for row in reader:

        # Add to total vote count
        total_votes += 1

        # Candidate data
        # Get candidate name from each row
        candidate_name = row[2]

        # Add candidate name to candidate list if not already in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add to candidate's vote count
        candidate_votes[candidate_name] += 1

        # County data
        # Get county name from each row
        county_name = row[1]

        # Add county name to county list if not already in list
        if county_name not in county_list:
            county_list.append(county_name)

            # Begin tracking county's vote count
            county_votes[county_name] = 0

        # Add to county's vote count
        county_votes[county_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results)

    # Save final vote count to text file
    txt_file.write(election_results)

    # Use for loop to get county from county vote count dictionary
    for county_name in county_votes:

        # Get county vote count
        county_vote_count = county_votes.get(county_name)

        # Calculate percentage of votes for county
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100

        # Print county results to terminal
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results)

        # Save county votes to text file
        txt_file.write(county_results)

        # Determine winning county and get its vote count
        if county_vote_count > largest_count:
            largest_count = county_vote_count
            largest_turnout_county = county_name

    # Print county with largest turnout to terminal
    largest_turnout_result = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(largest_turnout_result)

    # Save county with largest turnout to text file
    txt_file.write(largest_turnout_result)

    # Use for loop to get candidate from candidate vote count dictionary
    for candidate_name in candidate_votes:

        # Get candidate vote count
        votes = candidate_votes.get(candidate_name)

        # Calculate percentage of votes for candidate
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print candidate results to terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        #  Save candidate results to text file
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
    # Print winning candidate summary to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)