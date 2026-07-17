import pandas as pd

def handling_NaN(df):
    """
    Replace missing values in engineered ratio features.

    Missing values occur when balance-based ratios cannot be computed,
    such as when the original balance is zero.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with missing values handled.
    """

    df["fraction_used"] = df["fraction_used"].fillna(-1)
    df["remaining_fraction"] = df["remaining_fraction"].fillna(-1)
    df["transaction_fraction"] = df["transaction_fraction"].fillna(-1)

    return df

def drop_unused_columns(df):
    """
    Remove columns that are not used for model training.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe without unused identifier columns.
    """

    df = df.drop(columns=["nameOrig", "nameDest"])

    return df

def encode_transaction_type(df):
    """
    One-hot encode the transaction type feature.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with encoded transaction types.
    """

    df = pd.get_dummies(
        df,
        columns=["type"],
        drop_first=False,
        dtype=int
    )

    return df

def process(pre_df):
    """
    Apply all preprocessing steps before model training or inference.

    Args:
        pre_df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Preprocessed dataframe ready for the model.
    """

    row_df = pre_df.copy()

    row_df = handling_NaN(row_df)
    row_df = drop_unused_columns(row_df)
    row_df = encode_transaction_type(row_df)

    return row_df
