# *
# **
# ***
# ****   Pattern 1
print("Pattern 1")
i = 6
for j in range(i):
    print(j * "*")
########################################################
#           *
#          **
#         ***
#        ****
#       *****   Pattern 2
#######################################################
print("Pattern 2")
i = 6
for j in range(i):
    print((i - j) * " ", j * "*")

########################################################
#           *
#          * *
#         * * *
#        * * * *
#       * * * * *   pattern 3
#######################################################
print("Pattern 3")
i = 6
for j in range(i):
    print((i - j) * " ", j * " *")

########################################################
#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *      Pattern 4
#######################################################

print("Pattern 4")
i = 8
for j in range(i):
    print((i - j) * " ", j * " *")
for j in range(i):
    print((j) * " ", (i-j) * " *")

########################################################
# * * * * * * *
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
#
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
#######################################################

print("Pattern 5")
i = 7
for j in range(i):
    print(j * " ", (i-j) * " *")
for j in range(1,i):
    print((i - j) * " ", j * " *")