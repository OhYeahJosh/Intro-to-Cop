#to take course name
def course_name():
	course=input(" The name of the course:")
	return course

#input scores of students
def std_scores(n):
	scores=[]
	for i in range(n):
		scores.append(int(input(" Enter their score:")))
	return scores

#calculating average test score
def calculate_avg(scores):
		sum=0
		for i in range(len(scores)):
			#total scores
			sum=sum+scores[i]
		avg=sum/len(scores)
		return avg

#printing average score	
def print_avg(avg,course):
		print(" The average test score of",course," course is:%.2f"%avg)


#to allow teacher to enter again
while True:
	#3 courses
	for i in range(3):
		#function calls
		course=course_name()
		n=int(input(" How many students took the test:"))
		scores=std_scores(n)
		avg=calculate_avg(scores)
		print_avg(avg,course)
		print("\n")
	#yes or no
	ch=input(" Do you want to continue?(y/n):")
	print()
	if(ch=="y" or ch=="Y"):
		continue	
	else:
			break
