#**********************************************************
#Author: Abiodun Owoseje
#Date Created: 03/28/2017
#Assignment Description:  This program display the percentage of fruit in basket.
#                        
#
#
#Ver no.         Name(Initials)     Date			Description
#========     ===========    ==========		===============
#
#**********************************************************
#Variable Initialization

#(I)Enter the number of apples
n_apple = int(input('Enter the number of apples in basket: '))
#(I)Enter the number of oranges
n_orange = int(input('Enter the number of oranges in basket: '))
#(I)Enter the number of pears
n_pear = int(input('Enter the number of pears in basket: '))
#(P)Calculate total number of fruit
total = n_apple + n_orange + n_pear
#(P)Calculate percentage of each fruit
apples = n_apple/total * 100
oranges = n_orange/total * 100
pears = n_pear/total * 100

#(O) Percentage of the _Apples_ is ____ %
print('Percentage of the Apples is', format(apples, '.2f'),'%') 
#(O) Percentage of the _Oranges_ is ____ %
print('Percentage of the Oranges is', format(oranges, '.2f'),'%')  
#(O) Percentage of the _Pears_ is ____ %
print('Percentage of the Pears is', format(pears, '.2f'),'%')

