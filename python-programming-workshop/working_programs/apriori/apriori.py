def apriori(trans_set, min_sup):
    """ trans_set :: [(trans_id, [item, ...]), ...]
        That is, a list of tuples.  Each tuple has a trans_id and a list of items. """
  
    result_dict = {}
  
    freq = {}
  
    for tid, items in trans_set:
        for item in set(items):
            freq[item] = freq.get(item,0)+1
  
    freq_items = dict((k,v) for k,v in freq.items() if v >= min_sup)
  
    simple_trans_set = [(tid,set(i for i in items if i in freq_items))
            for tid,items in trans_set]
  
    cur_freq_item_sets = dict(((i,), f) for (i,f) in freq_items.iteritems())
    result_dict[1] = cur_freq_item_sets
  
    for cur_item_set_size in xrange(2,len(freq_items)+1):
        joined_itemsets = [itemset_join(s1,s2)
                for s1 in cur_freq_item_sets
                for s2 in cur_freq_item_sets
                if itemset_joinable(s1,s2)
                ]
  
        pruned_itemsets = [iset for iset in joined_itemsets
                if all(sub_iset in cur_freq_item_sets
                    for sub_iset in minus_one_subsets(iset)
                    )
                ]
  
        item_set_freqs = dict((itemset,0) for itemset in pruned_itemsets)
  
        for tid,items in simple_trans_set:
            for itemset in pruned_itemsets:
                if all(item in items for item in itemset):
                    item_set_freqs[itemset]+=1
  
        new_freq_item_sets = dict((k,v) for (k,v) in item_set_freqs.iteritems()
                if v >= min_sup)
  
        if len(new_freq_item_sets)==0:
            break
  
        result_dict[cur_item_set_size] = new_freq_item_sets
        cur_freq_item_sets = new_freq_item_sets
  
    return result_dict
  
def itemset_joinable(s1,s2):
    return all(x1 == x2 for x1,x2 in zip(s1,s2)[:-1]) and s1[-1] < s2[-1]
  
def itemset_join(s1,s2):
    return s1+s2[-1:]
  
def minus_one_subsets(s):
    for i in xrange(len(s)):
        yield s[:i]+s[i+1:]
