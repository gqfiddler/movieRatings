import pandas as pd

def load_and_clean(movieFilepath, ratingsFilepath):
    # load and merge
    movies_df = pd.read_csv(movieFilepath)
    raw_ratings_df = pd.read_csv(ratingsFilepath)
    ratings_df = pd.merge(
            raw_ratings_df,
            movies_df,
            left_on="movieId",
            right_on="movieId"
        )
    # convert dates to datetime; add month and dayofweek columns
    startDate = pd.to_datetime("1970-01-01 00:00:00")
    ratings_df["datetime"] = startDate + ratings_df["timestamp"].apply(pd.Timedelta, unit="s")
    del ratings_df["timestamp"]
    ratings_df["date"] = ratings_df["datetime"].dt.date
    ratings_df["month"] = ratings_df["datetime"].dt.month
    ratings_df["weekday"] = ratings_df["datetime"].dt.dayofweek
    return ratings_df
