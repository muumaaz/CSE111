n, k = input().split()
n = int(n)
k = int(k)

participation_counts = input().split()
participation_counts = [int(count) for count in participation_counts]

available_students = sum(1 for count in participation_counts if count < 5)
max_teams = available_students // 3

while max_teams > 0:
    if max_teams * k <= min(participation_counts):
        break
    max_teams -= 1

print(max_teams)