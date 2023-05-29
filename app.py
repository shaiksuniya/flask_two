from flask import Flask

FAI=Flask(__name__)

@FAI.route('/sonu/<na>/')
def sonu(na):
    return f'This is suniya {na}'

if __name__=='__main__':
    FAI.run(debug=True,host= '192.168.34.83',port=5002)
