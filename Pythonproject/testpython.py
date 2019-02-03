#Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 



print ('Hello world!')

#let us practice some variables, list, and some calculations.
#Most common variable types are integer, string, float and boolean.

str_var = 'Sam'
#Here Sam is string variable

int_var = 100
#here int_var is an integer

float_var = 100.001
#here float_var is a float

#Boolean variable return type is where a condition is either TRUE or FALSE

# Below is a test sample code to know capitals of some of the states in US.

#list us_statecaps
us_statecaps = ['TX', 'Austin','CA', 'Sacramento','VA','Richmond','CO','Denver','NY', 'Albany','FL', 'Tallahassee']


state = input('Enter states to know their capitals--TX,CA,VA,CO,NY,FL:')
str_state = str(state)
index_state = us_statecaps.index(str_state)

int_index_state = int(index_state)
print('Capital of ',str_state,'is ',us_statecaps[int_index_state+1],'.')





