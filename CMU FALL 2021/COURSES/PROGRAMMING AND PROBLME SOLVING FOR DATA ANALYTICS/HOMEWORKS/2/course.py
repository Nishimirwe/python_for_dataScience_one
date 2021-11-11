# -*- coding: utf-8 -*-
"""
This module contains classes to be used for Question 2 of the assignment.

@author: Prof: George and Student: Jean Paul
@Andrew ID of Jean Paul: jnishimi
@From MSIT at Carnegie Mellon University
@Date: On 4th October 2021

"""


class Student:
    """
    Student class definition.
    data members: 
        __rollNum, __name, __marks (from five homework assignments): list of marks 
    Each student does 5 homework assignments
    """

    #method definitions
    def __init__(self, rollNum='',name=''):
        """
        Sets up a Student object
        """
        self.__rollNum=rollNum
        self.__name=name
        self.__marks=[]
        
    #getters/accessors
    def getName(self):
        return self.__name
    def getRollNum(self):
        return self.__rollNum
    def getMarks(self):
        return self.__marks
    
    #mutators
    def setName(self,name):
        self.__name=name
    def setRollNum(self, rollNum):
        self.__rollNum=rollNum
    def setMarks(self, marks):
        """
        Sets up homework scores- a list of 5 or less values.
        """
        self.__marks=marks

    def addMark(self, mark):
        """
        Adds a single mark to the list of marks

        """
        self.__marks.append(mark)
        
    def percentageGen(self):
        """
        computes and returns the percentage score.
        """
        return sum(self.__marks)/5
        
    def gradeGen(self):
        """
        Computes and returns the grade.
        """
        
        #compute the percentage
        percentage=self.percentageGen()
        #compute the grade
        grade=''
        if percentage>=90:
            grade="A"
        elif percentage>=80:
            grade="B"
        elif percentage>=65:
            grade="C"
        elif percentage>=40:
            grade="D"
        else: 
            grade="E"
        #return the grade
        return grade
            
    def __str__(self):
        """
        Returns a string representation of a Student object
        """
        return f"Name:{self.__name}\nRoll Num:{self.__rollNum}\nMarks:\
            {str(self.__marks)}\nPercentage:{str(self.percentageGen())}\
                \nGrade:{self.gradeGen()}"
 


#######################################################################

class Course:
    """
    A class that keeps track of course name, semester, TAs and 
    maintains a list of students in the course. 
    
    @author: George
    """
    def __init__(self, courseID='', courseName='',instructor='',semester=''):
        """
        Sets up the instance variables
        __courseID, __courseName,__instructor,__semester: are all strings
        """
        self.__courseID=courseID
        self.__courseName=courseName
        self.__instructor=instructor
        self.__semester=semester
        #these below will be added by methods
        self.__courseTAs=[]
        self.__classlist=[]
             
    #accessors
    def getCourseID(self):
        return self.__courseID
    def getCourseName(self):
        return self.__courseName
    def getInstructor(self):
        return self.__instructor
    def getSemester(self):
        return self.__semester
    def getCourseTAs(self):
        return self.__courseTAs
    def getClasslist(self):
        return self.__classlist
    
    #mutators
    def setCourseID(self, courseID):
        self.__courseID=courseID
    def setCourseName(self, courseName):
        self.__courseName=courseName
    def setInstructor(self,instructor):
        self.__instructor=instructor
    def setSemester(self,semester):
        self.__semester=semester
    def setCourseTAs(self, courseTAs):
        self.__courseTAs=courseTAs
    def setClasslist(self, classlist):
        self.__classlist=classlist
        
    def addStudent(self,student):
        """
        Receives a Student object and adds it to the classlist.
        """
        self.__classlist.append(student)
        
    def addTA(self,ta_name):
        """
        Receives a TA name and adds it to the list of TAs.
        """
        self.__courseTAs.append(ta_name)
        
    def computeClassAverage(self):
        """
        Accesses all Student objects, computes each students average
        and then computes the class everage.
        """
        sum=0 #running
        for student in self.__classlist:
            sum+=student.percentageGen()
            
        return sum/len(self.__classlist)
    

    def addStudentsFromFile(self, filename):
        """
        #Adds students from file
        Parameters: filename, a file path
        """
        filereader=open(filename)
        lines=filereader.readlines()
        for line in lines:
            line=line.strip('\n')
            rollno,name,*hwk=line.split(':')
            #Convert homework into numbers
            marks=[eval(mark) for mark in hwk]
            #create a student
            student=Student(rollno,name)
            #set the marks
            student.setMarks(marks)
            #add to list
            self.addStudent(student)
        #close file
        filereader.close()   
       
    #Student class definition ends here.
    
          
    def addCourseDataFromFile(self, filename):
        """
        #Adds students from file
        Parameters: filename, a file path
        """
        filereader=open(filename)
        lines=filereader.readlines()
        i=0
        for line in lines:
            if i==0:
                self.__courseID=line.strip()
            elif i== 1:
                self.__courseName=line.strip()
            elif i==2:
                self.__semester=line.strip()
            elif i==3:
                self.__instructor=line.strip()
            elif i==4:
                TAS=line.split(",")
                for TA in TAS:
                    self.addTA(TA.strip())
            else: 
                line=line.strip('\n')
                rollno,name,*hwk=line.split(':')
                #Convert homework into numbers
                marks=[eval(mark) for mark in hwk]
                #create a student
                student=Student(rollno,name)
                #set the marks
                student.setMarks(marks)
                #add to list
                self.addStudent(student)
            i+=1
            
        #close file
        filereader.close()
        
    def printCourseDetails(self, filename):
        """
        Receives an output file name and outputs course details
        """
        filewriter=open(filename,'w')
        filewriter.write(f"{'*'*50}\nCourse ID:{self.__courseID}\
        \nCourse:{self.__courseName}\nInstructor:{self.__instructor}\
        \nSemester:{self.__semester}\nTAs:{self.__courseTAs}\n{'*'*50}\n\n")
            
        #Retrieve each student extract the details, compute the average and grade
        #and output rollNum, name, percentage mark, and grade to file.
        for student in self.__classlist:
            #compute the percentage mark
            percentage=student.percentageGen()
            #compute grade
            grade=student.gradeGen()
            filewriter.write(f"{student.getRollNum():8s}{student.getName():20s}\
            {percentage:8.2f} {grade:3s}\n")
        #Output class average
        filewriter.write(f"\n{'-'*25}\nClass Average:{self.computeClassAverage():8.2f}\n{'-'*25}\n")
        
        #close file    
        filewriter.close()
    
        
    def __str__(self):
        """
        Returns a string representation of a Course object
        """
        return f"{'**'*20}\nCourse:{self.__courseName}\nInstructor:{self.__instructor}\
                \nSemester:{str(self.__semester)}\nTAs:{str(self.__courseTAs)}\
                    \n{'**'*20}"
    
    

#Course class definition ends.

"""     
#create student
student=Student()
student.setRollNum('s1010')
student.setName('Yam Foo Foo')
student.setMarks([20,60,80,34,90])


print(student)
#create course
course=Course()
#add student
course.addStudent(student)

#create another student
student2=Student('s1007','Greg Gregory')
student2.setMarks([100,100,90,70,80])
#add student
course.addStudent(student2)
print(course)
list=course.getClasslist()
for student in list:
    print(student)



course2=Course()
course2.addStudentsFromFile('data.txt')
course2.printCourseDetails('results.txt')

"""