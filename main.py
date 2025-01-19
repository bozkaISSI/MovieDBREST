from fastapi import FastAPI, HTTPException
from typing import List
import models
import schemas

app = FastAPI()

@app.get("/movies/", response_model=List[schemas.Movie])
def get_movies():
    """Retrieve a list of all movies."""
    movies = models.Movie.select()
    return [schemas.Movie.from_orm(movie) for movie in movies]


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int):
    """Retrieve details of a specific movie by its ID."""
    try:
        movie = models.Movie.get(models.Movie.id == movie_id)
        return schemas.Movie.from_orm(movie)
    except models.Movie.DoesNotExist:
        raise HTTPException(status_code=404, detail="Movie not found")


@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie_data: schemas.MovieCreate):
    """Create a new movie."""
    new_movie = models.Movie.create(**movie_data.dict())
    return schemas.Movie.from_orm(new_movie)


@app.post("/movies/{movie_id}/actors", response_model=schemas.Movie)
def add_actor_to_movie(movie_id: int, actor_id: int):
    """Add an existing actor to a movie."""
    try:
        movie = models.Movie.get(models.Movie.id == movie_id)
        actor = models.Actor.get(models.Actor.id == actor_id)
        movie.actors.add(actor)
        return schemas.Movie.from_orm(movie)
    except models.Movie.DoesNotExist:
        raise HTTPException(status_code=404, detail="Movie not found")
    except models.Actor.DoesNotExist:
        raise HTTPException(status_code=404, detail="Actor not found")


@app.get("/actors/", response_model=List[schemas.Actor])
def get_actors():
    """Retrieve a list of all actors."""
    actors = models.Actor.select()
    return [schemas.Actor.from_orm(actor) for actor in actors]


@app.get("/actors/{actor_id}", response_model=schemas.Actor)
def get_actor(actor_id: int):
    """Retrieve details of a specific actor by its ID."""
    try:
        actor = models.Actor.get(models.Actor.id == actor_id)
        return schemas.Actor.from_orm(actor)
    except models.Actor.DoesNotExist:
        raise HTTPException(status_code=404, detail="Actor not found")


@app.post("/actors/", response_model=schemas.Actor)
def create_actor(actor_data: schemas.ActorCreate):
    """Create a new actor."""
    new_actor = models.Actor.create(**actor_data.dict())
    return schemas.Actor.from_orm(new_actor)
