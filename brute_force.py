def brute_force(string,substring):
    all_scores=[]
    for i in range(len(string)-len(substring)):
        score = 0
        for j in range(len(substring)):
            if string[i+j]==substring[j]:
                #I gave the match a score of 5
                score=score+5
            else:
                #missmatch a score of -2
                score=score-2
        #save the score of each position in a list
        all_scores.append(score)
        idx = all_scores.index(max(all_scores))
        seq = string[idx:idx+len(substring)]
        seq_idx = (seq, idx)
    return (seq_idx)
