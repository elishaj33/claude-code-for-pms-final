"""Recent acceptance — a running score of how often somebody has been
taking the callouts we send them.

One of the three inputs to ranking. Sits between 0 and 1. Everyone
starts at NEUTRAL_SCORE when we take them on.
"""

from config import (
    ACCEPTANCE_CREDIT,
    DECLINE_PENALTY,
    MISS_PENALTY,
    SCORE_FLOOR,
    SCORE_CEILING,
)

NEUTRAL_SCORE = 0.5

_scores = {}


def recent_acceptance(responder):
    """This responder's score right now. Read by routing.score()."""
    return _scores.get(responder.name, NEUTRAL_SCORE)


def record_accepted(responder):
    """They took the callout. Score goes up."""
    _set(responder, recent_acceptance(responder) + ACCEPTANCE_CREDIT)


# TODO(2019): should this ease back toward NEUTRAL_SCORE on its
# own after a while? For: somebody who had a bad month shouldn't still
# be carrying it in the spring. Against: if somebody has stopped taking
# work, we probably want that to stick until they take work again.
# Leaving it as-is for now.
def record_declined(responder):
    """They turned it down. Score goes down."""
    _set(responder, recent_acceptance(responder) - DECLINE_PENALTY)


def record_missed(responder):
    """We ran out of time waiting. Score goes down, but by less than a
    "no": a miss can be a slow phone rather than a choice.
    """
    _set(responder, recent_acceptance(responder) - MISS_PENALTY)


def reset_to_neutral(responder):
    """Put one responder back at NEUTRAL_SCORE.

    One-off, for the release that introduces record_missed: responders
    already pushed to the floor by the old rule are rarely asked, so they
    have no way to earn the score back. Not called anywhere in this
    folder; whoever ships the change runs it for the affected responders.
    """
    _set(responder, NEUTRAL_SCORE)


def _set(responder, value):
    _scores[responder.name] = max(SCORE_FLOOR, min(SCORE_CEILING, value))
