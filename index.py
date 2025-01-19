# You are allowed to import any modules whatsoever (not even numpy, sklearn etc)
# The use of file IO is forbidden. Your code should not read from or write onto files

# SUBMIT YOUR CODE AS TWO PYTHON (.PY) FILES INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILES MUST BE index.py and execute.py

# DO NOT CHANGE THE NAME OF THE METHODS my_index BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to create indices or statistics
class TrieNode:
    __slots__ = ['children', 'positions', 'is_terminal']
    
    def __init__(self):
        self.children = [None] * 26
        self.positions = []
        self.is_terminal = False

    def __getstate__(self):
        return (self.positions, self.is_terminal)

    def __setstate__(self, state):
        self.positions, self.is_terminal = state
        self.children = [None] * 26

class Trie:
    __slots__ = ['root']

    def __init__(self):
        self.root = TrieNode()

    def __getstate__(self):
        return ()

    def __setstate__(self, state):
        self.root = TrieNode()

    def char_to_index(self, ch):
        idx = ord(ch) - ord('a')
        return idx if 0 <= idx < 26 else -1

    def insert(self, word, position):
        current = self.root
        for char in word:
            idx = self.char_to_index(char)
            if idx == -1:
                continue  
            if current.children[idx] is None:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_terminal = True
        current.positions.append(position)

    def search(self, word):
        current = self.root
        for char in word:
            idx = self.char_to_index(char)
            if idx >= 0:
                if current.children[idx] is None:
                    return []
                current = current.children[idx]
        return current.positions if current.is_terminal else []

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            idx = self.char_to_index(char)
            if idx >= 0:
                if current.children[idx] is None:
                    return []
                current = current.children[idx]
        found_positions = []
        self._collect_positions(current, found_positions)
        return found_positions

    def _collect_positions(self, node, positions):
        if node.is_terminal:
            positions.extend(node.positions)
        for child in node.children:
            if child is not None:
                self._collect_positions(child, positions)
################################
# Non Editable Region Starting #
################################
def my_index( tuples ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create indices and statistics
	# Each tuple has 3 values -- the id, name and year
	
	# THE METHOD SHOULD RETURN A DISK MAP AND A VARIABLE PACKAGING INDICES AND STATS
    disk = []
    pos = 0
    name_trie = Trie()
    max_year = max(record[2] for record in tuples)
    year_positions = [[] for _ in range(max_year + 1)]
    sorted_tuples = sorted(tuples, key=lambda record: (record[1].lower(), record[2]))
    for id_val, name_val, year_val in sorted_tuples:
        disk.append(id_val)
        name_trie.insert(name_val.lower(), pos)
        year_positions[year_val].append(pos)
        pos += 1
    idx_stat=(name_trie, year_positions)
    return disk, idx_stat