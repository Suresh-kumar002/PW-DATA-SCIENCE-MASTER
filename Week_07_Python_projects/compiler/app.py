from flask import Flask, request, jsonify, render_template
import subprocess
import os
import uuid
import shutil

app = Flask(__name__)

BASE_DIR = "temp_files"

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_code():

    data = request.json
    language = data.get("language")
    code = data.get("code")
    user_input = data.get("input", "")

    file_id = str(uuid.uuid4())
    work_dir = os.path.join(BASE_DIR, file_id)

    os.mkdir(work_dir)

    try:

        # PYTHON 

        if language == "python":

            file_path = os.path.join(work_dir, "main.py")

            with open(file_path, "w") as f:
                f.write(code)

            result = subprocess.run(
                ["python", file_path],
                input=user_input,
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout + result.stderr


        # JAVASCRIPT 

        elif language == "javascript":

            file_path = os.path.join(work_dir, "main.js")

            with open(file_path, "w") as f:
                f.write(code)

            result = subprocess.run(
                ["node", file_path],
                input=user_input,
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout + result.stderr


        #C++
        elif language == "cpp":

            cpp = os.path.join(work_dir, "main.cpp")
            exe = os.path.join(work_dir, "main.exe")

            with open(cpp, "w") as f:
                f.write(code)

            compile = subprocess.run(
                ["g++", cpp, "-o", exe],
                capture_output=True,
                text=True
            )

            if compile.stderr:
                output = compile.stderr
            else:

                result = subprocess.run(
                    [exe],
                    input=user_input,
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                output = result.stdout + result.stderr


        #JAVA

        elif language == "java":

            java_file = os.path.join(work_dir, "Main.java")

            with open(java_file, "w") as f:
                f.write(code)

            compile = subprocess.run(
                ["javac", java_file],
                capture_output=True,
                text=True,
                cwd=work_dir
            )

            if compile.stderr:
                output = compile.stderr
            else:

                result = subprocess.run(
                    ["java", "Main"],
                    input=user_input,
                    capture_output=True,
                    text=True,
                    cwd=work_dir,
                    timeout=10
                )

                output = result.stdout + result.stderr


        # C

        elif language == "csharp":

            cs = os.path.join(work_dir, "Program.cs")
            exe = os.path.join(work_dir, "Program.exe")

            with open(cs, "w") as f:
                f.write(code)

            compile = subprocess.run(
                ["csc", cs],
                capture_output=True,
                text=True,
                cwd=work_dir
            )

            if compile.stderr:
                output = compile.stderr
            else:

                result = subprocess.run(
                    [exe],
                    input=user_input,
                    capture_output=True,
                    text=True,
                    cwd=work_dir,
                    timeout=10
                )

                output = result.stdout + result.stderr


        # C 

        elif language == "c":

            cfile = os.path.join(work_dir, "main.c")
            exe = os.path.join(work_dir, "main.exe")

            with open(cfile, "w") as f:
                f.write(code)

            compile = subprocess.run(
                ["gcc", cfile, "-o", exe],
                capture_output=True,
                text=True
            )

            if compile.stderr:
                output = compile.stderr
            else:

                result = subprocess.run(
                    [exe],
                    input=user_input,
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                output = result.stdout + result.stderr


        else:
            output = "Language not supported"


        shutil.rmtree(work_dir)

        return jsonify({"output": output})


    except subprocess.TimeoutExpired:

        shutil.rmtree(work_dir)

        return jsonify({
            "output": "Execution Timeout: Infinite loop detected"
        })


    except Exception as e:

        shutil.rmtree(work_dir)

        return jsonify({
            "output": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)