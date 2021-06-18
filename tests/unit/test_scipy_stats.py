import hypothesis.strategies as st
import numpy as np
import pytest
import scipy.stats
from hypothesis import given


@pytest.mark.skip("Saving this for later")
@given(
    prob_success=st.floats(0.0, 1.0, exclude_min=False, exclude_max=False),
    sample_size=st.just(100),
)
def test__scipy_stats_bernoulli_rvs__empirical_probs_are_close_to_parameter(
    prob_success, sample_size
):
    """
    A bernoulli distribution is a distribution over two outcomes:
        * 0, which is referred to as a "failure"
        * 1, which is referred to as a "success"

    A bernoulli distribution is parameterized by `prob_success`, which is the probability
    of success.

    This test tests that random variables sampled from a bernoulli distribution with some `prob_success` parameter
    with have an "empirical" success proportion (i.e., a proportion of successes in the sample)
    that is "close" to the `prob_success` parameter.

    "Closeness" is determined by some pre-determined multiple of the standard error, where we know from statistics
    that a sample of size `n` from a Bernoulli with success probability `p` will have an empirical success proportion
    `phat` whose standard error is the square root of
        p*(1-p)
        ------
          n.
    """
    STANDARD_ERROR_TOLERANCE = 5
    successes = scipy.stats.bernoulli(prob_success).rvs(sample_size)
    empirical_success_proportion = np.mean(successes)
    standard_error = np.sqrt(prob_success * (1 - prob_success) / sample_size)
    assert (
        prob_success - STANDARD_ERROR_TOLERANCE * standard_error
        <= empirical_success_proportion
        <= prob_success + STANDARD_ERROR_TOLERANCE * standard_error
    )
