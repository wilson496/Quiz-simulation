import libxml2
import sys

'''
purpose
	store the information from an answer element
'''


class Answer:
    def __init__(self, index, path, result, answer, time):
        self.index = index
        self.path = path
        self.result = result
        self.answer = answer
        self.time = time


'''
purpose
	Store the information from a display element.
'''


class Display:
    def __init__(self, index, path, time):
        self.index = index
        self.path = path
        self.time = time


'''
purpose
	Extract the information from log_file and return it as a list
	of answer and display objects.
preconditions
	log_file is the name of a legal, readable quiz log XML file
'''


def load_quiz_log(log_file):
    # parse the XML file in argv[1] and load it into memory
    parse_tree = libxml2.parseFile(log_file)

    # create a context for tree traversal
    context = parse_tree.xpathNewContext()

    # get the root of the tree
    root = parse_tree.getRootElement()

    # iterate over children of root, storing result in assignment dictionary
    dA = root.children

    # iterate over the children

    displayAnswer = []

    index, path, result, answer, time = None, None, None, None, None

    while dA is not None:

        child = dA.children

        if dA.name == "display":
            while child is not None:

                if child.name == "index":
                    if child.content == None:
                        index = None
                    else:
                        index = int(child.content)

                elif child.name == "path":
                    path = child.content

                elif child.name == "time":
                    if child.content == None:
                        time = None
                    else:
                        time = int(child.content)
                child = child.next
            storeD = Display(index, path, time)
            displayAnswer.append(storeD)

        if dA.name == 'answer':
            while child is not None:
                if child.name == "index":
                    if child.content.isdigit():
                        index = int(child.content)
                    else:
                        index = None

                elif child.name == "path":
                    path = child.content

                elif child.name == "time":
                    if child.content.isdigit():
			time = int(child.content)                        
                    else:
                        time = None

                elif child.name == "answer":
                    if child.content == '':
                        answer = None
                    else:
                        answer = child.content

                elif child.name == "result":
                    if child.content.isdigit():
                        result = int(child.content)
                    else:                        
			result = None
                child = child.next

            storeA = Answer(index, path, result, answer, time)
            displayAnswer.append(storeA)

    	dA = dA.next
    
    return displayAnswer


'''
purpose
	Return the number of distinct questions in log_list.
preconditions
	log_list was returned by load_quiz_log
'''


def compute_question_count(log_list):
    eL = []

    for x in log_list:
	       
	if x.index not in eL:		
		eL.append(x.index)     
    return len(eL)


'''
purpose
	Extract the list of marks.
	For each index value, use the result from the last non-empty answer,
	or 0 if there are no non-empty results.
preconditions
	log_list was returned by load_quiz_log
'''


def compute_mark_list(log_list):
    
	markList = [0] * compute_question_count(log_list)

	for x in log_list:

		if isinstance(x, Answer):

			if x.result is not None:

				markList[x.index] = x.result 

	return markList			
