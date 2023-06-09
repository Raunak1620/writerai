from flask import Flask, render_template, request
import config.config as config
import config.writer as writer

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Write a product  description about {}".format(submission)
        # openAIAnswerUnformatted = writer.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Write a job description on  {}".format(submission)
        # openAIAnswerUnformatted = writer.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Write a tweet idea on  {}".format(submission)
        # openAIAnswerUnformatted = writer.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('tweet-ideas.html', **locals())




@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a cold email to potential clients about: {}".format(submission)
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Write a social media post on {}".format(submission)
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('social-media.html', **locals())
    


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Write business pitch on {}".format(submission)
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Suggest Video ideas on  {}".format(submission)
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():
    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Write a video description on {}".format(submission)
        openAIAnswer = writer.openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-description.html', **locals())




if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5000', debug=True)
