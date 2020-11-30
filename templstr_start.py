# demonstrate template string functions
from string import Template


def main():
    str1 = 'i am {0} and i write {1}'.format('adrian vazquez', 'green')
    print(str1)

    templ = Template('i am ${nombre} and i write ${libro}')
    str2 = templ.substitute(nombre = 'adrian vazquez', libro = 'green')
    print(str2)

    data = {'nombre' : 'adrian vazquez', 'libro' : 'green'}
    str3 = templ.substitute(data)
    print(str3)
if __name__ == "__main__": main()

def tmplete1(**d):
    print('*'*100)
    text = Template('hola mi nombre es ${nombre} y mi apellido ${apellido}')
    text2 = text.substitute(nombre = 'Adrian', apellido = 'Vazquez')
    print(text2)
    text3 = text.substitute(d)
    print('chido', text3)

data = {'nombre' : 'adrian', 'apellido' : 'vazquez'}
tmplete1(**data)