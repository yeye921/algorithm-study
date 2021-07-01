def solution(seoul):
    index = seoul.index("Kim")
    return "김서방은 %s에 있다" % index
    # 문자열 대입하는 여러가지 방법
    # return "김서방은 {0}에 있다".format(index)
    # return "김서방은 {index}에 있다.format(index = seoul.index("Kim"))"
    # return f'김서방은 {index}에 있다'
