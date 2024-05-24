# 9184번: 신나는 함수 실행 - <img src="https://static.solved.ac/tier_small/9.svg" style="height:20px" /> Silver II

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/9184)


<p>재귀 호출만 생각하면 신이 난다! 아닌가요?</p>

<p>다음과 같은 재귀함수 w(a, b, c)가 있다.</p>

<pre>if a &lt;= 0 or b &lt;= 0 or c &lt;= 0, then w(a, b, c) returns:
    1

if a &gt; 20 or b &gt; 20 or c &gt; 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a &lt; b and b &lt; c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
</pre>

<p>위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)</p>

<p>a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.</p>



## 입력


<p>입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.</p>



## 출력


<p>입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.</p>



## 소스코드

[소스코드 보기](신나는%20함수%20실행.py)