from flask import Flask, render_template, request
import os
import pdfkit

path_wkhtmltopdf = r'D:\Softies\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

scriptpath = os.path.realpath(__file__)
head, tail = os.path.split(scriptpath)

app = Flask(__name__)
@app.route('/pdf_generate', methods=['POST'])
def results():
    input = request.get_json()
    html_page = render_template('cv.html',
                                name=input['name'],
                                email=input['email'],
                                mobile_no=input['mobile_no'],
                                address = input['address'],
                                profile=input['profile'],
                                technical_skills=input['technical_skills'],
                                work_experience=input['work_experience'],
                                projects=input['projects'],
                                education = input['education']
                                )
    css = head + "/static/style.css"
    print(css)
    pdfkit.from_string(html_page, 'out.pdf', css=css,configuration=config)
    return html_page

if __name__ == '__main__':
    app.run(debug=True)
