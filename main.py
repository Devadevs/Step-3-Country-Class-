from country import Country #imports the py file to the main

def main_country():
  c = Country() #declares 'c' as Country
  
  c._gdp_per_capita = 44195.8 #prints the gdp
  print(c.gdp_per_capita)

  c._net_income = 0 #prints the net income
  print(c.net_income)
  
  c._imports = 0 #prints the amount spent on imports
  print(c.imports)
  
  c._exports = 0 #prints the amount spent on exports
  print(c.exports)
  
  c._expenses = 25 #prints the total expenses (in %)
  print(c.expenses)
  
  c._flag_color = "Red" #Prints flag color
  print(c.flag_color)
  
  c._popular_sport = "Soccer" #prints the popular sport
  print(c.popular_sport)
  
  c._music_genre = "Latin" #prints the music genre
  print(c.music_genre)
  
if __name__ == "__main__":
  main_country()