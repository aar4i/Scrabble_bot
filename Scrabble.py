letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# make dictionary able to handle lowercase inputs as well
letters += [letter.lower() for letter in letters]

# multiply points list *2 because we created x2 letters(AaBb)

# create zip dict to combine letters and points
letter_to_points = {letters: points for letters,points in zip(letters,points)}
# add blank tiles to zip dict
letter_to_points[" "] = 0
print(letter_to_points)

# create function to score how many points in word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total
# score how many points in word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

# create new dict with players and words which they have played
player_to_words = {
  "player1": ["BLUE","TENNIS","EXIT"],
  "wordNerd": ["EARTH","EYES","MACHINE"],
  "Lexi Con": ["ERASER","BELLY","HUSKY"],
  "Prof Reader": ["ZAP","COMA","PERIOD"],
  }
# create empty list 
player_to_points = {}

def update_point_totals():
# create for loop to count how many points each players earn 
  for player, words in player_to_words.items():
    player_point = 0
    for word in words:
      player_point += score_word(word)
    player_to_points[player] = player_point

update_point_totals()
print(player_to_points)

# create function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player].append(word)

play_word("player1" , "CODE")
print(player_to_words)