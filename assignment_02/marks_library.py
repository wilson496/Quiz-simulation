# Cameron Wilson (V00822184)
# November 7th, 2015
import libxml2
import sys

'''
purpose
	return the course mark for student s
preconditions
	student is a list of the form:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [mark_id,score], ... ]
	assignments is a dictionary of the form:
		{mark_id:[points, percentage], ... }
'''
def compute_mark(student, assignments):
	
	courseMark = 0
	#iterate through the assignment marks that the student has achieved. Use the 
	# assignment id as the key in the assignment dictionary
	for x in student[3]:			
		studentAssignMark = float(x[1])
		totalAssignMark = float(assignments[x[0]][0])
		percentWeight = float(assignments[x[0]][1]) / 100
		courseMark += (studentAssignMark / totalAssignMark) * percentWeight 
	return courseMark * 100
		
'''
purpose
	extract the information from a and return it as a list:
		[mark_id, points, percentage]
preconditions
	s is an assignment element from a legal students XML file
'''
def extract_assignment(a):

	assignExtractList = ['mark_id', 'points', 'percentage']
	
	#until you reach the end of the XML file, determine whether each value is the 
	# mark_id, points value, or the percentage weight of the assignment
	while a is not None:
		
		if a.name == 'mark_id': 
			assignExtractList[0] = a.content	
		elif a.name == 'points':
			assignExtractList[1] = int(a.content) 	
		elif a.name == 'percentage':
			assignExtractList[2] = float(a.content)
		
		a = a.next
		
	return assignExtractList

'''			
	
purpose
	extract the information from s and return it as a list:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
preconditions
	s is a student element from a legal students XML file
'''
def extract_student(s):
	
	fullList = ['last_name', 'first_name', 'student_id', 'marks']
	marksList = [] 
	#iterate through each student 
	while s is not None:	
		
		if s.name == 'last_name':
			fullList[0] = s.content
		elif s.name == 'first_name':
			fullList[1] = s.content
		elif s.name == 'student_id':
			fullList[2] = s.content
		elif s.name == 'marks':
			marks = s.children
		#iterate through the list of the lists of marks for each assignment
			while marks is not None:  
				inMarks = marks.children
				assignMarks = [None, None]
				#iterate through the specific mark_id with their respective scores and place them in a list
				while inMarks is not None:
					
					if inMarks.name == 'mark_id':
						assignMarks[0] = inMarks.content
					
					elif inMarks.name == 'score':
						assignMarks[1] = int(inMarks.content)
								
					inMarks = inMarks.next	
				#Place the lists with the specific assignment_id's and the scores in the larger list of all assignment scores
				if None not in assignMarks:
					marksList.append(assignMarks)
					
								
				
				marks = marks.next					
			
		s = s.next
		#put the assignment scores with the full list of the student's first name, last name, and student id		
		fullList[3] = marksList
	return fullList


