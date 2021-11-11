
"""
@author: Student: Jean Paul
@author : jnishimi
@From MSIT at Carnegie Mellon University
@Date: On 4th October 2021
Description: This module contains one class GradeBook that uses other ctwo classes(Student and Course) from the Course module
             to create a meaning full course information that later used to produce useful information about the situation
             of the courses and the student taking those courses.

More info: I have decided to distribute different files in different folders. For this reason, I just zipped the folders used in codes
           with codes so that it would be easy for TAs to test my codes. 
"""

# imports
from course import Course

class GradeBook:
    # constructor
    def __init__(self):
        self.courses=dict()
        
    # return a course dictionary
    def getCourses(self):
        return self.courses
    
    # take a student roll number and determine whether they are a part of grade book in any of the course
    def find(self,roll_number):
        """
        This method takes a student rollNumber and tell us if the student exists in a grade book or not.
        """
        if len(self.courses) == 0:
            return False
        # I am gon loop in my dictionary finding the roll number given.
        course=list(self.courses.values())[0]
        for student in course.getClasslist():
            if roll_number == student.getRollNum():
                return True
        return False
    
    
    # take a student roll number and write their transcript in a file
    def printTranscript(self, roll_number):
        """
        This function takes a rollNumber argument and saves a student's transcript in
        transcripts/rollNum_transcript.txt file
        """
        if not self.find(roll_number): # if roll number is not in gradebook
            print(f"{roll_number} is invalid")
        else:
            student=self.isStudentValid(roll_number)
            filename=roll_number+"_transcript.txt"
            filewriter=open("transcripts/"+filename,'w')
            filewriter.write(f"{'-'*50}\n")
            filewriter.write(f"{roll_number}   {student.getName()} \n \n")
            for cskey, cs in zip(self.courses.keys(),self.courses.values()):
                if self.isStudentIn(roll_number,cs) != None:
                    student=self.isStudentIn(roll_number,cs)
                    filewriter.write(f"{cs.getCourseID()}   {cs.getCourseName()} {student.percentageGen()}  {student.gradeGen()}\n")
                    continue
            filewriter.write(f"{'-'*50}\n")
            print(f"Transcripts downloaded and saved in transcripts/{filename}")
    
    # ask user to enter valid 5 files of courses and create 5 courses
    def readMultipleCourse(self):
        """
        This function allows to add five courses from five different course files and add them in our courses dictionary.
        The course file contains information about course and the students in that particular course.
        """
        in_files=input("Enter 5 input files as comma separated values: \n")
        files=[file.strip() for file in in_files.split(",")]
        if len(files) != 5:
            return "Five courses wanted"
        for file in files:
            course=Course("default","default","default","default")
            course.addCourseDataFromFile(file)
            self.courses[course.getCourseID()]=course
        print(f"Courses saved from {len(files)} files")
            
    
    # show all student who have passed all registered courses
    def passedStudent(self):
        """
        This function finds the students that passed all of the courses and saves their information in
        passes/passes.txt file. The criteria for passing a course is having above 40 in all courses
        """
        if len(self.courses) == 0:
            print("No courses available")
            return -1
        passed=[]
        passed1=[] #Students passed course1
        passed2=[] #Students passed course2
        passed3=[] #Students passed course3
        passed4=[] #Students passed course4
        passed5=[] #Students passed course5
        i=0
        for lesson in self.courses.values():
            students=lesson.getClasslist()
            for student in students:
                if student.percentageGen() < 40: # I assumed like pass is 40 marks in all assignments'average
                    continue
                if i==0:
                    passed1.append(student.getRollNum())
                    continue
                if i==1:
                    passed2.append(student.getRollNum())
                    continue
                if i==2:
                    passed3.append(student.getRollNum())
                    continue
                if i==3:
                    passed4.append(student.getRollNum())
                    continue
                if i==4:
                    passed5.append(student.getRollNum())
                    continue
            i+=1
        
        # I am gon check who is winning in all courses
        for winner in passed1:
            if winner in passed2 and winner in passed3 and winner in passed4 and winner in passed5:
                passed.append(winner)
       # add a winner in a file
        filename="passes.txt"
        filewriter=open('passes/'+filename,'w')
        for win in passed:
            stName=self.isStudentValid(win).getName()
            filewriter.write(f"{win}  {stName} \n")
        filewriter.close()
        print(f"Passed students are saved in passes/{filename}")
                        
    # generate referrals.txt
    def generateReferrals(self):
        """"
        This function finds the students that failed at-least one course.
        We say a student failed a course if gotten below 40 marks.
        The data generated is saved in referrals/referrals.txt file.
        """
        if len(self.courses) == 0 :
            print("No courses available")
            return -1
        else:
            # getting all students. I use the first course to get them
            students=list()
            i=0
            for course in self.courses.values():
                students=course.getClasslist()
                if i== 0:
                    break
           # Now I have students
           # Time to prepare filewriter and do the job
            filename="referrals.txt"
            filewriter=open("referrals/"+filename,'w')
            failed=list()
            for student in students:
                for course in self.courses.values():
                    st=self.getStudentAndMarksIn(student.getRollNum(),course)
                    if st.percentageGen() < 40:
                        t=(st,course)
                        failed.append(t)
             # I have all failed students and the courses failed in   
            handled=[]
            for outer_fail in failed:
                st=outer_fail[0]
                if st.getRollNum() in handled:
                    continue
                handled.append(st.getRollNum())
                filewriter.write(f"{st.getRollNum()}   {st.getName()} \n") 
                for inner_fail in failed:
                    if inner_fail[0].getRollNum() == st.getRollNum():
                        course=inner_fail[-1]
                        filewriter.write(f"          {course.getCourseID()}  {course.getCourseName()}\n")
            print(f"Referrals students saved in referrals/{filename}")
                 
    # A funtion to generate grades for all students in all courses
    def generateGrades(self):
        """
        This funtion will show grades of all students in all five courses and 
        show the average of the student in all courses. The output of this function
        is stored in grades/grades.txt file path
        """
        if len(self.courses) == 0:
            print("No courses available")
            return -1
        filename="grades.txt"
        filewriter=open("grades/"+filename,'w')
        lessons=list(self.courses.keys())
        filewriter.write(f"rollnum  name         {lessons[0]}  {lessons[1]}  {lessons[2]}   {lessons[3]}   {lessons[4]}  Avg \n \n")
        students_now=list(self.courses.values())[0].getClasslist()
        students_rolnum=[i.getRollNum() for i in students_now]
        students_rolnum.sort()
        course_ids=list(self.courses.keys())
        saveStudents=list()
        saveAvg=list()
        for course_id,itr in zip(course_ids,range(len(course_ids))):
            for st in self.courses.get(course_ids[itr]).getClasslist():
                if st.getRollNum() == students_rolnum[itr]:
                    filewriter.write(f"{students_rolnum[itr]}    {self.isStudentIn(students_rolnum[itr],self.courses.get(course_ids[itr])).getName()}    ")
                    st_marks=[]
                    for inner_cours in course_ids:
                        st_marks.append(self.isStudentIn(st.getRollNum(),self.courses.get(inner_cours)).percentageGen())
                        filewriter.write(f"{st_marks[-1]}  ")
                    sum_marks=0
                    for mark in st_marks:
                        sum_marks+=mark
                    saveStudents.append(self.isStudentIn(st.getRollNum(),self.courses.get(inner_cours)))
                    saveAvg.append(sum_marks/len(st_marks))
                    avg=sum_marks/len(st_marks)
                    filewriter.write("{:.2f} \n".format(avg))
        maximum=saveAvg[0]
        best_st=saveStudents[0]
        for i in range(len(saveAvg)):
            if saveAvg[i]>maximum:
                maximum=saveAvg[i]
                best_st=saveStudents[i]
        filewriter.write("\n \nBest Student "+best_st.getRollNum()+", "+best_st.getName()) # Displaying the best student
        print(f"Grades are saved in grades/{filename}")
        
    # Generate a general transcript
    def generateOverallTranscript(self):
        """
        This method generates a transcript for all students and store them in a single file one student below another.
        The file is stored in general_transcript/transcripts.txt
        """
        if len(self.courses) == 0:
            print("No courses available")
            return -1
        filename="transcripts.txt"
        filewriter=open("general_transcript/"+filename,'w')
        students=list(self.courses.values())[0].getClasslist()
        students_rolnum=[i.getRollNum() for i in students]
        students_rolnum.sort()
        # I am gon loop in courses
        helper_courses=self.courses.values()
        student_name=""
        i=0
        for outer_course in self.courses.values():
            student_name=self.isStudentValid(students_rolnum[i]).getName()
            filewriter.write(f"{'-'*50} \n") 
            filewriter.write(f"{students_rolnum[i]}   {student_name} \n \n")
            student=None
            for inner_course in helper_courses:
                student=self.getStudentAndMarksIn(students_rolnum[i],inner_course)
                filewriter.write(f"{inner_course.getCourseID()}  {inner_course.getCourseName()}  {student.percentageGen()}  {student.gradeGen()} \n")
            filewriter.write(f"{'-'*50} \n \n")  
            i+=1
        print(f"All students' trascripts is stored in general_transcript/{filename}")
        
        
    # Function to take a course Id and print all students in a course with their grades
    def generateStudentsInfoInCourse(self,courseId):
        """
        This function takes a course id and give information of all students in a course
        The data are saved in courses_grades/courseId_grades.txt file
        """
        if len(self.courses) == 0:
            print("No courses available")
            return -1
        if not self.courseExists(courseId):
            print("This is invalid course ID.")
            return -1
        else:
            for id in self.courses.keys():
                if id == courseId:
                    filename=courseId+"_grades.txt"
                    filewriter=open("courses_grades/"+filename, 'w')
                    course=self.courses.get(id)
                    students=course.getClasslist()
                    for student in students:
                        filewriter.write(f"{student.getRollNum()}  {student.getName()}  {student.percentageGen()}  {student.gradeGen()} \n")
                    print(f"courses_grade file is stored in courses_grades/{filename} ")
         
    #MY HELPER FUNCTION (MY UTIL)
    # helper function to tell me if a student is in the course
    def isStudentIn(self, roll_number, course):
        for st in course.getClasslist():
            if roll_number == st.getRollNum():
                return st
        return None
    
    #helper function to return a student if exist
    def isStudentValid(self, roll_number):
        cs=list(self.courses.values())[3]
        for st in cs.getClasslist():
            if st.getRollNum() == roll_number:
                return st
        return None
    
    #hepler function to get marks of a student in a certain course
    def getStudentAndMarksIn(self, roll_num, course):
        if self.isStudentIn(roll_num,course) == None:
            return False, " A student is not part of the course"
        else:
            for st in course.getClasslist():
                if st.getRollNum() == roll_num:
                    return st
         
    # Helper helps to know if a course Id exists in a dictionary
    def courseExists(self,id):
        if id in self.courses.keys():
            return True
        return False
        
#You may define any additional claases or functions below this comment.

##########################################################################



def testGradeBook():
    """
    Your code to initiate GradeBook and generate the required output files.
    """
    grade=GradeBook()
    
    # Demonstrating a function to read multiple course from course files and add data in the courses dictionary
    grade.readMultipleCourse()
    print()
    print(" ---------------------------------------------------------------------------------")
    print("| All files are auomatically generated in their respective folders. Check the out |")
    print(" --------------------------------------------------------------------------------- \n")
    
    # Testing printTranscript(student_roll_num) of a student
    grade.printTranscript('S1006')
    grade.printTranscript('S1003')
    print()
    
    # Demostrate passedStudent() that show the list of all students that passed all of their courses.
    grade.passedStudent()
    print()
    
    # demonstrate generateReferrals() that shows all students who failed at least a course.
    grade.generateReferrals()
    print()
    
    # demonstrate grade.generateGrades() that shows each student’s score per course, the average score and the best student.
    grade.generateGrades()
    print()
    
    # Demonstrate grade.generateOverallTranscript() that prints all students transcripts
    grade.generateOverallTranscript()
    print()
    
    # Demonstrate grade.generateStudentsInfoInCourse(courseId) that shows all students of a particular course with their scores
    grade.generateStudentsInfoInCourse('04808E')
    print()
    
    
def main():
    if __name__=="__main__":
        testGradeBook()
    else:
        print("Not in grades' file to see the resu.")
           
main()
    
    