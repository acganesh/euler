# This file was *autogenerated* from the file 550.sage
from sage.all_cmdline import *   # import sage library
_sage_const_101787 = Integer(101787); _sage_const_3 = Integer(3); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_1904324 = Integer(1904324); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_49163 = Integer(49163); _sage_const_21 = Integer(21); _sage_const_1349779 = Integer(1349779); _sage_const_987654321 = Integer(987654321); _sage_const_664579 = Integer(664579); _sage_const_2406 = Integer(2406); _sage_const_11068 = Integer(11068); _sage_const_774078 = Integer(774078); _sage_const_2050696 = Integer(2050696); _sage_const_5210 = Integer(5210); _sage_const_233 = Integer(233); _sage_const_2444359 = Integer(2444359); _sage_const_510 = Integer(510); _sage_const_12 = Integer(12); _sage_const_10 = Integer(10); _sage_const_1124 = Integer(1124); _sage_const_23448 = Integer(23448); _sage_const_45 = Integer(45); _sage_const_102 = Integer(102); _sage_const_409849 = Integer(409849); _sage_const_207207 = Integer(207207)
R = Integers(_sage_const_987654321 )
roles = [_sage_const_4 , _sage_const_4 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , ]
m = _sage_const_5 

roles = [_sage_const_664579 , _sage_const_1904324 , _sage_const_2444359 , _sage_const_0 , _sage_const_2050696 , _sage_const_0 , _sage_const_0 , _sage_const_1349779 , _sage_const_774078 , _sage_const_0 , _sage_const_0 , _sage_const_409849 , _sage_const_0 , _sage_const_207207 , _sage_const_101787 , _sage_const_0 , _sage_const_49163 , _sage_const_0 , _sage_const_0 , _sage_const_23448 , _sage_const_0 , _sage_const_11068 , _sage_const_5210 , _sage_const_0 , _sage_const_0 , _sage_const_2406 , _sage_const_1124 , _sage_const_0 , _sage_const_510 , _sage_const_0 , _sage_const_0 , _sage_const_233 , _sage_const_102 , _sage_const_0 , _sage_const_0 , _sage_const_45 , _sage_const_0 , _sage_const_21 , _sage_const_7 , _sage_const_0 , _sage_const_0 , _sage_const_3 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 ]
m = _sage_const_10 **_sage_const_12 

n = len(roles)
mat = matrix(R, [[roles[i ^ j] for j in range(n)] for i in range(n)])
init = vector(R, [i == _sage_const_0  for i in range(n)])
print init

ans = mat**m * init
print ans
print sum(ans) - ans[_sage_const_0 ]
