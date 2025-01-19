# You are allowed to import any modules whatsoever (not even numpy, sklearn etc)
# The use of file IO is forbidden. Your code should not read from or write onto files

# SUBMIT YOUR CODE AS TWO PYTHON (.PY) FILES INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILES MUST BE index.py and execute.py

# DO NOT CHANGE THE NAME OF THE METHODS my_execute BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to create indices or statistics
def year_positions(year, operator, yearmap):
    positions = []
    max_year = len(yearmap) - 1
    if operator == '=':
        if 0 <= year <= max_year:
            positions.extend(yearmap[year])
    elif operator == '>=':
        for y in range(year, max_year + 1):
            positions.extend(yearmap[y])
    elif operator == '<=':
        for y in range(0, min(year, max_year) + 1):
            positions.extend(yearmap[y])
    return positions
def get_name_positions(name_index, name, operator):
    if operator == '=':
        return name_index.search(name.strip('"'))
    else :
        return name_index.starts_with(name.strip('"').rstrip('%'))
def process_predicate(predicate, name_index, yearmap):
    field, operator, value = predicate
    if field == 'name':
        positions = get_name_positions(name_index, value.lower(), operator)
    else :
        positions = year_positions(int(value), operator, yearmap)
    return set(positions)
################################
# Non Editable Region Starting #
################################
def my_execute( clause, idx ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to take a WHERE clause specification
	# and return results of the resulting query
	# clause is a list containing either one or two predicates
	# Each predicate is itself a list of 3 objects, column name, comparator and value
	# idx contains the packaged variable returned by the my_index method
	
	# THE METHOD MUST RETURN A SINGLE LIST OF INDICES INTO THE DISK MAP
    name_index, yearmap = idx
    results = [process_predicate(condition, name_index, yearmap) for condition in clause]
    diskloc_list=sorted(set.intersection(*results)) if results else []
    return diskloc_list