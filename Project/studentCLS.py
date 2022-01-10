#학생 클래스 구현
class student:
    
    #클래스 변수
    #학생 데이터 저장 <클래스 변수>
    DB = []
    count = 0
    #클래스 함수

    #정보 조회 함수 <클래스 함수>
    @classmethod
    def report(cls):
        printStr = ""
        print("이름\t학년\t반\t번호\t성별\t학번\t국어\t수학\t영어\t과학")
        for stu in student.DB:
            printStr += stu.selfInfoReport()
        return printStr

    #정보 검색 함수 <클래스함수>
    @classmethod
    def searchInfo(cls, searchHakbun):
        for inst in student.DB:
            if (searchHakbun == inst.hakbun):
                print("정보를 찾았습니다.")
                return inst
        #찾는값없을때
        print("정보를 못찾았습니다.")
        return 0 #예외 처리 해줄것@@@@@@@@@@@

    #3. 학생 정보 삭제@@@@@@@@(미구현)
    @classmethod
    def removeInfo(cls, serchedInst):
        print(serchedInst.selfInfoReport())
        chk = bool(input("찾으시는 정보가 맞습니까? (예:0/아니오:1)"))
        if chk == True:
            return 0
        else:
            print("{}님의 정보를 제거합니다.".format(searchedInst.name))
            student.DB.remove(searchedInst)
        
    
        
    #인스턴스 함수
    #생성자 <인스턴스 함수>
    def __init__(self, name, year, group, num, sex, korean, math, english, science):

        #기본정보
        self.name = name
        self.year = year
        self.group = group
        self.num = num
        self.sex = sex
        
        #성적
        """self.korean = korean
        self.math = math
        self.english = english
        self.science = science"""
        self.scoreBox = [korean, math, english, science, 0.0, 0.0]

        #성적표를 위한 변수 scoreBox[5] = 전체 총합, scoreBox[4] = 전체 평균
        self.scoreBox[5] = self.scoreBox[0] + self.scoreBox[1] + self.scoreBox[2] + self.scoreBox[3]
        self.scoreBox[4] = float(self.scoreBox[5] / 4)
        self.yearRank = 1 #학년 석차는 저장
        self.classRank = 1 #학년 석차는 저장

        #학번 생성하기
        self.hakbun = str(year) \
            + ( str(group) if str(group) == 1 else str(group).zfill(2) ) \
                + ( str(num) if str(num) == 1 else str(num).zfill(2) )
        
    def selfInfoReport(self):
        return "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(self.name, \
        self.year, self.group, self.num, self.sex, self.hakbun, self.scoreBox[0], self.scoreBox[1], self.scoreBox[2], \
        self.scoreBox[3])

    #2. 학생 정보 수정
    def modifyInfo(self):
        print("이름\t학년\t반\t번호\t성별\t학번\t국어\t수학\t영어\t과학")
        print(self.selfInfoReport())
        print("수정할 정보를 입력하세요.")
        chk = int(input("인적사항(0)\t성적(1)"))
        if (chk):
            chk1 = int(input("국어(0)\t수학(1)\t영어(2)\t과학(3)"))
            if(chk1 == 0):
                temp = float(input("국어점수 입력:"))
                self.scoreBox[chk1] = temp
            elif(chk1 == 1):
                temp = float(input("수학점수 입력:"))
                self.scoreBox[chk1] = temp
            elif(chk1 == 2):
                temp = float(input("영어점수 입력:"))
                self.scoreBox[chk1] = temp
            elif(chk1 == 3):
                temp = float(input("과학점수 입력:"))
                self.scoreBox[chk1] = temp
            else:
                print("잘못 입력하셨습니다.")
                return
        else:
            chk1 = int(input("이름(0)\t학년(1)\t반(2)\t번호(3)\t성별(4)"))
            if(chk1 == 0):
                temp = input("이름 재입력:")
                self.name = temp
            elif(chk1 == 1):
                temp = int(input("학년 재입력:"))
                self.year = temp
            elif(chk1 == 2):
                temp = int(input("반 재입력:"))
                self.group = temp
            elif(chk1 == 3):
                temp = int(input("번호 재입력:"))
                self.num = temp
            elif(chk1 == 4):
                temp = input("성별 재입력:")
                self.sex = temp
            else:
                print("잘못 입력하셨습니다.")

    #석차 매기기 함수(학년 / 학급)

    #학년 석차 구하기
    def arrangeYearRank(self, Chk):
        rankNum = 1
        yearRankArray = []
        stuCount = 0 #학년 학생수 카운트
        for inst in student.DB:
            if inst.hakbun[0] == self.hakbun[0]:
                stuCount += 1
                yearRankArray.append(inst.scoreBox[Chk])
        
        for i in yearRankArray:
            if i > self.scoreBox[Chk]:
                rankNum += 1
        
        self.yearRank = rankNum #학년 석차는 저장 -> 
        return rankNum, stuCount

    def arrangeClassRank(self, Chk):
        rankNum = 1
        classRankArray = []
        stuCount = 0 #반 학생수 카운트
        #학급 석차 구하기
        for inst in student.DB:
            if inst.hakbun[0:3] == self.hakbun[0:3]:
                stuCount += 1
                classRankArray.append(inst.scoreBox[Chk])

        for i in classRankArray:
            if i > self.scoreBox[Chk]:
                rankNum += 1
        
        return rankNum, stuCount

    #등급매기기
    def calcGrade(self, stuNum): 
        gradeA = float(self.yearRank) / float(stuNum)
        if gradeA > 0.96:
            return 1
        elif gradeA > 0.89:
            return 2
        elif gradeA > 0.77:
            return 3
        elif gradeA > 0.60:
            return 4
        elif gradeA > 0.40:
            return 5
        elif gradeA > 0.23:
            return 6
        elif gradeA > 0.11:
            return 7
        elif gradeA > 0.04:
            return 8
        else:
            return 9
    
    #5. 성적표 출력 / 통계
    def printReportCard(self):
        print("{} {}님의 성적표입니다.".format(self.hakbun, self.name))
        print("-----------------------------------------------------------------------")
        print("\t점수\t학급석차\t학년석차\t과목평균\t등급\t")
        print("-----------------------------------------------------------------------")
        for i in range(5):
            title = " "
            if(i == 0) : title = "국어"
            elif(i == 1) : title = "수학"
            elif(i == 2) : title = "영어"
            elif(i == 3) : title = "과학"
            elif(i == 4) : title = "평균"
            self.classRank, classStudentNum = self.arrangeClassRank(i)
            self.yearRank, yearStudentNum = self.arrangeYearRank(i)
            print("{}\t{}\t{}\t\t{}\t\t{}\t{}".format(title, self.scoreBox[i], str(self.classRank) + " / " + str(classStudentNum), \
                str(self.yearRank) + " / " + str(yearStudentNum), 0, self.calcGrade(yearStudentNum)))