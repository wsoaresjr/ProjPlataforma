# Plataforma de Elaboração de Itens

Este projeto consiste em uma aplicação web desenvolvida com **Django**, que permite o gerenciamento de usuários, grupos e associações entre eles, com funcionalidades específicas para administradores.

## **Funcionalidades**

### **Usuários**
- Cadastro de usuários com os seguintes campos:
  - `CodUsuario`
  - `Nome`
  - `Username`
  - `Senha`
  - `CPF`
  - `Email`
  - `ChavePix`
  - `StatusAtivo`
- Edição e exclusão de usuários.

### **Grupos**
- Cadastro de grupos com os seguintes campos:
  - `CodGrupo`
  - `NomeGrupo`
  - `Descrição`
- Edição e exclusão de grupos.

### **Associações (Usuários e Grupos)**
- Associação de usuários a um ou mais grupos.
- Edição e exclusão de associações.

### **Acesso Restrito**
- Apenas usuários pertencentes ao grupo "Administradores" têm acesso às funcionalidades administrativas:
  - Gerenciamento de usuários.
  - Gerenciamento de grupos.
  - Gerenciamento de associações.

## **Como Executar o Projeto**

### **1. Clonar o Repositório**

```bash
https://github.com/seuusuario/plataforma.git
cd plataforma
```

### **2. Criar e Ativar um Ambiente Virtual**

```bash
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

### **3. Instalar as Dependências**

```bash
pip install -r requirements.txt
```

### **4. Configurar o Banco de Dados**

1. Crie as migrações do banco de dados:
   ```bash
   python manage.py makemigrations
   ```
2. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

### **5. Criar um Superusuário**

Para acessar o sistema como administrador:

```bash
python manage.py createsuperuser
```

### **6. Executar o Servidor**

```bash
python manage.py runserver
```

Acesse a aplicação em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## **Estrutura do Projeto**

- **App `usuarios`:** Gerencia usuários da plataforma.
- **App `grupos`:** Gerencia grupos de usuários.
- **App `usuario_grupo`:** Gerencia associações entre usuários e grupos.

## **Requisitos**

- Python 3.12+
- Django 5.1.4+

## **Como Contribuir**

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e faça commit:
   ```bash
   git commit -m "Minha contribuição"
   ```
4. Envie para o GitHub:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## **Licença**

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
