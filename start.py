from flask import Flask, send_from_directory, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "*************"

@app.route("/")  # 도메인 루트로 접속 시 index.html 제공
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form['question']
    
    # OpenAI API 호출
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 한국어로 대답하는 친절한 도우미입니다."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message['content']

    return render_template('result.html', question=user_input, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
