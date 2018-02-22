# 201802191807 First test note
tags = #first #plain #oneandtwo


This is the first test note.
Let's link to the other notes, and to self, in a bulleted list:

* [[201802191807]] First test note
* [[201802191808]] Second test note
* [[201802191810]] A third note

## A code block
```python
def evaluate_sentence(self, sentence, spo_gts):
    """
    Evaluate a single sentence. Return best result
    :param sentence: Input sentence
    :param spo_gts: list of subject, predicate, object groundtruth tuples
    :return: best matching score and associated matchings
    """
    max_score = 0
    max_matchings = (0,0,0,0,0,0,0)
    words = sentence.split()
    for gt in spo_gts:
        result_tuple = self.match_sentence(words, gt)
        matching_score, matchings = self.calc_metrics(result_tuple)
        if matching_score > max_score:
            max_score = matching_score
            max_matchings = matchings
        if matching_score == 7:
            break
    return max_score, max_matchings
```

## Citations

* Read @FastZettelkastenmethodeKontrollieredein2015
* Read [][#AhrensHowTakeSmart2017]
* Check out [@HarzigMultimodalImageCaptioning2018]

What a note! :-)

