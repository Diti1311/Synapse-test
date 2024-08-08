from itertools import combinations
Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter",
         "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd",
          "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy",
       "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray",
         "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

dj_sets = {
    "Kevin": Kevin,
    "Stuart": Stuart,
    "Bob": Bob,
    "Edith": Edith
}

common_favs = set()
possible_dj = []

for pair in list(combinations(dj_sets.keys(), 2)):
    dj1 = pair[0]
    dj2 = pair[1]
    common_favs = dj_sets[dj1].intersection(dj_sets[dj2])
    common = len(common_favs)*10
    if common >= 30:
        possible_dj.append((dj1, dj2, common))

sorted_list = sorted(possible_dj,key=lambda a: a[2], reverse=True)
print('The possible DJ pairs are:')

for pair in sorted_list:
    print('{} and {} overlap:{}'.format(pair[0],pair[1],pair[2]))