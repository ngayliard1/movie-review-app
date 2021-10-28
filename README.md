# movie-review-app

This repo contains some basic modeling on the movie dataset, which can be found here:

https://www.kaggle.com/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_critic_reviews.csv

The .ipynb notebook file has the modeling in it.

## Dash Application

There is a dash app that allows a user to enter a review and receive a predicted score.

Docker image is located here to view:
https://hub.docker.com/repository/docker/ngayliard/movie-review-dash-image

Here is how to use it.

1. Download Docker Desktop for your OS (Make sure to increase memory settings in Docker settings to 4+ GB)

2. Run this code from terminal

docker run -it -p 8050:8050 --rm --name review_container ngayliard/movie-review-dash-image:1

3. Go to localhost:8050 in a web browser

4. Type in a movie review

5. Get a Rotten or Fresh prediction!
