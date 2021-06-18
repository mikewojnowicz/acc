import hypothesis.strategies as st
import numpy as np
import pytest
import scipy.stats
from hypothesis import given


@pytest.mark.skip("Saving this for later")
@given(
    prob_success=st.floats(0.0, 1.0, exclude_min=False, exclude_max=False),
    size=st.just(100),
)
def test_scipy_stats_bernoulli_rvs(prob_success, size):
    successes = scipy.stats.bernoulli(prob_success).rvs(size)
    empirical_prob = np.mean(successes)
    standard_error = np.sqrt(prob_success * (1 - prob_success) / size)
    assert (
        prob_success - 5 * standard_error
        <= empirical_prob
        <= prob_success + 5 * standard_error
    )
