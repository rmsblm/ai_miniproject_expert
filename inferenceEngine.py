from experta import *
from knowledge_base import all_movies


class MovieFact(Fact):
    pass #works as the container

class MovieEngine(KnowledgeEngine):  # all the rules go here
    def __init__(self):
        super().__init__()
        self.results = [] 

 #Action genre rules

    @Rule(MovieFact(genre="Action", film_type="Feature Film", duration=P(lambda d: d <= 150), year=P(lambda y: y >= 2000)))
    def Action_feature_film(self):
          
      for m in all_movies:
         if m["genre"] == "Action" and m["type"] == "Feature Film":
             self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="Animated Film", duration=P(lambda d: d <= 150), year=P(lambda y: y >= 2000)))
    def action_animated_film(self):
          
      for m in all_movies:
         if m["genre"] == "Action" and m["type"] == "Animated Film":
             self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="TV Movie", duration=P(lambda d: d <= 150), year=P(lambda y: y >= 2000)))
    def action_tv_movie(self):
          
      for m in all_movies:
         if m["genre"] == "Action" and m["type"] == "TV Movie":
             self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="Documentary", duration=P(lambda d: d <= 150), year=P(lambda y: y >= 2000)))
    def action_documentary(self):
          
      for m in all_movies:
         if m["genre"] == "Action" and m["type"] == "Documentary":
             self.results.append(m)

