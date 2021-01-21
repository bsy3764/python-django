# askcompany/instagram/converters.py

# 커스텀 Converter 정의
class YearConverter:
    regex = r"20\d{2}"
    
    # URL 매칭이 되었을 때, view함수를 호출하기 전에 인자를 정리함
    def to_python(self, value):
        return int(value)

    #URL Reverse를 할 때, 어떤 값을 URL로 전달할 문자열로 바꿈
    def to_url(self, value):
        return str(value)

class MonthConverter(YearConverter):   # YearConverter 상속받기
    regex = r"\d{1,2}"  # 1글자 또느 2글자

class DayConverter(YearConverter):
    regex = r"[0123]\d"