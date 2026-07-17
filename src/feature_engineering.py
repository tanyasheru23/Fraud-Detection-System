import pandas as pd
import numpy as np

"""
Feature engineering utilities for the Online Payment Fraud Detection project.

This module contains reusable functions for generating domain-specific
features used during both model training and inference.
"""

def balance_diff(df):
    """
    Compute sender and receiver balance differences after each transaction.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with balance difference features.
    """

    df["balanceDiffOrig"] = (
        df["oldbalanceOrg"]
        - df["newbalanceOrig"]
    )

    df["balanceDiffDest"] = (
        df["newbalanceDest"]
        - df["oldbalanceDest"]
    )

    return df

def balance_error(df):
    """
    Calculate balance consistency errors for the sender and receiver accounts.

    These features capture discrepancies between the expected and observed
    account balances after a transaction.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with balance error features.
    """

    df["origError"] = (
        df["oldbalanceOrg"]
        - df["amount"]
        - df["newbalanceOrig"]
    )

    df["destError"] = (
        df["oldbalanceDest"]
        + df["amount"]
        - df["newbalanceDest"]
    )

    return df

def fraction_amounts(df):
    """
    Create ratio-based features describing transaction size relative to
    available account balances.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with transaction fraction features.
    """

    df["fraction_used"] = np.where(
        df["oldbalanceOrg"] > 0,
        df["amount"] / df["oldbalanceOrg"],
        np.nan
    )

    df["remaining_fraction"] = np.where(
        df["oldbalanceOrg"] > 0,
        df["newbalanceOrig"] / df["oldbalanceOrg"],
        np.nan
    )

    df["transaction_fraction"] = np.where(
        (df["oldbalanceOrg"] + df["oldbalanceDest"]) > 0,
        df["amount"] /
        (df["oldbalanceOrg"] + df["oldbalanceDest"]),
        np.nan
    )

    return df

def zero_balance(df):
    """
    Create indicator features identifying accounts with zero initial balance.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with zero balance indicator features.
    """

    df["origin_zero_balance"] = (
        df["oldbalanceOrg"] == 0
    ).astype(int)

    df["destination_zero_balance"] = (
        df["oldbalanceDest"] == 0
    ).astype(int)

    return df

def balance_changed(df):
    """
    Create binary features indicating whether account balances changed after
    the transaction.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with balance change indicators.
    """

    df["origin_balance_changed"] = (
        df["oldbalanceOrg"] != df["newbalanceOrig"]
    ).astype(int)

    df["destination_balance_changed"] = (
        df["oldbalanceDest"] != df["newbalanceDest"]
    ).astype(int)

    return df

def entire_balance_transferred(df):
    """
    Identify transactions where nearly the entire sender balance was transferred.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with the full balance transfer indicator.
    """

    df["full_balance_transfer"] = np.isclose(
        df["amount"],
        df["oldbalanceOrg"],
        atol=1e-2
    ).astype(int)

    return df

def cash_transfer_indicator(df):
    """
    Create a binary feature indicating CASH_OUT or TRANSFER transactions.

    Args:
        df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe with cash transfer indicator.
    """

    df["is_cash_transfer"] = (
        df["type"].isin(["TRANSFER","CASH_OUT"])
    ).astype(int)

    return df

def feature_engineer(pre_fe_df):
    """
    Apply the complete feature engineering pipeline.

    This function generates all engineered features required by the fraud
    detection model while preserving the original input dataframe.

    Args:
        pre_fe_df (pd.DataFrame): Input transaction dataframe.

    Returns:
        pd.DataFrame: Dataframe containing all engineered features.
    """

    row_df = pre_fe_df.copy()

    balance_diff(row_df)
    balance_error(row_df)
    fraction_amounts(row_df)
    zero_balance(row_df)
    balance_changed(row_df)
    entire_balance_transferred(row_df)
    cash_transfer_indicator(row_df)
    
    return row_df