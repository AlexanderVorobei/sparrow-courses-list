cd ~
# ������� ����������� ���������
virtualenv env
# ���������� ����������� ���������
source env/scripts/activate
git clone https://github.com/AlexanderVorobei/sparrow-courses-list.git
# ������ ����������� ������
pip install -r requirements.txt
# ���������� ���� ������
flask db init
# ������� �������� ��
flask db migrate -m "courses table"
# ��������� ������
flask run