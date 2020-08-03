
# coding: utf_8
  
class FPTree(object):
    def __init__(self, min_sup):
        """ Build a FPTree with a given transaction set.
  
            weighted_trans_set :: [([item, ...], weight), ...]
            That is, a list of tuples.  Each tuple has a trans_id and a list of items.
  
            item:       Item in the transaction.
                        Duplicate items are allowed, but they are only counted as one.
            weight:     Weight of this itemset.  It denotes how many times such
                        pattern appears in the transaction DB.
  
            min_sup:    Minimum support.  The minimum frequency of an item to be
                        considered as "frequent".
            """
  
        self.min_sup = min_sup
        self.header_table = {}
        self.root = FPNode(None, None)
        self.item_sup = {}
  
    @staticmethod
    def new_by_named_trans_set(named_trans_set, min_sup):
        weighted_trans_set = [(items, 1) for tid,items in named_trans_set]
        return FPTree.new_by_weighted_trans_set(weighted_trans_set, min_sup)
  
    @staticmethod
    def new_by_weighted_trans_set(weighted_trans_set, min_sup):
        self = FPTree(min_sup)
  
        for items, weight in weighted_trans_set:
            for item in set(items):
                self.item_sup[item] = self.item_sup.get(item,0)+weight
  
        freq_rev_list = sorted(
                [(i,f) for (i,f) in self.item_sup.items() if f >= min_sup],
                key=lambda(i,f):f, reverse=True)
  
        freq_rev_order = dict((i,o) for (o,(i,f)) in enumerate(freq_rev_list))
        self.freq_rev_order = freq_rev_order
  
        for items, weight in weighted_trans_set:
            cur_freq_items = sorted([i for i in set(items) if i in freq_rev_order],
                    key = lambda i:freq_rev_order[i])
  
            self.insert_tree(cur_freq_items, weight)
  
        return self
  
    def is_empty(self):
        return len(self.root.children)==0
  
    def insert_tree(self, freq_items, weight):
        cur_node = self.root
        for item in freq_items:
            if item not in cur_node.children:
                new_node = FPNode(item, cur_node)
                cur_node.children[item] = new_node
                self.header_table.setdefault(item,[]).append(new_node)
            cur_node = cur_node.children[item]
            cur_node.count += weight
  
    def get_frequent_patterns(self):
        for fi in self._fp_growth(tuple()):
            yield fi
  
    def _fp_growth(self, suffix):
        for item in self.header_table:
            new_suffix = (item,)+suffix
            yield (new_suffix, self.item_sup[item])
            cond_tree = self._get_conditional_tree(item)
            if not cond_tree.is_empty():
                for freq_pat in cond_tree._fp_growth(new_suffix):
                    yield freq_pat
  
    def _get_conditional_tree(self, item):
        cond_db = []
        for node in self.header_table[item]:
            path = []
            cur_node = node.parent
            while cur_node is not self.root:
                path.append(cur_node.item)
                cur_node = cur_node.parent
            cond_db.append((path, node.count))
  
        return FPTree.new_by_weighted_trans_set(cond_db, self.min_sup)
  
  
class FPNode(object):
    def __init__(self, item, parent):
        self.item = item
        self.count = 0
        self.children = {}
        self.parent = parent
  
def analyze_trans_set(named_trans_set, min_sup):
    fpt = FPTree.new_by_named_trans_set(named_trans_set, min_sup)
    for freq_pat in fpt.get_frequent_patterns():
        yield freq_pat
  
def analyze_trans_set_group_by_size(named_trans_set, min_sup):
    group_dict = {}
  
    for itemset, sup_count in analyze_trans_set(named_trans_set, min_sup):
        count_dict = group_dict.setdefault(len(itemset),{})
        count_dict[itemset] = sup_count
  
    return group_dict
  
def print_fp_tree(fptree):
    def print_node(node, head_prefix, children_prefix):
        print u"%s%s:%d"%(head_prefix, node.item, node.count)
        children = node.children.values()
        if len(children)==0:
            return
        for child in children[:-1]:
            print_node(child, children_prefix+u"├", children_prefix+u"│")
        print_node(children[-1], children_prefix+u"└", children_prefix+u" ")
    print_node(fptree.root,u"",u"")
  
if __name__=='__main__':
    small_trans = [
            (100, ['f','a','c','d','g','i','m','p']),
            (200, ['a','b','c','f','l','m','o']),
            (300, ['b','f','h','j','o']),
            (400, ['b','c','k','s','p']),
            (500, ['a','f','c','e','l','p','m','n']),
            ]
  
    fpt = FPTree.new_by_named_trans_set(small_trans, 3)
  
    print "FPTree:"
    print_fp_tree(fpt)
  
    # Show some conditional subtrees
    for cond_items in [['p'],['m'],['c','m'],['b']]:
        t = fpt
        for cond_item in reversed(cond_items):
            t = t._get_conditional_tree(cond_item)
        print "Conditional subtree of %s is:" % "".join(cond_items)
        print_fp_tree(t)
  
    print "Frequent items:"
    for fp in fpt.get_frequent_patterns():
        print fp
  
