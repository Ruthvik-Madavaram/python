from Cricket.Australia import score_card as aus
from Cricket.India import score_card as ind

if aus.TOTAL_SCORE < ind.TOTAL_SCORE:
    print("India won the match")
elif aus.TOTAL_SCORE > ind.TOTAL_SCORE:
    print("Australia won the match")
else:
    print("Match Tied")