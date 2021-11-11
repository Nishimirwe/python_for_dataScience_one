
"""
@author : <pmanzi
@date:10/5/2021
Description: <convas-name: professor manzi>
"""
from course import Course

class GradeBook:
    #replace pass with your code that defines GradeBook as per the instructions.

    #You may define any additional claases or functions below this comment.
    
    def __init__(self):
        self.courses={}
        
    def getCourses(self):
        return self.courses

    def readFromFiveFiles(self):
        #getting inputs
        files_input = input ("Enter 5 comma separated files: ")
        splt_files = files_input.split (",")
        
        files = [file.strip() for file in splt_files]
        for filename in files:
            course=Course("","","","")
            course.addCourseDataFromFile(filename)
            self.courses[course.getCourseID()]=course
            
    def find(self, rollNum):
        one_course=self.courses.values()
        one_course=list(one_course)
        one_course=one_course[0]
        students=one_course.getClasslist()
        rollNums=[st.getRollNum() for st in students]
        if rollNum in rollNums:
            return True
        return False
            
    def printTranscript(self,rollNum):
        if not self.find(rollNum):
            return "Invalid student"
        courses=self.courses.values()
        student_course_marks=[]
        for course in courses:
            students=course.getClasslist()
            for student in students:
                if student.getRollNum() == rollNum:
                    student_course_marks.append((course, student))
        
        # printing data
        if len(student_course_marks) !=0:
            toFile=open(rollNum+"_transcript.txt",'w')
            toFile.write(f"{self.giveMeStudent(rollNum).getRollNum()}   {self.giveMeStudent(rollNum).getName()}\n \n")
            for data in student_course_marks:
                toFile.write(f"{data[0].getCourseID()}   {data[0].getCourseName()}  {data[1].percentageGen()}  {data[1].gradeGen()}\n")
            print("Transcript saved")
            toFile.close()
        else:
            print("Student not found")
            
            
    # functions to give students passed all of the courses
    def passes(self):
        courses=list(self.courses.values())
        students=courses[0].getClasslist()
        passed_students=set()
        failed_students=set()
        for student in students:
            for c in courses:
                c_sts=c.getClasslist()
                for c_st in c_sts:
                    if c_st.getRollNum() == student.getRollNum():
                        if(c_st.percentageGen() < 40):
                            failed_students.add(c_st.getRollNum())
            if student.getRollNum() not in failed_students:
                if student not in passed_students:
                    passed_students.add(student)
        
        # write in a file
        toFile=open("passes.txt",'w')
        st_roll_list=[i.getRollNum() for i in passed_students]
        st_roll_list=sorted(st_roll_list)
        for i in st_roll_list:
            toFile.write(f"{self.giveMeStudent(i).getRollNum()}   {self.giveMeStudent(i).getName()} \n")
        print("Passes saved")
        toFile.close()
        
    # Referrals
    def referrals(self):
        courses=list(self.courses.values())
        students=courses[0].getClasslist()
        failed_students=set()
        for student in students:
            for c in courses:
                c_sts=c.getClasslist()
                for c_st in c_sts:
                    if c_st.getRollNum() == student.getRollNum():
                        if(c_st.percentageGen() < 40):
                            failed_students.add(c_st.getRollNum())
                            break
        toFile=open("referrals.txt", 'w')
        sorted_roll_nums=sorted(failed_students)
        all_courses=list(self.courses.values())
        for i in sorted_roll_nums:
            toFile.write(f"{self.giveMeStudent(i).getRollNum()}   {self.giveMeStudent(i).getName()} \n")
            for course in all_courses:
                for course_st in course.getClasslist():
                    if course_st.getRollNum() == self.giveMeStudent(i).getRollNum():
                        if course_st.percentageGen() < 40:
                            toFile.write(f"          {course.getCourseID()}   {course.getCourseName()} \n")
                            break
        print("Referrals saved")
        toFile.close()
            
                        
    # Generate grades
    def grades(self):
        students=list(self.courses.values())[0].getClasslist()
        toFile=open("grades.txt",'w')
        toFile.write(f"rollNum    StudentName   {list(self.courses.values())[0].getCourseID()}  {list(self.courses.values())[1].getCourseID()} {list(self.courses.values())[2].getCourseID()}  {list(self.courses.values())[3].getCourseID()}    {list(self.courses.values())[4].getCourseID()}   Avg \n \n")
        students_with_marks=[]
        for student in students:
            student_marks=list()
            for course in self.courses.values():
                sts_course=course.getClasslist()
                for st in sts_course:
                    if st.getRollNum() == student.getRollNum():
                        student_marks.append(st.percentageGen())
                        break
            s = 0
            for mark in student_marks:
                s+=mark
            students_with_marks.append((student,s))
            toFile.write(f"Best Student: {student.getRollNum()}  {student.getName()}   {student_marks[0]}   {student_marks[1]}   {student_marks[2]}   {student_marks[3]}   {student_marks[4]}   {s/5} \n")
        # find the best student
        su=students_with_marks[0][1]
        stu=students_with_marks[0][0]
        for t in students_with_marks:
            if t[1] > su:
                su=t[1]
                stu=t[0]
        toFile.write(f"\n{stu.getRollNum()}   {stu.getName()}   {su/5}")
        print("Grades saved")  
        toFile.close()


    def transcripts(self):
        students=list(self.courses.values())[0].getClasslist()
        toFile=open("transcripts.txt",'w')
        for student in students:
            toFile.write("----------------------------------------------- \n")
            toFile.write(f"{student.getRollNum()}   {student.getName()} \n \n")
            for course in list(self.courses.values()):
                for i in course.getClasslist():
                    if student.getRollNum() == i.getRollNum():
                        toFile.write(f"{course.getCourseID()}   {course.getCourseName()}  {i.percentageGen()}   {i.gradeGen()}\n")
                        break
            toFile.write("----------------------------------------------- \n")
        print("Transcripts are saved")
        
    def courseGrade(self,course):
        if not course in self.courses.keys():
            return "Invalid course"
        wanted=self.courses.get(course)
        toFile=open(course+"_grades.txt",'w')
        for student in wanted.getClasslist():
            toFile.write(f"{student.getRollNum()}   {student.getName()}    {student.percentageGen()}   {student.gradeGen()} \n")
        print("Course grade saved")
        toFile.close()

    def giveMeStudent(self,roll):
        if len(self.courses) == 0:
            return "Empty"
        course=list(self.courses.values())[0]
        for student in course.getClasslist():
            if student.getRollNum() == roll:
                return student
    
    #def showCourses(self):
     #   for key in self.courses.keys():
     #      print(f"{self.courses.get(key).getClasslist()}")
    
        
##########################################################################


def testGradeBook():
    """
    Your code to initiate GradeBook and generate the required output files.
    """
    grade=GradeBook()
    grade.readFromFiveFiles()
    grade.printTranscript('S1002')
    grade.printTranscript("S1000")
    grade.passes()
    grade.referrals()
    grade.grades()
    grade.transcripts()
    grade.courseGrade("0444E")
    
testGradeBook()

