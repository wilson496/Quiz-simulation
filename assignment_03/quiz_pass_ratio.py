import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.




preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

# check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()


passRatioList = []
totalQuestions = 0
length = len(sys.argv) - 1



'''
Loop through each question and continue to do so until the number of 
evaluated questions equals the total number of questions across the XML files
'''

while totalQuestions != quiz_library.compute_question_count(quiz_library.load_quiz_log(sys.argv[length])):
	correctQs = 0.0
	
	for q in sys.argv[1:]:
		count = 0		
		log_string = quiz_library.load_quiz_log(q)
		
		for x in log_string:
		
			if isinstance(x, quiz_library.Answer):	
				if int(x.index) == totalQuestions:
					#print "The result of x is " + str(x.result)					
					if str(x.result) == "1":
						count = 1
		if count == 1:
			correctQs+= 1
	pass_ratio = correctQs/length	
	passRatioList.append(pass_ratio)	
	totalQuestions += 1	
stringy = "" + str(passRatioList[0])
for b in passRatioList[1:len(passRatioList)]:
	stringy = stringy + ',' + str(b)
print stringy
