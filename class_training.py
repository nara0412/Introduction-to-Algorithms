class student:
    
    def __init__(self,inputName,inputNum,inputSex,inputGrade,inputCourse):
        self.name = inputName
        self.num = inputNum
        self.sex = inputSex
        self.grade = inputGrade
        self.courses = inputCourse
    
    def studentInfo(self):
        print("====================\n")
        if self.name is not None:
            print("姓名:",self.name)
        if self.num is not None:
            print("學號:",self.num)
        if self.sex is not None:
            print("性別:",self.sex)
        if self.grade is not None:
            print("年級:",self.grade)
        if self.courses is not None:
            print("修課內容:")
            #for i in self.courses:
                #print(courses.name)
            for i in range(len(self.courses)):
                print(i,":",self.courses[i].name)

        print("====================\n")

class course:
    def __init__(self,coursename,coursetecher,courselocation,coursetime):
        self.name = coursename
        self.teacher = coursetecher
        self.location = courselocation
        self.time = coursetime
    def showinfo(self):
        print("課程資訊:\n===================="
              "\n課程名稱:",self.name,
              "\n授課老師:",self.teacher,
              "\n上課地點:",self.location,
              "\n上課時間:",self.time,
              "\n====================")
        
cours = [None]*5
cours[0] = course("資料結構與演算法實習","周永振","圖212","星期三 03-04") #資料結構與演算法實習
cours[1] = course("資料結構與演算法","周永振","圖212","星期一 06-08") #資料結構與演算法
cours[2] = course("程式設計應用實務","周澤捷","圖213","星期二 06-07") #程式設計應用實務
cours[3] = course("基礎程式設計實習","周永振","圖213","星期五 03-04") #基礎程式設計實習
cours[4] = course("基礎程式設計","周永振","圖213","星期四 05-07") #基礎程式設計

student1 = student("Jimmy","M1105115","男","碩二",cours[0:3])
student2 = student("Alice","D180525",None,"大二",cours[2:5])

student1.studentInfo()
student2.studentInfo()
student1.courses[0].showinfo()