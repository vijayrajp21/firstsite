from flask  import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def project(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=['email','full_name','subject','message'])

        writer.writerow(data)


def write_to_database(data):
    f = open("database.txt", mode="a")
    f.write(f'''

email : {data.get('email')}
Full Name : {data.get('full_name')}
Subject : {data.get('subject')}
Message : {data.get('message')}

================================================================''')
    f.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        print(data)
        write_to_csv(data)
        return redirect('Thanku.html')
    else:
        return 'somethings wrong'




