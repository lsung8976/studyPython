#2021 - 1학기 파이썬 프로젝트(학생정보시스템 만들기)

#Student 클래스 임포트
from studentCLS import *
import random

#학생 기본정보 입력하는 함수 --> 반환값 : 인스턴스
def inputHelper():  
    tempName = input("학생 이름을 입력하세요:")
    tempYear = int(input("학년을 입력하세요"))
    tempGroup = int(input("반을 입력하세요"))
    tempNum = int(input("번호을 입력하세요"))
    tempSex = input("성별을 입력하세요")
    tempKorean = int(input("국어점수를 입력하세요"))
    tempMath = int(input("수학점수를 입력하세요"))
    tempEnglish = int(input("영어점수를 입력하세요"))
    tempScience = int(input("과학점수를 입력하세요"))
    return student(tempName, tempYear, tempGroup, tempNum ,tempSex, tempKorean, tempMath, tempEnglish, tempScience)
    #student.DB.append()  -- 삭제부분

#랜덤 데이터 생성
def makeRandomData(maxYear = 3, maxGroup = 5, maxNum = 39):
    sList = ["남", "여"]
    sung = list("김이박최정강조윤장임한오")
    hanguls = ["가경", "강규", "강근", "강모", "강민", "강백", "강태", "강택", "강필", "건도", "건모", "건표", "경규", "경균", "경남", "경대", "경도", "경륜", "경모", "경무", "경백", "경복", "경빈", "경율", "경태", "경택", "경표", "경필", "공명", "공민", "교묵", "국길", "국도", "국만", "국태", "군길", "군모", "규강", "규건", "규경", "규광", "규람", "규로", "규리", "규만", "규민", "규백", "규범", "규빈", "규탁", "규태", "기남", "기담", "기동", "기룡", "기륭", "기문", "기민", "기백", "기복", "기봉", "기탁", "기태", "기택", "기표", "나경", "나리", "나영", "나우", "나희", "난경", "난영", "난욱", "난호", "남경", "남기", "남도", "남룡", "남연", "남이", "남익", "남인", "남헌", "남혁", "남현", "남호", "남훈", "남희", "내경", "내정", "내형", "다람", "다연", "다영", "다예", "다원", "다은", "다인", "다일", "다현", "다혜", "다호", "다환", "대건", "대권", "대규", "대근", "대기", "대길", "대동", "대로", "대언", "대엽", "대영", "대용", "대우", "대운", "대원", "대하", "대한", "대허", "대현", "대협", "대형", "대호", "대훈", "대희", "덕원", "도현", "도형", "도훈", "동건", "동관", "동광", "동구", "동권", "동규", "동근", "동기", "동길", "동륜", "동률", "동연", "동엽", "동영", "동오", "동우", "동운", "동원", "동윤", "동주", "동하", "동학", "동해", "동헌", "동현", "동협", "동호", "동화", "동훈", "동희", "두연", "두열", "두영", "두원", "두하", "두학", "두한", "두헌", "두혁", "두현", "두협", "두형", "두호", "두홍", "두환", "두희", "명기", "명성", "명진", "모준", "모찬", "목준", "목찬", "무길", "무민", "무선", "무찬", "무창", "문국", "미강", "미광", "미권", "미범", "미선", "미성", "미송", "미준", "민", "민강", "민건", "민걸", "민경", "민관", "민광", "민교", "민구", "민규", "민근", "민기", "민길", "민배", "민백", "민범", "민상", "민서", "민석", "민선", "민성", "민송", "민수", "민승", "민재", "민정", "민제", "민조", "민종", "민준", "민지", "민찬", "민창", "민채", "민철", "반석", "배문", "백강", "백광", "백규", "백민", "백범", "백산", "백삼", "백상", "백선", "백송", "백준", "백찬", "백철", "범근", "범기", "범길", "범모", "범식", "범준", "범진", "범찬", "범천", "범철", "병걸", "병관", "병국", "병권", "병규", "병기", "병길", "병만", "병모", "병민", "병서", "병석", "병선", "병섭", "병수", "병식", "병재", "병조", "병주", "병준", "병지", "병진", "병찬", "병창", "병채", "병천", "병철", "병필", "보경", "보광", "보길", "보민", "보배", "보빈", "보준", "본광", "본규", "본근", "본기", "본길", "본무", "본서", "본석", "본승", "본주", "본준", "본찬", "본창", "봉수", "봉천", "부광", "부길", "부민", "부석", "부선", "부성", "부송", "부찬", "부창", "비강", "비건", "비산", "비삼", "비선", "비성", "비창", "사미", "사범", "사빈", "사열", "사영", "사준", "사호", "사홍", "산", "산오", "산우", "산일", "산호", "삼우", "삼욱", "삼운", "삼원", "삼윤", "삼재", "삼정", "삼준", "삼헌", "삼혁", "삼현", "삼호", "상모", "상무", "상문", "상민", "상배", "상백", "상봉", "상빈", "상선", "상수", "상아", "상연", "상열", "상영", "상오", "상우", "상욱", "상운", "상원", "상유", "상윤", "상은", "상익", "상인", "상일", "상재", "상준", "상진", "상철", "상필", "상학", "상헌", "상혁", "상현", "상호", "상환", "서빈", "서양", "서연", "서영", "서욱", "서원", "서윤", "서은", "서일", "서일", "서정", "서준", "서진", "서찬", "서창", "서필", "서하", "서현", "서호", "서홍", "서환", "서훈", "서희", "석모", "석무", "석문", "석민", "석봉", "석수", "석영", "석오", "석우", "석운", "석원", "석윤", "석인", "석일", "석주", "석준", "석진", "석찬", "석하", "석헌", "석현", "석호", "석환", "석훈", "선모", "선빈", "선영", "선오", "선용", "선우", "선운", "선일", "선진", "선찬", "선필", "선혜", "선호", "선환", "선훈", "성모", "성무", "성묵", "성문", "성민", "성배", "성빈", "성수", "성식", "성신", "성아", "성안", "성연", "성열", "성오", "성용", "성우", "성운", "성원", "성윤", "성은", "성인", "성일", "성재", "성주", "성준", "성진", "성찬", "성철", "성필", "성헌", "성현", "성호", "성화", "성환", "성훈", "세빈", "세연", "세왕", "세은", "세인", "세일", "세진", "세찬", "세현", "세호", "세화", "세환", "세훈", "소민", "소범", "소언", "소연", "소영", "소일", "소정", "소준", "소진", "소찬", "소현", "소형", "소환", "소훈", "손호", "손환", "송민", "송연", "송열", "송우", "송욱", "송운", "송원", "송윤", "송이", "송재", "송주", "송준", "송찬", "송하", "송헌", "송호", "송환", "송회", "송훈", "수민", "수백", "수빈", "수석", "수아", "수양", "수연", "수열", "수영", "수예", "수용", "수운", "수웅", "수원", "수유", "수인", "수일", "수정", "수종", "수준", "수진", "수찬", "수창", "수철", "수하", "수헌", "수혁", "수현", "수혜", "수호", "수홍", "수환", "수황", "수훈", "순민", "순빈", "순식", "순신", "순양", "순열", "순영", "순오", "순용", "순우", "순욱", "순일", "순재", "순찬", "순창", "순필", "순하", "순헌", "순혁", "순현", "순호", "순홍", "순환", "승빈", "승선", "승연", "승오", "승은", "승이", "승인", "승종", "승주", "승준", "승진", "승학", "승환", "승희", "시연", "시영", "시완", "시원", "시윤", "시준", "시진", "시찬", "시형", "시환", "시훈", "신민", "신석", "신성", "신안", "신양", "신연", "신열", "신영", "신예", "신오", "신용", "신우", "신욱", "신원", "신일", "신조", "신준", "신찬", "신철", "신현", "신호", "신홍", "신화", "신환", "아승", "아연", "아영", "아진", "안오", "안중", "양우", "양운", "양원", "양윤", "양재", "양호", "양환", "연진", "연남", "연두", "연서", "연선", "연수", "연오", "연우", "연운", "연일", "연준", "연중", "연진", "연태", "연호", "열호", "영서", "영수", "영승", "영우", "영운", "영윤", "영재", "영중", "영호", "영환", "예리", "예림", "예서", "예원", "예일", "예종", "예준", "예지", "예진", "오준", "완우", "와운", "용", "용오", "용우", "용인", "용일", "용재", "용천", "용태", "용환", "우노", "우도", "우람", "우렴", "우석", "우성", "우승", "우식", "우열", "우영", "우용", "우원", "우윤", "우인", "우일", "우재", "우종", "우준", "우진", "우창", "우천", "우철", "우탄", "우태", "우혁", "우호", "운상", "운승", "운오", "운우", "운원", "운일", "운재", "운천", "운태", "웅우", "웅인", "웅재", "웅천", "웅태", "웅호", "원상", "원석", "원오", "원종", "원진", "원철", "원태", "원호", "원효", "유나", "유람", "유리", "유상", "유선", "유성", "유수", "유승", "유영", "유오", "유운", "유원", "유윤", "유인", "유일", "유임", "유재", "유정", "유조", "유중", "유진", "유찬", "유천", "유철", "유태", "유항", "유호", "유환", "윤상", "윤서", "윤석", "윤선", "윤소", "윤수", "윤승", "윤오", "윤우", "윤일", "윤재", "윤조", "윤중", "윤창", "윤천", "윤태", "윤형", "윤호", "윤환", "윤효", "율우", "은대", "은도", "은상", "은서", "은환", "의서", "의선", "의수", "의진", "의환", "이나", "이도", "이륜", "이림", "이서", "이석", "이성", "이열", "이영", "이웅", "이워", "이재", "이정", "이준", "이증", "이지", "이진", "이창", "이철", "이현", "이화", "이환", "인량", "인서", "인석", "인선", "인성", "인수", "인열", "인오", "인요", "인용", "인우", "인웅", "인원", "인유", "인재", "인준", "인중", "인직", "인진", "인창", "이철", "인태", "인한", "인항", "인혁", "인호", "인훈", "일오", "일원", "일윤", "일재", "일천", "일태", "일훈", "임오", "임우", "임천", "임태", "임환", "자빈", "자예", "자용", "자혁", "자호", "자환", "장번", "장복", "장빈", "장선", "장안", "장연", "장오", "장용", "장우", "장운", "장원", "장윤", "장일", "장이", "장준", "장진", "장찬", "장필", "장학", "장혁", "장호", "장환", "장호", "장훈", "재문", "재민", "재벽", "재빈", "재서", "재선", "재연", "재오", "재완", "재용", "재우", "재욱", "재운", "재웅", "재원", "재유", "재윤", "재익", "재인", "재일", "재준", "재진", "재찬", "재창", "재필", "재혁", "재형", "재호", "재환", "재효", "재훈", "전윤", "전훈", "정만", "정민", "정배", "정범", "정빈", "정서", "정선", "정섭", "정수", "정열", "정엽", "정영", "정예", "정완", "정요", "정용", "정우", "정원", "정유", "정윤", "정의", "정인", "정일", "정재", "정준", "정찬", "정천", "정철", "정필", "정하", "정혁", "정현", "정호", "정환", "정효", "정훈", "제빈", "제성", "제용", "제우", "제욱", "제웅", "제원", "재유", "재윤", "재익", "재인", "재일", "재준", "재진", "재찬", "재창", "재필", "재혁", "재형", "재호", "재환", "재효", "재훈", "전윤", "전훈", "정만", "정민", "정배", "정범", "정빈", "정서", "정선", "정선", "정섭", "정수", "정열", "정엽", "정영", "정예", "정완", "정요", "정용", "정우", "정원", "정유", "정윤", "정의", "정인", "정일", "정재", "정준", "정찬", "정천", "정철", "정필", "정하", "정혁", "정현", "정호", "정환", "정효", "정훈", "제빈", "제성", "제용", "제우", "제원", "제준", "제진", "제찬", "제혁", "제환", "제훈", "조서", "조운", "제원", "조윤", "조인", "조일", "종연", "종오", "종우", "종원", "종윤", "종인", "종일", "종학", "종호", "종환", "종효", "종훈", "좌준", "좌혁", "주", "주백", "주빈", "주상", "주서", "주선", "주영", "주용", "주원", "주윤", "주이", "주일", "주청", "주필", "주혁", "주형", "주호", "주환", "주훈", "준모", "준민", "준오", "준우", "준원", "준일", "준필", "준형", "준호", "준환", "중민", "중우", "중원", "중현", "중호", "지민", "지빈", "지서", "지선", "지섭", "지수", "지언", "지연", "지영", "징", "지오", "지용", "지우", "지욱", "지운", "지원", "지유", "지윤", "지은", "지응", "지익", "지일", "지준", "지혁", "지형", "지호", "차빈", "차연", "차준", "차혁", "차현", "차환", "차훈", "창무", "창복", "창연", "창우", "창욱", "창운", "창윤", "창조", "창현", "창호", "창환", "창희", "채문", "채성", "채송", "채연", "채우", "채윤", "채은", "채정", "채필", "채환", "채희", "천용", "천우", "천운", "천준", "천혁", "천환", "천훈", "철오", "철원", "철윤", "철형", "철호", "철환", "청모", "청무", "청문", "청오", "청운", "청원", "청윤", "청호", "청환", "초", "추원", "추윤", "추호", "추환", "충원", "태근", "태길", "태룡", "태륜", "태륭", "태림", "태영", "태오", "태용", "태우", "태운", "태원", "태윤", "태융", "태익", "태인", "태한", "태혁", "태호", "태홍", "태후", "태훈", "태희", "판겸", "판규", "판석", "판섭", "판성", "판승", "판식", "평진", "포규", "포겸", "표묵", "표문", "표섭", "표성", "필규", "필묵", "필범", "필성", "필승", "하승", "하운", "하윤", "하일", "하재", "하태", "한수", "한승", "한오", "한원", "한윤", "항우", "항원", "항윤", "항인", "항일", "항재", "해서", "해선", "해수", "해인", "해준", "해환", "향선", "헌환", "현서", "현석", "현선", "현성", "현수", "현섭", "현승", "현우", "현호", "형우", "형주", "형철", "형필", "형환", "혜승", "혜우", "혜일", "혜천", "혜호", "혜환", "호섭", "호승", "호운", "호원", "호영", "호윤", "호인", "호일", "호임", "호재", "호정", "호제", "호준", "호철", "호환", "화령", "화선", "환승", "환원", "환윤", "환인", "환재", "효곤", "효상", "효서", "훈승", "훈오", "후원", "후윤", "훈일", "훈재", "훈항", "훈호", "훈호", "희승", "희오", "희우", "희운", "희원", "희윤", "희일", "희재", "희천", "희태"]
    for year in range(1, maxYear + 1): #year 학년
        for group in range(1, maxGroup + 1): #group 반
            for num in range(1, maxNum + 1): #num 번호
                name = random.choice(sung) + random.choice(hanguls)
                sex = random.choice(sList)
                #성적
                korean = random.randrange(0,100)
                math = random.randrange(0,100)
                english = random.randrange(0,100)
                science = random.randrange(0,100)

                student.DB.append(student(name, year, group, num, sex, korean, math, english, science))
    
    student.count = maxYear * maxGroup * maxNum

#메인화면
def main():
    while True:
        print("**기능을 선택하세요**")
        print("--------------")
        print("1. 학생 정보 입력")
        print("2. 학생 정보 수정")
        print("3. 학생 정보 삭제")
        print("4. 학생 성적 조회")
        print("5. 성적표 출력 / 통계")
        print("6. 프로그램 종료")
        chk = int(input(">"))

        if(chk == 1):
            newInst = inputHelper()
            if(student.searchInfo(newInst.hakbun) == 0):
                student.DB.append(newInst)
            else:
                print("해당하는 학번에 다른 정보가 있습니다. 중복된 정보는 입력이 불가합니다.")
                continue
        elif(chk == 2):
            try:
                (student.searchInfo(input("학번을 입력하세요"))).modifyInfo()
            except AttributeError as exception:
                print("학번에 해당하는 학생이 없습니다.")
                continue
        elif(chk == 3):
            try:    
                student.removeInfo((student.searchInfo(input("학번을 입력하세요"))))
            except ValueError as exception:
                print("학번에 해당하는 학생이 없습니다.")
                continue
            except NameError as exception:
                print("처음화면으로 돌아갑니다.")
                continue
        elif(chk == 4):
            print(student.report())
        elif(chk == 5):
            #try:    
                (student.searchInfo(input("학번을 입력하세요"))).printReportCard()
                """except AttributeError() as exception:
                print("학번에 해당하는 학생이 없습니다.")
                continue"""
        elif(chk == 6):
            print("**프로그램을 종료합니다.**\n")
            break
        else:
            print("**미구현 기능입니다.**\n")


print("랜덤 데이터 생성중입니다...")
makeRandomData()

"""#임시 데이터
student.DB = [  student("이성준", 3, 3, 15, "남", 93, 10, 42, 61), \
                student("김남효", 2, 1, 24, "남", 93, 70, 32, 100,), \
                student("박준석", 1, 5, 3, "남", 83, 99, 92, 20,) ]
"""
#실행구문!!
main()
#student.calcGrade(1,2,3)