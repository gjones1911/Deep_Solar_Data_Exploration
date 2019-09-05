import sys


def show_list(l, numbered=False, type='s', vec_prnt=False):
    if vec_prnt:
        cnt = 0
        for s in l:
            if cnt == 0:
                print(" = ['{:s}',".format(str(s)))
            elif cnt == len(l):
                print("'{:s}']".format(str(s)))
            else:
                print("'{:s}',".format(str(s)))
            cnt += 1
    elif numbered:
        cnt = 1
        if type == 's':
            for e in l:
                print('{:d}: {:s}'.format(cnt, str(e)))
                cnt += 1
        elif type == 'd':
            for e in l:
                print('{:d}: {:d}'.format(cnt, e))
                cnt += 1
    else:
        if type == 's':
            for e in l:
                print('{:s}'.format(e))
        elif type == 'd':
            for e in l:
                print('{:d}'.format(e))

def show_dict(d, type='sn'):
        for k in d:
            if type[0] == 's':
                if type[1] == 'l':
                    print('{:s}:'.format(str(k)))
                    self.show_list(d[k])
                elif type[1] == 's' or type[1] == 'n':
                    print('{:s}: {:s}'.format(str(k), str(d[k])))
                elif type[1] == 'd':
                    self.show_dict(d[k], type=type[1:])

def sort_dict(d, t=1, rt='d', reverse=False):
    import operator
    if rt == 't':
        return sorted(d.items(), key=operator.itemgetter(t), reverse=reverse)
    elif rt == 'd':
        return dict(sorted(d.items(), key=operator.itemgetter(t), reverse=reverse))


def complete_path(partial, end):
    return partial + end