import hypothesis.strategies as st
import numpy as np
import scipy.stats
from hypothesis import given


@given(
    prob_success=st.floats(0.0, 1.0),
    sample_size=st.integers(1, 1000),
)
def test__scipy_stats_bernoulli_rvs__empirical_probs_are_close_to_parameter(
    prob_success, sample_size
):
    STANDARD_ERROR_TOLERANCE = 5
    successes = scipy.stats.bernoulli(prob_success).rvs(sample_size)
    empirical_prob = np.mean(successes)
    standard_error = np.sqrt(prob_success * (1 - prob_success) / sample_size)
    assert (
        prob_success - STANDARD_ERROR_TOLERANCE * standard_error
        <= empirical_prob
        <= prob_success + STANDARD_ERROR_TOLERANCE * standard_error
    )
