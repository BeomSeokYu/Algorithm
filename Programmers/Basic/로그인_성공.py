def solution(id_pw, db):
    answer = ''
    id_db = []
    pw_db = []

    for i, p in db:
        id_db.append(i)
        pw_db.append(p)

    if id_pw in db:
        answer = 'login'
    elif id_pw[0] not in id_db:
        answer = 'fail'
    else:
        answer = 'wrong pw'

    return answer