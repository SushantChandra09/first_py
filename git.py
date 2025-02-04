import os

# Get number of commits from the user
try:
    NUM_COMMITS = int(input("Enter the number of commits to create (Jan 13 - Jan 28, 2025): "))
except ValueError:
    print("Please enter a valid integer for the number of commits.")
    exit(1)

year = 2025  
START_DAY = 13
END_DAY = 28
DAYS_IN_RANGE = END_DAY - START_DAY + 1  # Total days available for commits

# Distribute commits evenly across Jan 13 - Jan 28
COMMITS_PER_DAY = max(1, NUM_COMMITS // DAYS_IN_RANGE)  
EXTRA_COMMITS = NUM_COMMITS % DAYS_IN_RANGE  # Handle extra commits

# Create a file for dummy commits
file_path = 'test.txt'
with open(file_path, 'a') as file:
    file.write('Initial commit\n')
os.system('git add test.txt')
os.system('git commit -m "Initial commit"')

commit_count = 0  

for day in range(START_DAY, END_DAY + 1):  # Loop from Jan 13 to Jan 28
    commits_today = COMMITS_PER_DAY + (1 if day - START_DAY < EXTRA_COMMITS else 0)  # Distribute extra commits

    for _ in range(commits_today):
        if commit_count >= NUM_COMMITS:
            break

        # Construct commit date string
        commit_date_str = f"{year}-01-{day:02d} 12:00:00"

        # Write to file to create a change
        with open(file_path, 'a') as file:
            file.write(f'Commit for {commit_date_str}\n')

        # Add and commit changes with the specified date
        os.system('git add test.txt')
        os.system(f'git commit --date="{commit_date_str}" -m "Commit #{commit_count+1}"')

        commit_count += 1

# Push commits to the remote repository
try:
    os.system('git push -u origin main')
except Exception as e:
    print(f"Error pushing to repository: {e}")
