import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 953761952

def solution(p: float, x: np.array) -> tuple:
    loc1 = 2 / 47 ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    loc2 = 2 / 47 ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    return loc1, loc2
