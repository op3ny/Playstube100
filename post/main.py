import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/html/playstube/video'

# Configurando o diretório de upload
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'mp4'}

# Função para verificar se a extensão é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum arquivo foi enviado', 400

    file = request.files['file']
    channel_name = request.form['channel']

    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400

    # Verifica se a extensão do arquivo é .mp4
    if not allowed_file(file.filename):
        return 'Apenas arquivos .mp4 são permitidos', 400

    # Criando o diretório com o nome do canal, se não existir
    channel_dir = os.path.join(app.config['UPLOAD_FOLDER'], channel_name)
    os.makedirs(channel_dir, exist_ok=True)

    # Salvando o arquivo no diretório do canal
    file_path = os.path.join(channel_dir, file.filename)
    file.save(file_path)

    return f'Vídeo enviado no canal especificado com sucesso! O nome do canal e a pasta, e o video esta dentro da pasta. <br> (Obs:. Para deletar seu video, pedimos para entrar em contato com op3n@hsyst.com.br "Webmaster")', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
