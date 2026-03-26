from experta import *
from knowledgeBase import movies


class MovieFact(Fact):
    pass  # works as the container


class MovieEngine(KnowledgeEngine):  # all the rules go here
    def __init__(self, min_dur, max_dur, min_year, max_year):
        super().__init__()
        self.results = []
        self.min_dur = min_dur
        self.max_dur = max_dur
        self.min_year = min_year
        self.max_year = max_year

    # Action genre rules

    @Rule(MovieFact(genre="Action", film_type="Feature Film"))
    def action_feature_film(self):
        for m in movies:
            if m["genre"] == "Action" and m["type"] == "Feature Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="Animated Film"))
    def action_animated_film(self):
        for m in movies:
            if m["genre"] == "Action" and m["type"] == "Animated Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="TV Movie"))
    def action_tv_movie(self):
        for m in movies:
            if m["genre"] == "Action" and m["type"] == "TV Movie":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="Action", film_type="Documentary"))
    def action_documentary(self):
        for m in movies:
            if m["genre"] == "Action" and m["type"] == "Documentary":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

  # Drama genre rules

    @Rule(MovieFact(genre="Drama", film_type="Feature Film"))
    def drama_feature_film(self):
        for m in movies:
            if m["genre"] == "Drama" and m["type"] == "Feature Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="Drama", film_type="TV Movie"))
    def drama_tv_movie(self):
        for m in movies:
            if m["genre"] == "Drama" and m["type"] == "TV Movie":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    # Comedy genre rules

    @Rule(MovieFact(genre="Comedy", film_type="Feature Film"))
    def comedy_feature_film(self):
        for m in movies:
            if m["genre"] == "Comedy" and m["type"] == "Feature Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="Comedy", film_type="Animated Film"))
    def comedy_animated_film(self):
        for m in movies:
            if m["genre"] == "Comedy" and m["type"] == "Animated Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    # History genre rules

    @Rule(MovieFact(genre="History", film_type="Feature Film"))
    def history_feature_film(self):
        for m in movies:
            if m["genre"] == "History" and m["type"] == "Feature Film":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)

    @Rule(MovieFact(genre="History", film_type="Documentary"))
    def history_documentary(self):
        for m in movies:
            if m["genre"] == "History" and m["type"] == "Documentary":
                if m["duration"] >= self.min_dur and m["duration"] <= self.max_dur:
                    if m["year"] >= self.min_year and m["year"] <= self.max_year:
                        self.results.append(m)