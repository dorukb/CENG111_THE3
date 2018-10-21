def place_words(corpus):
	grid_size = len(corpus[0])
	grid = []
	n = 0
	corp_size = len(corpus)
	return place(corpus,corp_size,n,grid,grid_size)
	
def place(corpus,corp_size,n,grid,grid_size):
	if n > grid_size-1:
		return True
	i = 0
	while i < corp_size:
		item = corpus[i]
		grid.append(item)
		if grid_is_ok(item,grid,corpus) and place(corpus,corp_size,n+1,grid,grid_size):return grid
		else:
			grid.pop()
			i+=1
	return False
	
def in_corpus(query,corpus,grid,j):
	corpus_size = len(corpus)
	for i in range(0,corpus_size):
		if query in corpus[i][0:j+1] and corpus[i] != grid:
			return True
	return False

def grid_is_ok(current,grid,corpus):
	item_size = len(current)
	grid_size = len(grid)
	n=0;j=0
	for j in range(0,grid_size):
		for k in range(0,item_size):
			query =""
			for q in range(0,grid_size):
				query=query + grid[q][k]
			if in_corpus(query,corpus,grid[j],j):
				n += 1			
	if n >= item_size:
		return True
	return False
	
