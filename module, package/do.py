# import my_module
# my_module.나라친구()

# import tour.jeonnam
# tour.jeonnam.채리()
#
# from tour import jeonnam
# jeonnam.채리()
#
# from tour.jeonnam import 채리
# 채리()

# import tour.jeonnam as tj
# tj.jeonnam.채리()
#
# from tour import jeonnam as je
# je.채리()
#
# from tour.jeonnam import 채리 as cherry
# # 채리() NameError 남
# cherry()

from tour import *
jeonnam.채리()
gw = gangwondo.GangwondowPackage()
print(gw)