from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
#...
app = Flask(__name__)
#...
bootstrap = Bootstrap(app)


def percentage(a,b):
    results = ((a / b) * 100)
    return "%.2f" % results + "%"

@app.route('/')
def capacity():
   return render_template('capacity.html')
  # if request.method == 'POST':
#      result = request.form
      #return render_template("capacity_results.html",result = result)
@app.route('/capacity_results_answer',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        memory_used = float(request.form['memory_mb_used'])
        memory = float(request.form['memory_mb'])
        m_answer = percentage(memory_used, memory)
        vcpu_used = float(request.form['vcpu_used'])
        vcpu = float(request.form['vcpu']) * 4
        v_answer = percentage(vcpu_used, vcpu)
        disk_available_least = float(request.form['disk_available_least'])
        local_gb = float(request.form['local_gb'])
        d_answer = percentage(disk_available_least, local_gb)
        return render_template("capacity_results_answer.html" ,mem = m_answer,vcpu = v_answer, disk = d_answer)


if __name__ == '__main__':
   app.run(debug = True)
