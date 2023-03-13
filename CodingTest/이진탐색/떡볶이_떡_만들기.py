import sys
input = sys.stdin.readline

def bSearch(arr, t, s, e):
    result = 0
    while s <= e:
        mid = (s + e) // 2
        rc_len = 0
        for i in arr:
            if i > mid:
                rc_len += i - mid
        if rc_len < t:
            e = mid - 1
        elif rc_len > t:
            s = mid + 1
            result = mid
        else:
            return mid
    return result

n, m = map(int, input().split())
rc = sorted(list(map(int, input().split())))
print(bSearch(rc, m, 0, rc[-1]))