import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.
	For each log file
		write to standard output the course mark for the log file,
		in CSV format
preconditions
	Each command-line argument is the name of a legal, readable quiz log file.

	All of the log files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

for q in sys.argv[1:]:
	
		
	
	string = quiz_library.load_quiz_log(q)
		
	L = quiz_library.compute_mark_list(string)
	
	b = reduce(lambda x, y: x + y, L)		

	print q + "," + str(b)

