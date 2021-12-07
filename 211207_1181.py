"""
단어 정렬
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
"""

def word_sort():
    n = int(input())
    str_list = []
    for _ in range(n):
        s = input()
        if s not in str_list:
            str_list.append(s)
            continue
    str_list.sort()
    sort_str_list = sorted(str_list, key=lambda x: len(x))

    return print(*sort_str_list, sep='\n')

if __name__ == "__main__":
    word_sort()