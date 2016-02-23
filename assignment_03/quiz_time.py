import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

times = [0] * 4


#iterate through each file name and therefore each file on the command line
for quiz in sys.argv[1:]:
	
	log_file = quiz_library.load_quiz_log(quiz)
	num_q = quiz_library.compute_question_count(log_file)
	disp = None
	ans = None
	La = [l for l in log_file if isinstance(l, quiz_library.Display)]
	
	for x, y in enumerate(La):
		disp = ans 
		ans = y
		
		if disp == None:
			continue
		times[disp.index] += ans.time - disp.time  
		if x == len(La) - 1:
			disp = ans			
			ans = log_file[-1]
			times[disp.index] += ans.time - disp.time
			
#list comprehension to do average	

final = [float(b)/2 for b in times]

 
#print the list as CSV

	
st = "" + str(final[0])
for b in final[1:len(final)]:
	st = st + ',' + str(b)
print st

