# LING 83600 Lab 1
## Cass Lowry's answers

### Part 1

The code I wrote is *part1_wordnet.py*. The calculated similarity scores for each pair, along with the orginal human judgements, are in *part1_wordnet.tsv*.

The correlations and coverage for each similarity method are below, orderd from most highly to least correlated:

**Resnik**
Spearman's rho = 0.582; p-value < .001 
Coverage: 201 words, 99% of the data

**Lin**
Spearman's rho = 0.577; p-value < .001 
Coverage: 201 words, 99% of the data

**Wu-Palmer**
Spearman's rho = 0.553; p-value < .001 
Coverage: 200 words, 99% of the data

**Jiang-Conrath**
Spearman's rho = 0.493; p-value < .001 
Coverage: 197 words, 97% of the data

**Path**
Spearman's rho = 0.454; p-value < .001 
Coverage: 201 words, 99% of the data

**Leacock-Chodorow**
Spearman's rho = 0.454; p-value < .001
Coverage: 201 words, 99% of the data

The only challenge I had with Part 1 was deciding what kind of object to use to store the human judgement ratings. I decided to use pandas so that I could create additional columns for each word pairs' similarity scores. I had never used pandas before, so I had to spend a lot of time figuring out the indexing. A slight problem, when calculating the correlations, was excluding the NA cases, but that wasn't too difficult to figure out.

### Part 2

The code I wrote to tokenize the news crawl data is *tokenizer.py*. The calculated PPMI scores are in *ppmi_1.tsv*. 

Comparing the human judgements and the PPMI scores, the Spearman's rho is -0.150, p-value = .041. The PPMI covers 187/203 pairs, 92% of the data.

I had three main challenges with part 2:
* I did not know how to tokenize the data. I originally had each token as its own line. I feel like my tokenization code could be much better.
* I did not know how to run python scripts in the command line. Read some blog posts to learn that.
* I did not know how to re-organize the word pairs so that they match the ordering of the pairs output by *ppmi.py*. I did it manually in Excel because I ran out of time to learn a better way 

### Part 3

The calculated word2vec scores are in *word2vec_1.tsv*. 

Comparing the human judgements and the word2vec scores, the Spearman's rho is 0.664, p-value < .001. The word2vec covers 100% of the data.

Other than having to reinstall gensim, I had no problems with this portion

### Part 4

Something must have gone wrong with the PPMI results, because I should not have had a negative correlation. Comparing word2vec with the Wordnet similarity scores, word2vec far outperforms each of the similarity measurements