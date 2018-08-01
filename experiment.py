import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def split(smallRatings_df):
    day_grouped_df = smallRatings_df.groupby(["userId","date"]).agg({"movieId":"count"}).reset_index()
    day_grouped_df.rename(index=str, columns={"movieId":"rating_count"}, inplace=True)

    # SEPARATE SINGLETON DATASET
    singletons_df = day_grouped_df[day_grouped_df["rating_count"]==1]
    singletons_df = singletons_df.merge(
        smallRatings_df,
        on=["userId", "date"])
    del singletons_df["rating_count"]

    # SEPARATE LARGE-BATCH DATASET
    batches_df = day_grouped_df[day_grouped_df["rating_count"]>5]
    batches_df = batches_df.merge(
        smallRatings_df,
        on=["userId", "date"])
    del batches_df["rating_count"]

    return singletons_df, batches_df

def contrastPlots(singletons_df, batches_df):
    # PLOT SINGLETONS
    rating_mean = singletons_df["rating"].mean()
    rating_std = singletons_df["rating"].std()
    plt.figure(figsize=(15,5))
    plt.subplot(121)
    sns.countplot("rating", data=singletons_df)
    plt.title("SINGLETON rating distribution (mean = {}, std = {})".format(round(rating_mean, 2), round(rating_std, 2)))
    plt.subplot(122)
    roundedRatings = (singletons_df["rating"] + .01).round() # add .01 to avoid skew from default banker's rounding
    sns.countplot(roundedRatings)
    plt.title("SINGLETON rating distribution (rounded up to nearest whole star)")
    plt.show()

    # PLOT LARGE BATCHES
    rating_mean = batches_df["rating"].mean()
    rating_std = batches_df["rating"].std()
    plt.figure(figsize=(15,5))
    plt.subplot(121)
    sns.countplot("rating", data=batches_df)
    plt.title("BATCH rating distribution (mean = {}, std = {})".format(round(rating_mean, 2), round(rating_std, 2)))
    plt.subplot(122)
    roundedRatings = (batches_df["rating"] + .01).round() # add .01 to avoid skew from default banker's rounding
    sns.countplot(roundedRatings)
    plt.title("BATCH rating distribution (rounded up to nearest whole star)")
    plt.show()

    return None
