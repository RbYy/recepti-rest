from weakref import WeakKeyDictionary


class A():
    validate = 3

    def s(self, a):
        return self.validate


class B():
    def __init__(self, a):
        self.a = a

    def met(self, a):
        return self.a.s(777) + a

a = A()
a.s(7)
b = B(a)
print(b.met(5))


class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self._budget = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    def profit(self):
        return self.gross - self.budget


m = Movie('Casablanca', 97, 102, 964000, 1300000)
print(m.budget)       # calls m.budget(), returns result
try:
    m.budget = -100  # calls budget.setter(-100), and raises ValueError
except ValueError:
    print("Woops. Not allowed")


class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        print('init ...', default)
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        print('getting ...self: {0}, instance: {1}, owner: {2}'.format(self, instance, owner))
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        print('setting attribute {0} on movie {1}.'.format(value, instance))
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value


class Movie(object):

    # always put descriptors at the class-level
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)
    aaa = 5
    def __str__(self):
        return self.title

    def __init__(self, title, rating, runtime, budget, gross):
        self.aaa = 6
        self.title = title
        print('prepare setting ...')
        self.rating = rating
        print('prepare setting ...')
        self.runtime = runtime
        print('prepare setting ...')
        self.budget = budget
        print('prepare setting ...')
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


m = Movie('Casablanca', 97, 102, 964000, 1300000)
#m = Movie()
print('budget: ', m.budget)  # calls Movie.budget.__get__(m, Movie)
m.rating = 100  # calls Movie.budget.__set__(m, 100)
print('rating: ', m.rating)
print(m.aaa)
try:
    m.rating = -1   # calls Movie.budget.__set__(m, -100)
except ValueError:
    print("Woops, negative value")


class D(object):
    pass


import sys
sys.setrecursionlimit(50000)

sss = 111
def koraki(baza, expo=1, k=0):
    print(sss)
    if baza == 1:
        return k * expo
    def bd(baza, deljitelj=2):
        if not baza % deljitelj:
            return baza / deljitelj
        return bd(baza, deljitelj + 1)
    return koraki(baza - bd(baza), expo, k + 1)



osnova = 2016
exponent = 155
print(koraki(osnova, exponent))
print(koraki(16, 5))
print(koraki(2017))
print('---------')


#print(vrni_pra(42))
"""
@decorator_with_args(arg)
def foo(*args, **kwargs):
    pass

translates to

foo = decorator_with_args(arg)(foo)
"""


def nad(spodnja):
    """ Decorator; decorates a fuction
     which returns an iterable of numbers.
     Takes one argument, returns a list of 
     numbers higher than the argument. """
    def srednja(func):
        def notranja(*args, **kwargs):
            return [x for x in func(*args, **kwargs) if x >= spodnja]
        return notranja
    return srednja


#@nad(30)
def vrni_pra(n):
    pralista = []
    def pra(n, k=2):
        if n >= k:
            if n == k:
                pra(n - 1)
                pralista.append(n)
            elif n % k:
                pra(n, k + 1)
            else:
                pra(n - 1)
        else:
            pralista.append(1)
    pra(n)
    return pralista
#print(vrni_pra(500))

vrni_pra = nad(30)(vrni_pra)

print(vrni_pra(50))


class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self._budget = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        print('setting ', value)
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    def profit(self):
        return self.gross - self.budget


m = Movie('Casablanca', 97, 102, 964000, 1300000)
print (m.budget)       # calls m.budget(), returns result
try:
    m.budget = -100  # calls budget.setter(-100), and raises ValueError
except ValueError:
    print ("Woops. Not allowed")
print(sss)
class D:
    x = 3
ff = D()
print(ff.x)
def l():
    sss = 8
    ff.x = 4
    D.y = 5
    print(ff.x)
    #print('f1 ', sss)

    #sss = 999
    #print(f2 ', sss)
    print(sss)

l()
print('ff.x: ', ff.x)
print('D.y: ', D.y)
print('ff.y: ', ff.y)
print('koncna ostaja 111? -- ', sss)

i=2
k = [3,4]
def fun(a):
    global i
    i += 1
    k.append(8)
    i = 8

    def fun1(i=i):
        i += 1
        return i
    return fun1

qq = fun(18)

print(qq())


def ff(self):
    print('uspelo')
D.XX = ff

h = D()
h.XX()
import os, sys
print(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import djangoenv
from models import Jed
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser



#user = User(username="qqq", password="111")
#jed = Jed(ime="eee", recept="oijoij", poreklo="uihu", user=user, vrsta = "fds")
#print(jed)
class JedSerializer(serializers.Serializer):
    user = UserSerializer()
    ime = serializers.CharField()
    recept = serializers.CharField()
    poreklo = serializers.CharField()
    vrsta = serializers.CharField()

