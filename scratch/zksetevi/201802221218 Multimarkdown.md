# 201802221218 Multimarkdown
tags = #mmd

## ____________________ Citation ____________________

[Visual Question Answering][#TeneyTipsTricksVisual2017]

## ________________________ Table ________________________

| a  | b  | c  | d  | e  |
|----|----|----|----|----|
| a2 | b2 | c2 | d2 | e2 |
|    |    |    |    |    |
|    |    |    |    |    |


## ____________________ Code Block ____________________

```python
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

## ____________________ Image ____________________

![Image](img/rene_shades.png)
