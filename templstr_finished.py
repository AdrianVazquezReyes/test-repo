# demonstrate template string functions

from string import Template


def main():
    # Usual string formatting with format()
    print('*'*100)
    str1 = 'you are reading the book: {0} by {1}'.format('Blue house', 'Edward Alan')
    print(str1)

    # create a template with placeholders
    templ = Template('you are reading the book: ${title} by ${author}')

    # use the substitute method with keyword arguments
    str2 = templ.substitute(title= 'Blue', author= 'Edward')
    print(str2)
    str3 = templ.substitute(title= 'house', author='Alan')
    print(str3)

    # use the substitute method with a dictionary
    data = dict(
        author= 'Edward Alan Poe',
        title=  'My Blue House'
        )
    print(data)
    data2 = {
        'author' : 'Edward',
        'title' : 'Blue'
        }
    print(data2)

    str4 = templ.substitute(data)
    print(str4)
    
if __name__ == "__main__":
    main()
    