from fastapi import FastAPI, HTTPException
from playhouse.shortcuts import model_to_dict
import models

app = FastAPI()

@app.get("/movies/")
def get_movies():
    movies = models.Movie.select()
    return [model_to_dict(movie, backrefs=True) for movie in movies]

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    try:
        movie = models.Movie.get(models.Movie.id == movie_id)
        return model_to_dict(movie, backrefs=True)
    except models.Movie.DoesNotExist:
        raise HTTPException(status_code=404, detail="Movie not found")

@app.post("/movies/")
def create_movie(movie: dict):
    new_movie = models.Movie.create(
        title=movie["title"],
        director=movie["director"],
        year=movie["year"],
        description=movie.get("description", "")
    )
    return model_to_dict(new_movie)

@app.get("/actors/")
def get_actors():
    actors = models.Actor.select()
    return [model_to_dict(actor) for actor in actors]

@app.get("/actors/{actor_id}")
def get_actor(actor_id: int):
    try:
        actor = models.Actor.get(models.Actor.id == actor_id)
        return model_to_dict(actor)
    except models.Actor.DoesNotExist:
        raise HTTPException(status_code=404, detail="Actor not found")

@app.post("/actors/")
def create_actor(actor: dict):
    new_actor = models.Actor.create(name=actor["name"], surname=actor["surname"])
    return model_to_dict(new_actor)

@app.post("/movies/{movie_id}/actors/")
def add_actor_to_movie(movie_id: int, actor_id: int):
    try:
        movie = models.Movie.get(models.Movie.id == movie_id)
        actor = models.Actor.get(models.Actor.id == actor_id)
        movie.actors.add(actor)
        return {"message": f"Actor {actor.name} {actor.surname} added to movie {movie.title}"}
    except (models.Movie.DoesNotExist, models.Actor.DoesNotExist):
        raise HTTPException(status_code=404, detail="Movie or Actor not found")
