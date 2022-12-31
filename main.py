import numpy as np


# обучение на векторах
def training():
    final_weights = np.zeros((35, 35))
    vectors = []
    for g in range(4):
        fname = str(g + 1) + '.txt'
        arr = np.loadtxt(fname)
        l = []
        for k in range(7):
            megal = arr[k]
            l.extend(megal)
        vectors.append(l)
        for j in range(len(l)):
            l[j] = int(l[j])
        l = np.matrix(l)
        lt = l.T
        multx = np.dot(lt, l)
        final_weights = np.add(final_weights, multx)
    return final_weights, vectors


# сравниваем новые векторы с уже существующими
def match_vector(vec):
    for l in range(4):
        matchwith = vectors[l]
        if np.array_equal(matchwith, vec) == True:
            return l + 1
    return 0


# берет вектор, вычисляет его и сравнивает с имеющимися
def create_vector(vec):
    vec2 = np.matrix(vec)
    generated = []
    for t in range(35):
        w = final_weights[:, t]
        w2 = np.matrix(w)
        matx = np.dot(vec2, w2)
        if matx > 0:
            generated.append(1)
        else:
            generated.append(-1)
    return generated


# проверяем наличие вектора в файле
def check_new_vector(fnamex):
    f = np.loadtxt(fnamex)
    l = []
    for k in range(7):
        ml = f[k]
        l.extend(ml)
    vec = create_vector(l)
    numx = match_vector(vec)
    return numx


def check_if_matching(file):
    cnew1 = check_new_vector(file)
    if cnew1 != 0:
        print('совпадает с вектором  №', cnew1)
    else:
        print('нет совпадений с векторами')


final_weights, vectors = training()
print('Провели тренировку на', len(vectors), 'векторах')

correct = 0
for f in range(4):
    vec = create_vector(vectors[f])
    numx = match_vector(vec)
    if numx != 0:
        correct += 1

if correct == 4:
    ok = True
else:
    ok = False

if ok:
    print('проверяем файлы на совпадение с запомненными векторами:')
    check_if_matching('1noise.txt')
    print('-----------------------')
    check_if_matching('2noise.txt')

