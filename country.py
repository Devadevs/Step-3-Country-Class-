#Authors: Devan Hall, Ceasar Martinez, Logan Keach
class Country:

  def __init__(self):    # constructors
    self._imports = 0
    self._net_income = 0
    self._gdp_per_capita = 0
    self._exports = 0
    self._expenses = 0
    self._popular_sport = ""
    self._flag_color = ""
    self._music_genre = ""
    self._list_of_countries = []

  # Devan Hall 
  # get and set imports of country
  @property
  def imports(self):
    return self._imports
  @imports.setter
  def imports(self, imports):
    assert imports > 0    # imports are not negative 
    self._imports = imports 

  # Devan Hall
  # get and set  net income of country 
  @property
  def net_income(self):
    return self._net_income
  @net_income.setter
  def net_income(self, net_income):
    assert net_income > 0    # income is not negative
    self._imports = net_income

  # Devan Hall
  # get and set for gdp per capita of country
  @property
  def gdp_per_capita(self):
    return  self._gdp_per_capita
  @gdp_per_capita.setter
  def gdp_per_capita(self, gdp):
    assert isinstance(gdp, (int, float))
    self._gdp_per_capita = gdp
  #Cesar M
  #get and set exports of country
  @property
  def exports (self):
    return self._exports
  @exports.setter
  def exports(self,exports):
    assert exports >0    #exports or not negative
    self._exports=exports
    #Cesar M
  #get and set expenses for country
  @property
  def expenses(self):
    return self._expenses
  @expenses.setter
  def expenses(self,expenses):
      assert expenses >0    #expenses not negative 
      self._expenses=expenses

  #Logan Keach
  #get and set the popular sport of a country
  @property
  def popular_sport(self):
    return self._popular_sport
  @popular_sport.setter
  def popular_sport(self, popular_sport):
    self._popular_sport = popular_sport

  #Logan Keach
  #get and set the country's flag color/colors
  @property
  def flag_color(self):
    return self._flag_color
  @flag_color.setter
  def flag_color(self, flag_color):
    self._flag_color = flag_color

  #Logan Keach
  #get and set the favorite music genre of each country
  @property
  def music_genre(self):
    return self._music_genre
  @music_genre.setter
  def music_genre(self, music_genre):
    self._music_genre = music_genre
  
  
