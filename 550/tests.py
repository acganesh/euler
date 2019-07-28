from py_rule_freq_dist import old_main
from main import main as new_main
from tree_search import main as tree_main

def test1(mod=None):
    mod = 13
    for n in xrange(4, 20):
        for k in xrange(2, 6):
            if mod:
                assert old_main(n, k) % mod == new_main(n, k, mod)
            else:
                assert old_main(n, k) == new_main(n, k)
    print 'test1 passed!'

def test2(mod=None):
    for n in xrange(4, 300):
        for k in xrange(2, 3):
            if mod:
                assert old_main(n, k) % mod == new_main(n, k, mod)
            else:
                assert old_main(n, k) == new_main(n, k)
        if n % 50 == 0: print n
    print 'test2 passed!'

def test3(mod=None):
    for n in xrange(4, 10):
        for k in xrange(2, 10):
            if mod:
                assert old_main(n, k) % mod == new_main(n, k, mod)
            else:
                assert old_main(n, k) == new_main(n, k)

def test4():
    for n in xrange(4, 12):
        for k in xrange(2, 6):
            assert tree_main(n, k) == new_main(n, k)

def test5():
    for n in xrange(4, 20):
        for k in xrange(2, 3):
            assert tree_main(n, k) == new_main(n, k)

def test6():
    for mod in xrange(3, 100000, 2):
        assert new_main(10, 5, mod) == 40085 % mod

test6()
