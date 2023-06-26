'''
/*********************************************************************
*Title : 물 주기
*Number : null
*Author : null
*Description : 랑이 집사는 고양이들이 좋아한다는 캣닢을 직접 재배하려고 한다.일직선으로 놓여진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">N</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</mjx-container>개의 화분에 캣닢이 하나씩 심어져 있다.각 화분은 초기에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">K</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</mjx-container>만큼의 수분을 머금고 있고, 매일 아래와 같은 일이 순서대로 일어난다.랑이 집사가 연속된 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">A</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</mjx-container>개의 화분에 물을 준다. 이 때 물을 준 화분의 수분은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">B</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</mjx-container>만큼씩 증가한다.모든 화분의 수분이 1씩 감소한다.수분이 0이 된 화분에 있는 캣닢은 죽는다.모든 캣닢이 살아 있는 기간이 최대한 길어지도록 물을 줄 때, 첫 캣닢이 죽는 날짜를 출력하는 프로그램을 작성하시오. 첫 날은 1일이다. 
*Input : 첫째 줄에 자연수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">N</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">K</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">A</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">B</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</mjx-container>가 공백을 사이에 두고 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline">2≤N≤100</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N \le 100$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline">1≤K≤100</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le K \le 100$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">1≤A×B<N</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le A \times B < N$</mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">A</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</mjx-container>는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline">N</mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</mjx-container>의 약수) 
*Output : 모든 캣닢이 살아 있는 기간이 최대한 길어지도록 물을 줄 때, 첫 캣닢이 죽는 날짜를 출력한다. 
*Start Time : 2023년 1월 10일 9시 8분 53초
*End Time : 2023년 1월 10일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/


'''

import sys
input = sys.stdin.readline
# n: 화분 개수
# k: 초기 수분
# a: 물을 줄 연속된 화분 수 (a는 n의 약수임)
# b: 문을 준 화분의 수분 증가량 (1 < a * b < n)
n, k, a, b = map(int, input().split())

cnt = 0
c = [k for _ in range(n)]
flag = True
while flag:
    cnt += 1 # 다음 날

    # 죽기 직전인 놈 인덱스 알아내기
    _min = min(c)
    idx = c.index(_min)

    # 죽기 직전인 놈부터 k개의 연속된 화분에 물주기
    for i in range(a):
        c[idx + i] += b

    # 모든 화분의 수분 1 감소
    for i in range(n):
        c[i] -= 1
        if c[i] == 0:
            flag = False
print(cnt)