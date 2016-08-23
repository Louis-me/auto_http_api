# -*- coding:utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="284772894@qq.com"    #用户名
mail_pass="eoehiaxoxxzncaea"   #口令

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(f, to_addr):
    '''

    :param f: 附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = mail_user
    password = mail_pass
    # to_addr = "ashikun@126.com"
    smtp_server = mail_host

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('施坤<%s>' % from_addr)
    msg['To'] = _format_addr('大人 <%s>' % to_addr)
    msg['Subject'] = Header('接口测试报告……', 'utf-8').encode()

    msg.attach(MIMEText('接口测试报告.', 'plain', 'utf-8'))
    part = MIMEApplication(open(f, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=f)
    msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
