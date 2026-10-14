"""Tuning values for callout routing.

Everything in here changes who gets asked to take a job, so don't
change anything in here without telling the engineering manager.
"""

# How long a callout offer stays on a responder's phone before we give
# up on them and move to the next person on the list.
OFFER_TIMEOUT_SECONDS = 60           # was 90 until 4.2

# How much each input counts when we rank who to ask first. These are
# relative to each other; they don't need to add up to anything.
WEIGHT_PROXIMITY = 0.60              # was 0.45 until 4.2
WEIGHT_RECENT_ACCEPTANCE = 0.25      # was 0.40 until 4.2
WEIGHT_CAPABILITY_MATCH = 0.15       # unchanged since 4.0

# Points on and off the recent-acceptance score.
ACCEPTANCE_CREDIT = 0.08
DECLINE_PENALTY = 0.12               # they turned it down
# A missed ping (the wait ran out) costs less than a "no". A miss can be
# a slow phone, not a choice. PROPOSED, not shipped: 0.03 chosen from a
# replay of 12 Aug to 6 Sep pings; check against response times.
MISS_PENALTY = 0.03

# The score never goes outside these.
SCORE_FLOOR = 0.0
SCORE_CEILING = 1.0

# Anyone further out than this scores zero on proximity.
PROXIMITY_HORIZON_MINUTES = 45
