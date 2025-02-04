# declaring a variable with in dynamic typing
text = input('Enter something: ')

# check everything about the input
print(f'\"{text}\" is a {type(text)} data type')
print(f'is it a number? {text.isnumeric()}')
print(f'is it alphabetic? {text.isalpha()}')
print(f'is it alphanumeric? {text.isalnum()}')
print(f'is it in uppercase only? {text.isupper()}')
print(f'is it in lowercase only? {text.islower()}')
print(f'is it capitalized? {text.istitle()}')